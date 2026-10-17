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
- diversity: at most N entries per source, an exact source-origin quota (6 China / 14 international
  for the default 20); all international stories are listed first, then all China stories

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
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from daily_digest import (  # noqa: E402
    fetch_items_db,
    fetch_items_jsonl,
    load_sources_yaml,
    local_time,
    merge_by_url,
    one_line,
    parse_ts,
)

try:  # same matcher the collector uses; absent when the repo is not checked out (stdlib-only mode)
    from collector.pipeline import _keyword_pattern
except ImportError:  # pragma: no cover
    _keyword_pattern = None

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
ENTITY_STOP = STOP | {
    "ai", "model", "models", "agent", "agents", "news", "report", "research",
    "company", "companies", "technology", "tech", "open", "source", "system",
    "data", "using", "based", "latest", "today", "announces", "announced",
}
KNOWN_ENTITIES = {
    "openai", "chatgpt", "anthropic", "claude", "gemini", "deepmind", "deepseek",
    "qwen", "kimi", "mistral", "llama", "nvidia", "huggingface", "meta", "microsoft",
    "google", "apple", "amazon", "aws", "alibaba", "tencent", "bytedance", "seedance",
    "grok", "xai", "copilot", "minimax", "moonshot", "cohere", "stability",
    "muse",
}
ACTION_PATTERNS = {
    "funding": re.compile(r"融资|募资|估值|投资|funding|fundraise|raises?|valuation|series [a-z]", re.I),
    "acquisition": re.compile(r"收购|并购|acquir|merger|takeover", re.I),
    "release": re.compile(r"发布|推出|上线|开源|release|launch|introduc|announc|unveil|rolls? out|open[- ]?weight", re.I),
    "security": re.compile(r"安全|攻击|漏洞|风险|警告|security|attack|hack|vulnerab|kill|risk|warn|threat", re.I),
    "policy": re.compile(r"监管|法案|政策|禁令|regulat|policy|law|ban", re.I),
}
FAMILY_CAPS = {
    "academic-papers": 4,
    "model-releases": 2,
    "social-discovery": 2,
}
GIANT_CORPS = {
    "google", "meta", "microsoft", "apple", "amazon", "aws", "alibaba", "tencent", "bytedance", "nvidia",
}
BOILERPLATE_RE = re.compile(
    r"^(?:share this|subscribe|related posts?|read more|copyright|all rights reserved|"
    r"sign up for|follow us|advertisement|sponsored|"
    r"延伸阅读|相关阅读|责编|编辑[:：]|本文来自|未经允许|欢迎关注|点击阅读原文)",
    re.I,
)
STEM_RE = re.compile(r"^([a-z]{3,})[-_.]?v?\d", re.I)


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


def entity_tokens(title: str) -> frozenset[str]:
    """Cross-language anchors: model/company names survive in both English and Chinese titles."""
    out = set()
    for raw in re.findall(r"[A-Za-z0-9][A-Za-z0-9_.+-]*", title):
        value = raw.lower().strip("._+-")
        is_camel = any(ch.islower() for ch in raw) and any(ch.isupper() for ch in raw[1:])
        if not value or value in ENTITY_STOP:
            continue
        if value in KNOWN_ENTITIES or any(ch.isdigit() for ch in value) or is_camel:
            out.add(value)
    # Normalize the common two-word brand spelling to the same anchor as "HuggingFace".
    low = title.lower()
    if "hugging face" in low or "huggingface" in low:
        out.add("huggingface")
        out.discard("hugging")
        out.discard("face")
    return frozenset(out)


def action_tokens(title: str) -> frozenset[str]:
    return frozenset(name for name, pattern in ACTION_PATTERNS.items() if pattern.search(title))


