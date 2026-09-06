"""Record the curated stories the server just pulled as "pushed", for next day's cross-day dedupe.

Runs on the China box right after sync_digest.sh downloads digest/curated.json. Appends one line
per story to pushed-history.jsonl ({"pushed_on", "url", "titles"}), skips URLs already present,
drops entries older than --keep-days. The file is then uploaded to the data branch by
publish_archive.py so curate_digest.py (on GitHub) can exclude those stories. Stdlib only.

usage: python3 scripts/mark_pushed.py --curated data/curated.json --history archive/digest/pushed-history.jsonl
"""
from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timedelta
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--curated", type=Path, required=True)
    ap.add_argument("--history", type=Path, required=True)
    ap.add_argument("--keep-days", type=int, default=14)
    args = ap.parse_args()

    curated = json.loads(args.curated.read_text(encoding="utf-8"))
    today = date.today().isoformat()  # local (server) date, i.e. Beijing time
    cutoff = (datetime.now() - timedelta(days=args.keep_days)).date().isoformat()

    existing: list[dict] = []
    if args.history.exists():
        for line in args.history.read_text(encoding="utf-8").splitlines():
            if line.strip():
                entry = json.loads(line)
                if entry.get("pushed_on", "") >= cutoff:
                    existing.append(entry)
    known = {e.get("url") for e in existing}

    added = 0
    for item in curated.get("items", []):
        if item.get("url") in known:
            continue
        existing.append({"pushed_on": today, "url": item["url"], "titles": item.get("titles") or [item["title"]]})
        added += 1

    args.history.parent.mkdir(parents=True, exist_ok=True)
    args.history.write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in existing), encoding="utf-8")
    print(f"pushed-history: +{added} stories for {today}, {len(existing)} kept (last {args.keep_days} days)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
