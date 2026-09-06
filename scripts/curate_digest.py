"""Turn the last 24 hours of raw items into a short, ranked, deduplicated candidate list.

Everything a weak LLM is bad at is done here deterministically, so the pusher (OpenClaw) only
has to translate and format:

- cross-source merge: titles are tokenised (English words / Chinese bigrams) and greedily
  clustered by Jaccard / containment similarity, so one story reported by five outlets is one entry
- ranking: distinct sources x tier weight, Hacker News points, Hugging Face likes, release words
- noise filter: Reddit self-posts, single-source Reddit/Product Hunt links, HF uploads nobody
  liked, items without a title
- cross-day dedupe: stories similar to anything in the pushed-history file (what the server
  actually pulled and pushed on previous days) are dropped
- diversity: at most N entries per source, a minimum quota of Chinese-language entries

Stdlib only; reuses the loaders in daily_digest.py.

usage (in the collect workflow):
  python scripts/curate_digest.py --db data/collector.db --jsonl 'archive/items/*.cn.jsonl' \
      --sources-yaml config/sources.yaml --history archive/digest/pushed-history.jsonl \
      --out-md archive/digest/curated.md --out-json archive/digest/curated.json
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import tempfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from daily_digest import (  # noqa: E402
    fetch_items_db,
    fetch_items_jsonl,
    load_sources_yaml,
    local_time,
    merge_by_url,
    one_line,
    parse_ts,
)

TIER_WEIGHT = {1: 3.0, 2: 2.0, 3: 1.0}
RELEASE_RE = re.compile(
    r"发布|开源|推出|上线|融资|收购|发布会|正式|首个|release|launch|open[- ]?source|open[- ]?weight|announc|"
    r"introduc|unveil|raises|acquire|ships|debut|rolls? out|now available|preview|GA\b",
    re.I,
)
STOP = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with", "is", "are", "its", "it", "as", "by",
    "at", "from", "new", "how", "what", "why", "this", "that", "be", "has", "have", "will", "can", "vs", "into",
    "about", "after", "over", "up", "out", "your", "you", "we", "i", "not", "no", "than", "more", "just", "via",
    "says", "said", "here", "there", "their", "his", "her", "our", "all", "one", "two", "first", "was", "were",
    "但", "和", "与", "的", "了", "在", "是", "为", "将", "也", "被", "让", "把", "对", "从", "到", "及", "或",
}
BRACKET_TAG_RE = re.compile(r"\[(?:[a-z]{1,2}|news|research|discussion|project)\]", re.I)
WORD_RE = re.compile(r"[a-z0-9][a-z0-9_.+-]*|[\u4e00-\u9fff]+")


def tokens(title: str) -> frozenset[str]:
    text = BRACKET_TAG_RE.sub(" ", title.lower())
    out: set[str] = set()
    for w in WORD_RE.findall(text):
        if re.fullmatch(r"[\u4e00-\u9fff]+", w):
            if len(w) == 1:
                continue
            out.update(w[i : i + 2] for i in range(len(w) - 1))
        elif w in STOP or len(w) < 2 or (w.isdigit() and len(w) < 3):
            continue
        else:
            out.add(w.strip("._+-"))
    return frozenset(out)


def similar(a: frozenset[str], b: frozenset[str]) -> bool:
    if not a or not b:
        return False
    inter = len(a & b)
    if inter < 2:
        return False
    jaccard = inter / len(a | b)
    containment = inter / min(len(a), len(b))
    return jaccard >= 0.4 or (containment >= 0.6 and inter >= 3)


class Cluster:
    def __init__(self, item: dict) -> None:
        self.items: list[dict] = [item]
        self.tokens: frozenset[str] = tokens(item["title"])

    def add(self, item: dict) -> None:
        self.items.append(item)
        self.tokens = self.tokens | tokens(item["title"])

    @property
    def rep(self) -> dict:
        # First-party over media over social; then the earliest report.
        return sorted(self.items, key=lambda it: (it["source_tier"], it.get("published_at") or "9"))[0]

    @property
    def sources(self) -> list[str]:
        seen: dict[str, None] = {}
        for it in self.items:
            seen.setdefault(it["source_id"])
        return list(seen)


def cluster_items(items: list[dict]) -> list[Cluster]:
    clusters: list[Cluster] = []
    for item in sorted(items, key=lambda it: (it["source_tier"], it.get("published_at") or "9")):
        tk = tokens(item["title"])
        for c in clusters:
            if similar(tk, c.tokens):
                c.add(item)
                break
        else:
            clusters.append(Cluster(item))
    return clusters


def raw_number(item: dict, key: str) -> float:
    raw = item.get("raw") or {}
    try:
        return float(raw.get(key) or 0)
    except (TypeError, ValueError):
        return 0.0


def is_noise(c: Cluster) -> bool:
    """Single-source social/aggregator entries and unloved model uploads."""
    if len(c.sources) > 1:
        return False
    it = c.items[0]
    sid = it["source_id"]
    if sid.startswith(("reddit", "producthunt")):
        return True  # only worth pushing when another source picked the story up too
    if sid.startswith("hf-models"):
        return raw_number(it, "likes") < 20 and raw_number(it, "downloads") < 5000
    if sid.startswith("hackernews"):
        return raw_number(it, "points") < 80
    return False


def score(c: Cluster, now: datetime) -> float:
    per_source = {}
    for it in c.items:
        per_source[it["source_id"]] = TIER_WEIGHT.get(int(it["source_tier"]), 1.0)
    s = sum(per_source.values()) + 1.5 * (len(per_source) - 1)
    s += min(max(raw_number(it, "points") for it in c.items) / 100, 2.0)
    s += min(math.log10(max(raw_number(it, "likes") for it in c.items) + 1), 2.0)
    if any(RELEASE_RE.search(it["title"]) for it in c.items):
        s += 1.0
    published = parse_ts(c.rep.get("published_at"))
    if published and now - published.astimezone(timezone.utc) < timedelta(hours=12):
        s += 0.5
    return round(s, 2)


def load_history(path: Path | None, days: int) -> list[frozenset[str]]:
    if not path or not path.exists():
        return []
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).date().isoformat()
    out: list[frozenset[str]] = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            entry = json.loads(line)
            if entry.get("pushed_on", "") < cutoff:
                continue
            tk: set[str] = set()
            for t in entry.get("titles") or [entry.get("title", "")]:
                tk |= tokens(t)
            if tk:
                out.append(frozenset(tk))
    return out


def select(clusters: list[Cluster], now: datetime, max_items: int, min_zh: int, per_source_cap: int) -> list[Cluster]:
    ranked = sorted(clusters, key=lambda c: score(c, now), reverse=True)
    chosen: list[Cluster] = []
    used: dict[str, int] = defaultdict(int)

    def take(c: Cluster) -> None:
        chosen.append(c)
        used[c.rep["source_id"]] += 1

    # Chinese-language quota first so domestic coverage is never crowded out.
    for c in ranked:
        if len(chosen) >= min_zh:
            break
        if (c.rep.get("lang") or "").startswith("zh") and used[c.rep["source_id"]] < per_source_cap:
            take(c)
    for c in ranked:
        if len(chosen) >= max_items:
            break
        if c in chosen or used[c.rep["source_id"]] >= per_source_cap:
            continue
        take(c)
    return sorted(chosen, key=lambda c: score(c, now), reverse=True)


def build_markdown(chosen: list[Cluster], names: dict[str, str], now: datetime, stats: dict, summary_chars: int) -> str:
    lines = [
        f"# Daily AI News 候选清单（已去重排序，共 {len(chosen)} 条）",
        f"生成时间：{now.astimezone().strftime('%Y-%m-%d %H:%M %Z')}",
        f"数据窗口：最近 24 小时，{stats['items']} 条原始条目 → {stats['clusters']} 个事件；"
        f"过滤噪音 {stats['noise']} 个，排除前 {stats['history_days']} 天已推送的 {stats['dup']} 个。",
        "",
        "> 给 OpenClaw：本文件已完成跨源合并、跨天去重和排序。不要再筛选、不要联网、不要读其他文件，",
        "> 按 skill daily-ai-news 只做翻译与排版。「来源」里有几家就是几家同时报道，可作为重要程度的依据。",
        "",
    ]
    for i, c in enumerate(chosen, 1):
        rep = c.rep
        src_names = [names.get(s, s) for s in c.sources]
        lines.append(f"## {i}. {one_line(rep['title'], 200)}")
        lines.append(
            f"- 语言：{rep.get('lang') or '?'} ｜ 来源：{'、'.join(src_names[:5])}"
            f"（{len(c.sources)} 个来源） ｜ 热度：{score(c, now)}"
        )
        summary = one_line(rep.get("summary") or rep.get("content"), summary_chars)
        if summary:
            lines.append(f"- 摘要：{summary}")
        lines.append(f"- 发布时间：{local_time(rep.get('published_at') or rep.get('fetched_at'))}")
        lines.append(f"- 链接：{rep['url']}")
        others = [it for it in c.items if it is not rep][:2]
        for it in others:
            lines.append(f"- 同事件报道：{one_line(it['title'], 120)}（{names.get(it['source_id'], it['source_id'])}）")
        lines.append("")
    return "\n".join(lines)


def write_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".curated-", suffix=path.suffix)
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", type=Path, help="collector SQLite file (GitHub-side items)")
    ap.add_argument("--jsonl", action="append", default=[], metavar="GLOB", help="archive files to merge (server side)")
    ap.add_argument("--sources-yaml", type=Path)
    ap.add_argument("--history", type=Path, help="pushed-history.jsonl written by the server after each pull")
    ap.add_argument("--history-days", type=int, default=3)
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--max-items", type=int, default=20)
    ap.add_argument("--min-zh", type=int, default=4)
    ap.add_argument("--per-source-cap", type=int, default=3)
    ap.add_argument("--summary-chars", type=int, default=220)
    ap.add_argument(
        "--exclude-source",
        action="append",
        default=None,
        metavar="ID",
        help="sources never pushed as stories (default: tldr-ai newsletter roundups, github-trending repo names)",
    )
    ap.add_argument("--out-md", type=Path, required=True)
    ap.add_argument("--out-json", type=Path, required=True)
    args = ap.parse_args()
    excluded = set(args.exclude_source or ["tldr-ai", "github-trending"])

    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=args.hours)
    items: list[dict] = fetch_items_db(args.db, since) if args.db else []
    if args.jsonl:
        items = merge_by_url(items, fetch_items_jsonl(args.jsonl, since))
    items = [
        it for it in items if (it.get("title") or "").strip() and it.get("url") and it["source_id"] not in excluded
    ]
    names = {s["id"]: s.get("name", s["id"]) for s in (load_sources_yaml(args.sources_yaml) if args.sources_yaml else [])}

    clusters = cluster_items(items)
    kept = [c for c in clusters if not is_noise(c)]
    noise = len(clusters) - len(kept)
    history = load_history(args.history, args.history_days)
    fresh = [c for c in kept if not any(similar(c.tokens, h) for h in history)]
    dup = len(kept) - len(fresh)

    chosen = select(fresh, now, args.max_items, args.min_zh, args.per_source_cap)
    stats = {"items": len(items), "clusters": len(clusters), "noise": noise, "dup": dup, "history_days": args.history_days}
    write_atomic(args.out_md, build_markdown(chosen, names, now, stats, args.summary_chars))
    payload = [
        {
            "rank": i,
            "title": c.rep["title"],
            "lang": c.rep.get("lang"),
            "url": c.rep["url"],
            "score": score(c, now),
            "sources": c.sources,
            "titles": [it["title"] for it in c.items],
            "published_at": c.rep.get("published_at"),
            "summary": one_line(c.rep.get("summary") or c.rep.get("content"), args.summary_chars),
        }
        for i, c in enumerate(chosen, 1)
    ]
    write_atomic(args.out_json, json.dumps({"generated_at": now.isoformat(), "stats": stats, "items": payload}, ensure_ascii=False, indent=1))
    print(
        f"curated {len(chosen)} of {len(clusters)} clusters from {len(items)} items "
        f"(noise {noise}, already pushed {dup}) -> {args.out_md}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