def same_event(
    left_tokens: frozenset[str],
    right_tokens: frozenset[str],
    left_entities: frozenset[str],
    right_entities: frozenset[str],
    left_actions: frozenset[str],
    right_actions: frozenset[str],
) -> bool:
    if similar(left_tokens, right_tokens):
        return True
    common_entities = left_entities & right_entities
    if len(common_entities) >= 2:
        return True
    meaningful_common = (left_tokens & right_tokens) - ENTITY_STOP
    if common_entities and len(meaningful_common) >= 2:
        return True
    # One shared company plus an unambiguous corporate event catches cross-language headlines
    # such as "Mistral raises €3B" / "Mistral 完成 30 亿欧元融资" without merging every release.
    strong_actions = {"funding", "acquisition", "security", "policy"}
    return bool(common_entities and left_actions & right_actions & strong_actions)


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
        self.entities: frozenset[str] = entity_tokens(item["title"])
        self.actions: frozenset[str] = action_tokens(item["title"])

    def add(self, item: dict) -> None:
        self.items.append(item)
        self.tokens = self.tokens | tokens(item["title"])
        self.entities = self.entities | entity_tokens(item["title"])
        self.actions = self.actions | action_tokens(item["title"])

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
        entities = entity_tokens(item["title"])
        actions = action_tokens(item["title"])
        for c in clusters:
            if same_event(tk, c.tokens, entities, c.entities, actions, c.actions):
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


def off_topic(c: Cluster, keywords_by_source: dict[str, list[str]]) -> bool:
    """General-purpose feeds pass the collector's filter when the *summary* mentions AI; for the
    push we want the story itself to be about AI, so the title must match when every source in
    the cluster is a keyword-filtered feed (a bond-market explainer from Axios + CNBC is not news here)."""
    if _keyword_pattern is None:
        return False
    if any(not keywords_by_source.get(it["source_id"]) for it in c.items):
        return False  # at least one AI-vertical source carried it
    return not any(
        _keyword_pattern(tuple(keywords_by_source[it["source_id"]])).search(it["title"]) for it in c.items
    )


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


def load_history(path: Path | None, days: int) -> list[dict]:
    if not path or not path.exists():
        return []
    cutoff = (
        (datetime.now(timezone.utc) - timedelta(days=days)).date().isoformat()
        if days > 0
        else None
    )
    out: list[dict] = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            entry = json.loads(line)
            if cutoff is not None and entry.get("pushed_on", "") < cutoff:
                continue
            history_titles = entry.get("titles") or [entry.get("title", "")]
            tk: set[str] = set()
            entities: set[str] = set()
            actions: set[str] = set()
            for title in history_titles:
                tk |= tokens(title)
                entities |= entity_tokens(title)
                actions |= action_tokens(title)
            out.append(
                {
                    "pushed_on": entry.get("pushed_on", ""),
                    "title": history_titles[0] if history_titles else "",
                    "titles": history_titles,
                    "url": (entry.get("url") or "").rstrip("/"),
                    "tokens": frozenset(tk),
                    "entities": frozenset(entities),
                    "actions": frozenset(actions),
                }
            )
    return out


def was_pushed(c: Cluster, history: list[dict]) -> bool:
    urls = {(item.get("url") or "").rstrip("/") for item in c.items}
    for old in history:
        if old["url"] and old["url"] in urls:
            return True  # permanent exact-URL dedupe
        if same_event(
            c.tokens,
            old["tokens"],
            c.entities,
            old["entities"],
            c.actions,
            old["actions"],
        ):
            return True
    return False


def _entity_stems(entities: frozenset[str]) -> frozenset[str]:
    """Extract base family stems from versioned entities (e.g. 'gpt-6' -> 'gpt', 'qwen2.5' -> 'qwen')."""
    stems: set[str] = set()
    for ent in entities:
        m = STEM_RE.match(ent)
        if m:
            stems.add(m.group(1).lower())
        elif ent in KNOWN_ENTITIES:
            stems.add(ent)
    return frozenset(stems)


