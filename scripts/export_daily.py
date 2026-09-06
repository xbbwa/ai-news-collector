"""Append newly collected items to per-day JSONL archives and trim the working database.

Used by the GitHub Actions workflow right after `python -m collector once`:

  python scripts/export_daily.py --db data/collector.db --out-dir archive/items \
      --cursor data/export_cursor --prune-days 14

- Every item with id > cursor is appended, as the same JSON the API returns (full text
  included), to items/<fetched_at UTC date>.jsonl. The archive is complete and append-only.
- The cursor file is advanced to the last exported id.
- Rows fetched more than --prune-days ago are deleted from the DB (they live in the archive);
  the DB only needs to remember enough URL hashes to dedupe entries that stay in feeds.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import delete, select  # noqa: E402

from collector.db import init_db, make_engine, make_session_factory  # noqa: E402
from collector.models import Item, utcnow  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True, help="directory receiving <date>.jsonl files")
    ap.add_argument("--cursor", type=Path, required=True, help="file holding the last exported item id")
    ap.add_argument("--prune-days", type=int, default=0, help="delete items fetched more than N days ago (0 = keep)")
    ap.add_argument(
        "--file-suffix",
        default="",
        help='inserted before ".jsonl", e.g. ".cn" -> 2026-09-06.cn.jsonl, so two collectors never write the same file',
    )
    args = ap.parse_args()

    cursor = int(args.cursor.read_text().strip() or 0) if args.cursor.exists() else 0
    engine = make_engine(f"sqlite:///{args.db.resolve().as_posix()}")
    init_db(engine)
    session_factory = make_session_factory(engine)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    handles: dict[str, object] = {}
    exported = 0
    last_id = cursor
    with session_factory() as s:
        for row in s.scalars(select(Item).where(Item.id > cursor).order_by(Item.id)):
            day = row.fetched_at.strftime("%Y-%m-%d")
            fh = handles.get(day)
            if fh is None:
                fh = handles[day] = open(  # noqa: SIM115
                    args.out_dir / f"{day}{args.file_suffix}.jsonl", "a", encoding="utf-8"
                )
            fh.write(json.dumps(row.to_dict(), ensure_ascii=False) + "\n")
            exported += 1
            last_id = row.id
        for fh in handles.values():
            fh.close()  # type: ignore[attr-defined]

        pruned = 0
        if args.prune_days:
            cutoff = utcnow() - timedelta(days=args.prune_days)
            pruned = s.execute(delete(Item).where(Item.fetched_at < cutoff)).rowcount
            s.commit()

    args.cursor.parent.mkdir(parents=True, exist_ok=True)
    args.cursor.write_text(f"{last_id}\n")

    # Leave a single self-contained .db file behind (no -wal/-shm) so it can be uploaded as is.
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        if pruned:
            conn.exec_driver_sql("VACUUM")
        conn.exec_driver_sql("PRAGMA wal_checkpoint(TRUNCATE)")
    engine.dispose()

    span = f"ids {cursor + 1}..{last_id}" if exported else "nothing new"
    files = [f"{day}{args.file_suffix}.jsonl" for day in sorted(handles)]
    print(f"exported {exported} items ({span}) into {files}; pruned {pruned} old rows")
    if gh_out := os.environ.get("GITHUB_OUTPUT"):
        with open(gh_out, "a", encoding="utf-8") as fh:
            fh.write(f"exported={exported}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
