"""Write a Markdown digest of recently collected items for a downstream reader (OpenClaw).

Same output file and role as the old ~/scripts/daily_ai_news.py on the server (a file the
pusher reads instead of going online), fed by the collector instead of four hard-coded feeds.
Stdlib only. Data sources (combinable):

  --api URL      running collector API (self-hosted Docker setup)
  --db PATH      the SQLite file directly (GitHub Actions run, where no API is up)
  --jsonl GLOB   archive files from another collector (e.g. the China box's items/*.cn.jsonl);
                 repeatable; items are merged with the above and deduplicated by URL

usage:
  python3 scripts/daily_digest.py --out digest/latest.md --db data/collector.db --sources-yaml config/sources.yaml \
      --jsonl 'archive/items/*.cn.jsonl' [--hours 24] [--max-per-source 8] [--summary-chars 400]
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sqlite3
import sys
import tempfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import urlopen

TIER_NAMES = {1: "一手来源（实验室 / 公司 / 论文）", 2: "专业媒体", 3: "社交 / 聚合"}


def get_json(url: str) -> object:
    with urlopen(url, timeout=60) as resp:
        return json.load(resp)


def fetch_items_api(api: str, since: datetime) -> list[dict]:
    items: list[dict] = []
    since_id = 0
    while True:
        query = urlencode(
            {"since_id": since_id, "limit": 1000, "fetched_after": since.isoformat(), "include_content": "true"}
        )
        page = get_json(f"{api}/items?{query}")
        items.extend(page["items"])
        if page["count"] < 1000:
            return items
        since_id = page["next_since_id"]


def fetch_items_db(db_path: Path, since: datetime) -> list[dict]:
    """Read straight from the collector's SQLite file (datetimes are stored naive UTC)."""
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            "select id, source_id, source_tier, url, title, author, summary, content, published_at, fetched_at "
            "from items where fetched_at >= ? order by id",
            (since.astimezone(timezone.utc).replace(tzinfo=None).isoformat(sep=" "),),
        ).fetchall()
    finally:
        conn.close()

    def iso(value: str | None) -> str | None:
        return f"{value.replace(' ', 'T')}+00:00" if value else None

    return [
        {**dict(r), "published_at": iso(r["published_at"]), "fetched_at": iso(r["fetched_at"])} for r in rows
    ]


def fetch_items_jsonl(patterns: list[str], since: datetime) -> list[dict]:
    """Items from per-day archive files. Only files whose date could hold items in the window are read."""
    earliest = (since - timedelta(days=1)).date().isoformat()
    items: list[dict] = []
    for pattern in patterns:
        for path in sorted(glob.glob(pattern)):
            if Path(path).name[:10] < earliest:  # names start with YYYY-MM-DD
                continue
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    if not line.strip():
                        continue
                    item = json.loads(line)
                    fetched = parse_ts(item.get("fetched_at"))
                    if fetched is not None and fetched >= since:
                        items.append(item)
    return items


def merge_by_url(*groups: list[dict]) -> list[dict]:
    """Two collectors may store the same article (an HN link to a 量子位 story); keep the first seen."""
    seen: set[str] = set()
    merged: list[dict] = []
    for group in groups:
        for item in group:
            key = (item.get("url") or "").rstrip("/")
            if key in seen:
                continue
            seen.add(key)
            merged.append(item)
    return merged


def load_sources_yaml(path: Path) -> list[dict]:
    """Source names/langs for headings. PyYAML is optional; without it ids are shown."""
    try:
        import yaml  # type: ignore[import-not-found]
    except ImportError:
        return []
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    # Mirror SourceConfig's default for entries that leave lang unset.
    return [{"lang": "en", **s} for s in doc.get("sources") or [] if isinstance(s, dict) and "id" in s]


def parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def local_time(value: str | None) -> str:
    dt = parse_ts(value)
    return dt.astimezone().strftime("%Y-%m-%d %H:%M %Z") if dt else "未知时间"


def one_line(text: str | None, limit: int) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= limit else text[:limit].rstrip() + "..."