def find_history_callback(
    c: Cluster,
    history: list[dict],
    *,
    callback_days: int = 30,
    now: datetime | None = None,
) -> dict | None:
    """Find the most relevant prior story in pushed-history that shares specific entities/model stems
    with this cluster without being the exact same event."""
    if callback_days <= 0 or not history or not c.entities:
        return None
    current = now or datetime.now(timezone.utc)
    cutoff = (current - timedelta(days=callback_days)).date().isoformat()
    urls = {(item.get("url") or "").rstrip("/") for item in c.items}
    c_stems = _entity_stems(c.entities)

    best_score = 0.0
    best_date = ""
    best_entry: dict | None = None
    best_anchors: set[str] = set()

    for old in history:
        old_url = (old.get("url") or "").rstrip("/")
        if old_url and old_url in urls:
            continue
        pushed_on = old.get("pushed_on") or ""
        if pushed_on and pushed_on < cutoff:
            continue
        old_tokens = old.get("tokens") or frozenset()
        old_entities = old.get("entities") or frozenset()
        old_actions = old.get("actions") or frozenset()
        if same_event(c.tokens, old_tokens, c.entities, old_entities, c.actions, old_actions):
            continue

        common_entities = set(c.entities & old_entities)
        common_stems = set((c_stems & _entity_stems(old_entities)) - GIANT_CORPS)
        anchors = common_entities | common_stems
        if not anchors:
            continue

        specific = anchors - GIANT_CORPS
        shared_actions = c.actions & old_actions
        meaningful_common = (c.tokens & old_tokens) - ENTITY_STOP - anchors

        if specific:
            ultra_specific = {e for e in specific if e not in KNOWN_ENTITIES}
            rel_score = len(ultra_specific) * 3.5 + len(specific - ultra_specific) * 2.0
            rel_score += len(meaningful_common) * 1.5 + (1.0 if shared_actions else 0.0)
        else:
            # Giant tech conglomerate alone only triggers a callback when paired with shared action or topic token
            if not (shared_actions or meaningful_common):
                continue
            rel_score = 1.0 + len(meaningful_common) * 1.5 + (0.5 if shared_actions else 0.0)

        if (rel_score, pushed_on) > (best_score, best_date):
            best_score = rel_score
            best_date = pushed_on
            best_entry = old
            best_anchors = specific or anchors

    if best_entry is None:
        return None
    title = best_entry.get("title") or (best_entry.get("titles") or [""])[0]
    if not title:
        return None
    return {
        "pushed_on": best_entry.get("pushed_on", ""),
        "title": title,
        "url": best_entry.get("url", ""),
        "entities": sorted(best_anchors),
    }


def _overlaps_summary(paragraph: str, summary: str, title: str) -> bool:
    """Return True when a paragraph mostly repeats the RSS summary or headline."""
    p_low = " ".join(paragraph.lower().split())
    for ref in (summary, title):
        if not ref:
            continue
        r_low = " ".join(ref.lower().split()).rstrip(".")
        if len(r_low) >= 25 and (p_low.startswith(r_low[:50]) or r_low.startswith(p_low[:50])):
            return True
        p_tk = tokens(paragraph)
        r_tk = tokens(ref)
        if p_tk and r_tk and len(p_tk & r_tk) / min(len(p_tk), len(r_tk)) >= 0.7:
            return True
    return False


def sample_content_excerpt(c: Cluster, summary: str = "", limit: int = 360) -> str:
    """Sample head (problem/method) + tail (conclusion/metrics) from full-text `content` for a
    selected cluster, skipping leading paragraphs that merely repeat `summary`."""
    if limit <= 0:
        return ""
    candidates = [c.rep, *(it for it in c.items if it is not c.rep)]
    raw_content = ""
    for it in candidates:
        text = (it.get("content") or "").strip()
        if len(text) >= 200:
            raw_content = text
            break
        if len(text) > len(raw_content):
            raw_content = text
    if not raw_content or len(" ".join(raw_content.split())) < 100:
        return ""

    raw_blocks = [
        " ".join(b.split())
        for b in re.split(r"\n+", raw_content)
        if len(" ".join(b.split())) >= 30 and not BOILERPLATE_RE.search(" ".join(b.split()))
    ]
    if len(raw_blocks) <= 1:
        # Single-paragraph full text: split into sentence groups
        sentences = [
            s.strip()
            for s in re.split(r"(?<=[.!?。！？])\s+", " ".join(raw_content.split()))
            if len(s.strip()) >= 20 and not BOILERPLATE_RE.search(s.strip())
        ]
        raw_blocks = sentences if sentences else raw_blocks

    title = c.rep.get("title") or ""
    blocks = [b for b in raw_blocks if not _overlaps_summary(b, summary, title)]
    if not blocks:
        return ""

    joined = " ".join(blocks)
    if len(joined) <= limit:
        return joined

    if len(blocks) == 1:
        text = blocks[0]
        head_budget = int(limit * 0.55)
        tail_budget = max(limit - head_budget - 3, 40)
        head = one_line(text, head_budget)
        tail = text[-tail_budget:].lstrip()
        return f"{head} … {tail}"

    head_budget = int(limit * 0.55)
    head_src = blocks[0] if len(blocks[0]) >= 60 or len(blocks) == 2 else f"{blocks[0]} {blocks[1]}"
    head = one_line(head_src, head_budget)
    tail_budget = max(limit - len(head) - 3, 60)
    tail_src = blocks[-1] if len(blocks[-1]) >= 50 or len(blocks) == 2 else f"{blocks[-2]} {blocks[-1]}"
    tail = one_line(tail_src, tail_budget)
    if head == tail or _overlaps_summary(tail, head, ""):
        return one_line(joined, limit)
    return f"{head} … {tail}"


