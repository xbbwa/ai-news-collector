"""Write a Markdown digest of recently collected items for a downstream reader (OpenClaw).

This is the drop-in replacement for the old ~/scripts/daily_ai_news.py on the server: same
output file, same role (a file the pusher reads instead of going online), but fed by the
collector's HTTP API instead of four hard-coded RSS feeds. Stdlib only, so it runs with the
host's system python3 straight from cron - no venv, no docker exec.

usage:
  python3 scripts/daily_digest.py --out /mnt/data/openclaw-kb/openclawdata/daily-ai-news-summary.md
      [--api http://localhost:8000] [--hours 24] [--max-per-source 8] [--summary-chars 400]
"""
from __future__ import annotations

import argparse
import json
import os
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


def fetch_items(api: str, since: datetime) -> list[dict]:
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
        "> 本文件由 ai-news-collector 从 HTTP API 导出生成，每天覆盖更新。",
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
    ap.add_argument("--api", default=os.environ.get("COLLECTOR_API", "http://localhost:8000"))
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--max-per-source", type=int, default=8)
    ap.add_argument("--summary-chars", type=int, default=400)
    args = ap.parse_args()

    since = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    try:
        items = fetch_items(args.api, since)
        sources = get_json(f"{args.api}/sources")
    except (URLError, OSError, KeyError, ValueError) as exc:
        print(f"ERROR: cannot read collector API at {args.api}: {exc}", file=sys.stderr)
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