def build_markdown(items: list[dict], sources: list[dict], hours: int, max_per_source: int, summary_chars: int) -> str:
    source_meta = {s["id"]: s for s in sources}
    by_source: dict[str, list[dict]] = defaultdict(list)
    for it in items:
        by_source[it["source_id"]].append(it)

    now = datetime.now().astimezone()
    lines = [
        "# Daily AI News（原文采集，国内外）",
        f"生成时间：{now.strftime('%Y-%m-%d %H:%M %Z')}",
        f"时间窗口：最近 {hours} 小时内采集到的条目；每个信源最多列 {max_per_source} 条，按发布时间倒序。",
        "",
        "> 本文件由 ai-news-collector 自动生成（github.com/xbbwa/ai-news-collector，data 分支），每小时覆盖更新。",
        "> OpenClaw 推送时只应读取本文件，不要联网、不抓全文、不扩展搜索。",
        "> 摘要为原文节选（未翻译、未清洗）；英文条目请在推送时翻译成中文。",
        "",
    ]

    total = 0
    for tier in (1, 2, 3):
        tier_sources = sorted(
            (sid for sid, its in by_source.items() if its and its[0]["source_tier"] == tier),
            key=lambda sid: (source_meta.get(sid, {}).get("lang", ""), sid),
        )
        if not tier_sources:
            continue
        lines.append(f"# Tier {tier} — {TIER_NAMES[tier]}")
        lines.append("")
        for sid in tier_sources:
            entries = sorted(
                by_source[sid], key=lambda it: it.get("published_at") or it.get("fetched_at") or "", reverse=True
            )[:max_per_source]
            meta = source_meta.get(sid, {})
            lines.append(f"## {meta.get('name', sid)}（{sid}，{meta.get('lang', '?')}，本窗口共 {len(by_source[sid])} 条）")
            lines.append("")
            for i, it in enumerate(entries, 1):
                lines.append(f"### {i}. {one_line(it['title'], 200)}")
                summary = one_line(it.get("summary") or it.get("content"), summary_chars)
                if summary:
                    lines.append(f"- 摘要：{summary}")
                if it.get("author"):
                    lines.append(f"- 作者：{one_line(it['author'], 80)}")
                lines.append(f"- 发布时间：{local_time(it.get('published_at') or it.get('fetched_at'))}")
                lines.append(f"- 链接：{it['url']}")
                lines.append("")
                total += 1

    lines += [
        "---",
        f"共列出 {total} 条（窗口内采集总数 {len(items)} 条，来自 {len(by_source)} 个信源）",
        "",
        "## OpenClaw 推送提示",
        "请基于本文件生成中文 Daily AI News 推送，不要联网，不要抓原文，不要扩展搜索。",
        "优先 Tier 1 一手来源和国内外媒体中被多个信源同时报道的事件；Tier 3 社交条目只做补充。",
        "每日只保留最新内容，覆盖更新。",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, type=Path, help="markdown file to (over)write")
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--api", help="collector API base URL (default: $COLLECTOR_API or http://localhost:8000)")
    src.add_argument("--db", type=Path, help="read the SQLite file directly instead of the API")
    ap.add_argument("--jsonl", action="append", default=[], metavar="GLOB", help="archive files to merge in (repeatable)")
    ap.add_argument("--sources-yaml", type=Path, help="with --db: sources.yaml for names/langs (needs PyYAML)")
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--max-per-source", type=int, default=8)
    ap.add_argument("--summary-chars", type=int, default=400)
    args = ap.parse_args()

    since = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    try:
        if args.db:
            items = fetch_items_db(args.db, since)
            sources = load_sources_yaml(args.sources_yaml) if args.sources_yaml else []
        else:
            api = args.api or os.environ.get("COLLECTOR_API", "http://localhost:8000")
            items = fetch_items_api(api, since)
            sources = get_json(f"{api}/sources")
        if args.jsonl:
            items = merge_by_url(items, fetch_items_jsonl(args.jsonl, since))
    except (URLError, OSError, KeyError, ValueError, sqlite3.Error) as exc:
        print(f"ERROR: cannot read collector data: {exc}", file=sys.stderr)
        return 1

    text = build_markdown(items, sources, args.hours, args.max_per_source, args.summary_chars)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    # Write atomically so a reader never sees a half-written file.
    fd, tmp = tempfile.mkstemp(dir=args.out.parent, prefix=".digest-", suffix=".md")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(tmp, 0o644)  # mkstemp creates 0600; the reader may run as another user
    os.replace(tmp, args.out)
    print(f"OK: wrote {args.out} ({len(items)} items in the last {args.hours}h)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