def parse_curated_md_items(md: str) -> list[dict]:
    """Extract ordered ({region, url, title}) items from a curated.md string."""
    items: list[dict] = []
    region = "intl"
    current: dict | None = None
    for raw_line in md.splitlines():
        line = raw_line.strip()
        if line in ("国外：", "国外:", "国际：", "国际:"):
            region = "intl"
        elif line in ("国内：", "国内:"):
            region = "cn"
        elif line.startswith("## "):
            if current and current.get("url"):
                items.append(current)
            title = re.sub(r"^##\s*\d+\.\s*", "", line)
            current = {"region": region, "title": title, "url": ""}
        elif current is not None and line.startswith("- 链接："):
            current["url"] = line.split("：", 1)[1].strip()
    if current and current.get("url"):
        items.append(current)
    return items


def backfill_links(
    text: str,
    curated: dict | list[dict] | str,
    *,
    style: str = "line",
) -> str:
    """Deterministically inject canonical source URLs into an LLM-rendered Daily AI News text
    without requiring the LLM to generate or copy URLs during inference."""
    if isinstance(curated, str):
        raw_items = parse_curated_md_items(curated)
    elif isinstance(curated, dict):
        raw_items = list(curated.get("items") or [])
    else:
        raw_items = list(curated)

    by_region: dict[str, list[dict]] = {"intl": [], "cn": []}
    for it in raw_items:
        reg = it.get("region") or "intl"
        by_region.setdefault(reg, []).append(it)

    lines = text.splitlines()
    out: list[str] = []
    current_region: str | None = None
    active_url: str = ""

    def flush_link() -> None:
        nonlocal active_url
        if not active_url:
            return
        if style == "inline" and out:
            if active_url not in out[-1] and "http://" not in out[-1] and "https://" not in out[-1]:
                out[-1] = f"{out[-1]}｜🔗 {active_url}"
        else:
            out.append(f"   🔗 {active_url}")
        active_url = ""

    item_header_re = re.compile(r"^\s*(\d+)\.\s*【")
    region_intl_re = re.compile(r"^\s*(?:国外|国际)\s*[：:]\s*$")
    region_cn_re = re.compile(r"^\s*国内\s*[：:]\s*$")

    for raw_line in lines:
        if region_intl_re.match(raw_line):
            flush_link()
            current_region = "intl"
            out.append(raw_line)
            continue
        if region_cn_re.match(raw_line):
            flush_link()
            current_region = "cn"
            out.append(raw_line)
            continue

        m = item_header_re.match(raw_line)
        if m:
            flush_link()
            idx = int(m.group(1)) - 1
            pool = by_region.get(current_region or "", []) if current_region else raw_items
            if not pool and current_region:
                pool = raw_items
            active_url = (pool[idx].get("url") or "").strip() if 0 <= idx < len(pool) else ""
            out.append(raw_line)
            continue

        if not raw_line.strip():
            flush_link()
            out.append(raw_line)
            continue

        if active_url and (active_url in raw_line or "🔗" in raw_line or "http://" in raw_line or "https://" in raw_line):
            active_url = ""
        out.append(raw_line)

    flush_link()
    return "\n".join(out)


def cluster_region(c: Cluster, regions: dict[str, str]) -> str:
    """Quota follows the representative/most authoritative source, not title language."""
    return regions.get(c.rep["source_id"], "intl")


def source_family(source_id: str) -> str:
    if source_id.startswith("arxiv-") or source_id in {"hf-daily-papers", "nature-ml"}:
        return "academic-papers"
    if source_id.startswith("hf-models"):
        return "model-releases"
    if source_id.startswith(("reddit-", "hackernews-", "producthunt-")):
        return "social-discovery"
    return source_id


def select(
    clusters: list[Cluster],
    now: datetime,
    max_items: int,
    cn_items: int,
    per_source_cap: int,
    regions: dict[str, str],
) -> list[Cluster]:
    ranked = sorted(clusters, key=lambda c: score(c, now), reverse=True)
    targets = {"cn": cn_items, "intl": max_items - cn_items}
    selected: dict[str, list[Cluster]] = {"cn": [], "intl": []}
    used: dict[tuple[str, str], int] = defaultdict(int)
    family_used: dict[tuple[str, str], int] = defaultdict(int)

    for region in ("intl", "cn"):
        for c in ranked:
            if len(selected[region]) >= targets[region]:
                break
            if cluster_region(c, regions) != region:
                continue
            source = c.rep["source_id"]
            if used[(region, source)] >= per_source_cap:
                continue
            family = source_family(source)
            family_cap = FAMILY_CAPS.get(family)
            if family_cap is not None and family_used[(region, family)] >= family_cap:
                continue
            selected[region].append(c)
            used[(region, source)] += 1
            family_used[(region, family)] += 1

    # User-facing order is deliberate: all international stories first, China stories last.
    return selected["intl"] + selected["cn"]


def build_markdown(
    chosen: list[Cluster],
    names: dict[str, str],
    langs: dict[str, str],
    regions: dict[str, str],
    now: datetime,
    stats: dict,
    summary_chars: int,
    *,
    excerpt_chars: int = 360,
    history: list[dict] | None = None,
    callback_days: int = 30,
) -> str:
    history_scope = "全部历史" if stats["history_days"] == 0 else f"前 {stats['history_days']} 天"
    lines = [
        f"# Daily AI News 候选清单（国外 {stats['selected_intl']}｜国内 {stats['selected_cn']}）",
        f"生成时间：{now.astimezone().strftime('%Y-%m-%d %H:%M %Z')}",
        f"数据窗口：最近 24 小时，{stats['items']} 条原始条目 → {stats['clusters']} 个事件；"
        f"过滤噪音 {stats['noise']} 个，排除{history_scope}已推送的 {stats['dup']} 个。",
        f"强制配额：国外源 {stats['selected_intl']}/{stats['target_intl']}，"
        f"国内源 {stats['selected_cn']}/{stats['target_cn']}；国外全部在前，国内全部在后。",
        "",
        "> 给 OpenClaw：本文件已完成跨源合并、跨天去重和排序。不要再筛选、不要联网、不要读其他文件，",
        "> 按 skill daily-ai-news 只做翻译与排版。「来源」里有几家就是几家同时报道，可作为重要程度的依据。",
        "",
    ]
    current_region = None
    section_index = 0
    for c in chosen:
        rep = c.rep
        src_names = [names.get(s, s) for s in c.sources]
        region = cluster_region(c, regions)
        region_label = "国内源" if region == "cn" else "国外源"
        lang = rep.get("lang") or langs.get(rep["source_id"], "en")
        if region != current_region:
            current_region = region
            section_index = 0
            lines.append("国内：" if region == "cn" else "国外：")
            lines.append("")
        section_index += 1
        lines.append(f"## {section_index}. {one_line(rep['title'], 200)}")
        lines.append(
            f"- 地区：{region_label} ｜ 语言：{lang} ｜ 来源：{'、'.join(src_names[:5])}"
            f"（{len(c.sources)} 个来源） ｜ 热度：{score(c, now)}"
        )
        summary = one_line(rep.get("summary") or rep.get("content"), summary_chars)
        if summary:
            lines.append(f"- 摘要：{summary}")
        excerpt = sample_content_excerpt(c, summary=summary, limit=excerpt_chars)
        if excerpt:
            lines.append(f"- 正文抽样：{excerpt}")
        if history:
            callback = find_history_callback(c, history, callback_days=callback_days, now=now)
            if callback:
                cb_date = callback.get("pushed_on") or "此前"
                cb_entities = "、".join(callback.get("entities") or [])
                suffix = f"（关联实体：{cb_entities}）" if cb_entities else ""
                lines.append(f"- 历史关联：{cb_date} 曾报道《{one_line(callback['title'], 120)}》{suffix}")
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
    ap.add_argument(
        "--history-days",
        type=int,
        default=0,
        help="fuzzy history window in days; 0 compares all retained history (default)",
    )
    ap.add_argument(
        "--callback-days",
        type=int,
        default=30,
        help="window in days for matching related prior stories via entity callbacks (0 disables)",
    )
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--max-items", type=int, default=20)
    ap.add_argument(
        "--cn-items",
        type=int,
        help="exact number selected from region=cn (default: 30%% of --max-items)",
    )
    ap.add_argument("--per-source-cap", type=int, default=3)
    ap.add_argument("--summary-chars", type=int, default=220)
    ap.add_argument(
        "--excerpt-chars",
        type=int,
        default=360,
        help="head+tail full-text excerpt length for selected Top-N items (0 disables)",
    )
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
    cn_items = round(args.max_items * 0.3) if args.cn_items is None else args.cn_items
    if not 0 <= cn_items <= args.max_items:
        ap.error("--cn-items must be between 0 and --max-items")
    excluded = set(args.exclude_source or ["tldr-ai", "github-trending"])

    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=args.hours)
    items: list[dict] = fetch_items_db(args.db, since) if args.db else []
    if args.jsonl:
        items = merge_by_url(items, fetch_items_jsonl(args.jsonl, since))
    items = [
        it for it in items if (it.get("title") or "").strip() and it.get("url") and it["source_id"] not in excluded
    ]
    sources = load_sources_yaml(args.sources_yaml) if args.sources_yaml else []
    names = {s["id"]: s.get("name", s["id"]) for s in sources}
    langs = {s["id"]: s.get("lang", "en") for s in sources}
    regions = {s["id"]: s.get("region", "intl") for s in sources}
    keywords_by_source = {s["id"]: list(s.get("keywords") or []) for s in sources}

    clusters = cluster_items(items)
    kept = [c for c in clusters if not is_noise(c) and not off_topic(c, keywords_by_source)]
    noise = len(clusters) - len(kept)
    history = load_history(args.history, args.history_days)
    fresh = [c for c in kept if not was_pushed(c, history)]
    dup = len(kept) - len(fresh)

    chosen = select(fresh, now, args.max_items, cn_items, args.per_source_cap, regions)
    stats = {
        "items": len(items),
        "clusters": len(clusters),
        "noise": noise,
        "dup": dup,
        "history_days": args.history_days,
        "available_cn": sum(cluster_region(c, regions) == "cn" for c in fresh),
        "available_intl": sum(cluster_region(c, regions) == "intl" for c in fresh),
        "target_cn": cn_items,
        "target_intl": args.max_items - cn_items,
        "selected_cn": sum(cluster_region(c, regions) == "cn" for c in chosen),
        "selected_intl": sum(cluster_region(c, regions) == "intl" for c in chosen),
    }
    write_atomic(
        args.out_md,
        build_markdown(
            chosen,
            names,
            langs,
            regions,
            now,
            stats,
            args.summary_chars,
            excerpt_chars=args.excerpt_chars,
            history=history,
            callback_days=args.callback_days,
        ),
    )
    payload = []
    for i, c in enumerate(chosen, 1):
        summary = one_line(c.rep.get("summary") or c.rep.get("content"), args.summary_chars)
        excerpt = sample_content_excerpt(c, summary=summary, limit=args.excerpt_chars)
        callback = find_history_callback(c, history, callback_days=args.callback_days, now=now) if history else None
        payload.append(
            {
                "rank": i,
                "title": c.rep["title"],
                "lang": c.rep.get("lang") or langs.get(c.rep["source_id"], "en"),
                "region": cluster_region(c, regions),
                "url": c.rep["url"],
                "score": score(c, now),
                "sources": c.sources,
                "titles": [it["title"] for it in c.items],
                "published_at": c.rep.get("published_at"),
                "summary": summary,
                "excerpt": excerpt,
                "history_callback": callback,
            }
        )
    write_atomic(args.out_json, json.dumps({"generated_at": now.isoformat(), "stats": stats, "items": payload}, ensure_ascii=False, indent=1))
    print(
        f"curated {len(chosen)} of {len(clusters)} clusters from {len(items)} items "
        f"(noise {noise}, already pushed {dup}, "
        f"cn {stats['selected_cn']}/{stats['target_cn']}, "
        f"intl {stats['selected_intl']}/{stats['target_intl']}) -> {args.out_md}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

