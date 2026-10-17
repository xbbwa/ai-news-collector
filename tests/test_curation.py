from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from curate_digest import (  # noqa: E402
    Cluster,
    action_tokens,
    backfill_links,
    build_markdown,
    cluster_region,
    entity_tokens,
    find_history_callback,
    load_history,
    sample_content_excerpt,
    same_event,
    select,
    tokens,
    was_pushed,
)
from daily_digest import fetch_items_db  # noqa: E402


def make_cluster(source: str, title: str) -> Cluster:
    return Cluster(
        {
            "source_id": source,
            "source_tier": 2,
            "title": title,
            "url": f"https://example.com/{source}/{title}",
            "published_at": datetime.now(timezone.utc).isoformat(),
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "raw": {},
        }
    )


class RegionQuotaTests(unittest.TestCase):
    def test_exact_70_30_with_international_first(self) -> None:
        clusters = [
            *(make_cluster(f"cn-{i}", f"中国新闻{i}") for i in range(16)),
            *(make_cluster(f"intl-{i}", f"International story {i}") for i in range(16)),
        ]
        regions = {
            **{f"cn-{i}": "cn" for i in range(16)},
            **{f"intl-{i}": "intl" for i in range(16)},
        }
        chosen = select(
            clusters,
            datetime.now(timezone.utc),
            max_items=20,
            cn_items=6,
            per_source_cap=3,
            regions=regions,
        )
        actual = [cluster_region(c, regions) for c in chosen]
        self.assertEqual(actual, ["intl"] * 14 + ["cn"] * 6)

    def test_short_side_is_not_filled_from_other_region(self) -> None:
        clusters = [
            *(make_cluster(f"cn-{i}", f"中国新闻{i}") for i in range(3)),
            *(make_cluster(f"intl-{i}", f"International story {i}") for i in range(12)),
        ]
        regions = {
            **{f"cn-{i}": "cn" for i in range(3)},
            **{f"intl-{i}": "intl" for i in range(12)},
        }
        chosen = select(
            clusters,
            datetime.now(timezone.utc),
            max_items=10,
            cn_items=5,
            per_source_cap=3,
            regions=regions,
        )
        actual = [cluster_region(c, regions) for c in chosen]
        self.assertEqual(actual.count("cn"), 3)
        self.assertEqual(actual.count("intl"), 5)
        self.assertEqual(len(actual), 8)

    def test_academic_family_is_capped_across_source_ids(self) -> None:
        clusters = [
            *(make_cluster(f"arxiv-cs-{i}", f"Paper {i}") for i in range(12)),
            *(make_cluster(f"media-{i}", f"Industry story {i}") for i in range(14)),
        ]
        regions = {c.rep["source_id"]: "intl" for c in clusters}
        chosen = select(
            clusters,
            datetime.now(timezone.utc),
            max_items=14,
            cn_items=0,
            per_source_cap=3,
            regions=regions,
        )
        papers = [c for c in chosen if c.rep["source_id"].startswith("arxiv-")]
        self.assertEqual(len(chosen), 14)
        self.assertEqual(len(papers), 4)


class CrossDayDedupeTests(unittest.TestCase):
    def test_cross_language_company_funding_is_same_event(self) -> None:
        english = "Mistral raises €3B in Samsung-led funding round"
        chinese = "Mistral 完成 30 亿欧元融资，三星领投"
        self.assertTrue(
            same_event(
                tokens(english),
                tokens(chinese),
                entity_tokens(english),
                entity_tokens(chinese),
                action_tokens(english),
                action_tokens(chinese),
            )
        )

    def test_cross_language_camelcase_product_is_same_event(self) -> None:
        english = "AlphaGenome Atlas: A predictive map of every possible DNA change"
        chinese = "谷歌 DeepMind 推出 AlphaGenome Atlas，覆盖人类基因组变异预测"
        self.assertTrue(
            same_event(
                tokens(english),
                tokens(chinese),
                entity_tokens(english),
                entity_tokens(chinese),
                action_tokens(english),
                action_tokens(chinese),
            )
        )

    def test_same_product_announcement_titles_merge(self) -> None:
        first = "Introducing Muse: The World's First Personal AI Agent Built for Everyone"
        second = "Meta Announces Muse AI Agent for Personal Tasks and Organization"
        self.assertTrue(
            same_event(
                tokens(first),
                tokens(second),
                entity_tokens(first),
                entity_tokens(second),
                action_tokens(first),
                action_tokens(second),
            )
        )

    def test_exact_url_is_permanently_deduped(self) -> None:
        cluster = make_cluster("intl-1", "A completely rewritten title")
        cluster.items[0]["url"] = "https://example.com/same"
        history = [
            {
                "url": "https://example.com/same",
                "tokens": frozenset(),
                "entities": frozenset(),
                "actions": frozenset(),
            }
        ]
        self.assertTrue(was_pushed(cluster, history))

    def test_history_days_zero_loads_old_entries(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "history.jsonl"
            path.write_text(
                json.dumps(
                    {
                        "pushed_on": "2020-01-01",
                        "url": "https://example.com/old",
                        "titles": ["Old story"],
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            self.assertEqual(len(load_history(path, days=0)), 1)
            self.assertEqual(len(load_history(path, days=1)), 0)


class FulltextHeadTailSamplingTests(unittest.TestCase):
    def test_skips_summary_overlap_and_samples_head_plus_tail(self) -> None:
        cluster = make_cluster("anthropic-eng", "Contextual Retrieval for RAG Systems")
        summary = "Anthropic introduces Contextual Retrieval to improve RAG chunk accuracy across enterprise datasets."
        cluster.items[0]["summary"] = summary
        cluster.items[0]["content"] = "\n\n".join(
            [
                "Anthropic introduces Contextual Retrieval to improve RAG chunk accuracy across enterprise datasets.",
                "Traditional RAG pipelines split documents into fixed-size chunks, losing crucial document-level context such as entity names and fiscal quarters.",
                "We evaluated the approach across codebases, legal contracts, scientific papers, and customer support logs with multiple embedding models.",
                "Combining Contextual Embeddings with Contextual BM25 reduced top-20 retrieval failure rates by 67% while keeping p95 latency under 120ms.",
                "Subscribe to our newsletter for more updates.",
            ]
        )
        excerpt = sample_content_excerpt(cluster, summary=summary, limit=320)
        self.assertIn("Traditional RAG pipelines split documents", excerpt)
        self.assertIn("67%", excerpt)
        self.assertIn(" … ", excerpt)
        self.assertNotIn("Subscribe to our newsletter", excerpt)

    def test_falls_back_to_secondary_item_content_when_rep_lacks_fulltext(self) -> None:
        cluster = make_cluster("ft-tech", "DeepMind unveils new chip architecture")
        cluster.items[0]["summary"] = "Short paywalled teaser from Financial Times."
        cluster.items[0]["content"] = None
        cluster.add(
            {
                "source_id": "ars-technica",
                "source_tier": 2,
                "title": "DeepMind unveils new chip architecture for sparse models",
                "url": "https://arstechnica.com/chip",
                "summary": "Short teaser",
                "content": (
                    "First paragraph explaining how sparse mixture-of-experts routing bottlenecks memory bandwidth on current H100 clusters.\n\n"
                    "Middle details about optical interconnect topology and compiler scheduling passes.\n\n"
                    "Final benchmark paragraph showing 3.4x throughput per watt on 1T-parameter inference workloads."
                ),
            }
        )
        excerpt = sample_content_excerpt(cluster, summary="Short paywalled teaser from Financial Times.", limit=260)
        self.assertIn("sparse mixture-of-experts", excerpt)
        self.assertIn("3.4x throughput", excerpt)


class HistoryCallbackTests(unittest.TestCase):
    def test_matches_followup_story_on_specific_entity_without_duplicate_event(self) -> None:
        now = datetime(2026, 9, 12, 8, 0, tzinfo=timezone.utc)
        history = [
            {
                "pushed_on": "2026-09-07",
                "title": "OpenAI launches GPT-6 Astra",
                "titles": ["OpenAI launches GPT-6 Astra"],
                "url": "https://example.com/gpt6-launch",
                "tokens": tokens("OpenAI launches GPT-6 Astra"),
                "entities": entity_tokens("OpenAI launches GPT-6 Astra"),
                "actions": action_tokens("OpenAI launches GPT-6 Astra"),
            }
        ]
        followup = make_cluster("lmsys", "GPT-6 Tops Blind Coding Arena Benchmark by 90 Elo")
        self.assertFalse(was_pushed(followup, history))
        cb = find_history_callback(followup, history, callback_days=30, now=now)
        self.assertIsNotNone(cb)
        assert cb is not None
        self.assertEqual(cb["pushed_on"], "2026-09-07")
        self.assertIn("gpt-6", cb["entities"])

    def test_matches_version_stem_progression(self) -> None:
        now = datetime(2026, 9, 12, 8, 0, tzinfo=timezone.utc)
        history = [
            {
                "pushed_on": "2026-09-01",
                "title": "Alibaba open-sources Qwen2.5-Coder technical report",
                "titles": ["Alibaba open-sources Qwen2.5-Coder technical report"],
                "url": "https://example.com/qwen25",
                "tokens": tokens("Alibaba open-sources Qwen2.5-Coder technical report"),
                "entities": entity_tokens("Alibaba open-sources Qwen2.5-Coder technical report"),
                "actions": action_tokens("Alibaba open-sources Qwen2.5-Coder technical report"),
            }
        ]
        followup = make_cluster("hf-models", "Qwen3-Coder weights uploaded to Hugging Face Hub")
        cb = find_history_callback(followup, history, callback_days=30, now=now)
        self.assertIsNotNone(cb)
        assert cb is not None
        self.assertIn("qwen", cb["entities"])

    def test_ignores_unrelated_giant_corp_coincidence(self) -> None:
        now = datetime(2026, 9, 12, 8, 0, tzinfo=timezone.utc)
        history = [
            {
                "pushed_on": "2026-09-05",
                "title": "Google signs clean geothermal power contract in Nevada",
                "titles": ["Google signs clean geothermal power contract in Nevada"],
                "url": "https://example.com/google-power",
                "tokens": tokens("Google signs clean geothermal power contract in Nevada"),
                "entities": entity_tokens("Google signs clean geothermal power contract in Nevada"),
                "actions": action_tokens("Google signs clean geothermal power contract in Nevada"),
            }
        ]
        unrelated = make_cluster("verge", "Google updates Workspace sidebar icons for enterprise users")
        cb = find_history_callback(unrelated, history, callback_days=30, now=now)
        self.assertIsNone(cb)


class LinkBackfillTests(unittest.TestCase):
    def test_backfills_links_by_region_and_index_idempotently(self) -> None:
        llm_text = (
            "📰 Daily AI News · 2026-10-18（国外 2 条｜国内 1 条）\n\n"
            "国外：\n"
            "1. 【NVIDIA 宣布收购 Hugging Face】\n"
            "   承诺保持平台开放｜来源：NVIDIA 博客（共 3 家）\n\n"
            "2. 【Anthropic 推出上下文检索】\n"
            "   检索失败率降低 67%｜来源：Anthropic（共 1 家）\n\n"
            "国内：\n"
            "1. 【通义千问开源 Qwen3】\n"
            "   推理吞吐提升 2 倍｜来源：量子位（共 2 家）"
        )
        curated = {
            "items": [
                {"region": "intl", "url": "https://blogs.nvidia.com/hf"},
                {"region": "intl", "url": "https://anthropic.com/rag"},
                {"region": "cn", "url": "https://qwen.ai/qwen3"},
            ]
        }
        enriched = backfill_links(llm_text, curated, style="line")
        self.assertIn("   🔗 https://blogs.nvidia.com/hf", enriched)
        self.assertIn("   🔗 https://anthropic.com/rag", enriched)
        self.assertIn("   🔗 https://qwen.ai/qwen3", enriched)
        # Running twice is idempotent
        self.assertEqual(backfill_links(enriched, curated, style="line"), enriched)

    def test_backfills_from_curated_md_with_inline_style(self) -> None:
        now = datetime(2026, 10, 18, 0, 0, tzinfo=timezone.utc)
        c_intl = make_cluster("intl-1", "Intl Story")
        c_cn = make_cluster("cn-1", "CN Story")
        md = build_markdown(
            [c_intl, c_cn],
            names={"intl-1": "Intl", "cn-1": "CN"},
            langs={"intl-1": "en", "cn-1": "zh"},
            regions={"intl-1": "intl", "cn-1": "cn"},
            now=now,
            stats={
                "history_days": 0,
                "selected_intl": 1,
                "selected_cn": 1,
                "items": 2,
                "clusters": 2,
                "noise": 0,
                "dup": 0,
                "target_intl": 1,
                "target_cn": 1,
            },
            summary_chars=220,
        )
        llm_text = (
            "国外：\n"
            "1. 【国际标题】\n"
            "   国际摘要｜来源：Intl（共 1 家）\n\n"
            "国内：\n"
            "1. 【国内标题】\n"
            "   国内摘要｜来源：CN（共 1 家）"
        )
        enriched = backfill_links(llm_text, md, style="inline")
        self.assertIn(f"｜🔗 {c_intl.rep['url']}", enriched)
        self.assertIn(f"｜🔗 {c_cn.rep['url']}", enriched)


class DatabaseLoaderTests(unittest.TestCase):
    def test_db_loader_keeps_lang_and_raw_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "collector.db"
            conn = sqlite3.connect(path)
            conn.execute(
                """
                create table items (
                    id integer primary key,
                    source_id text,
                    source_tier integer,
                    url text,
                    title text,
                    author text,
                    lang text,
                    summary text,
                    content text,
                    raw text,
                    published_at text,
                    fetched_at text
                )
                """
            )
            now = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(sep=" ")
            conn.execute(
                "insert into items values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    1,
                    "hackernews-ai",
                    3,
                    "https://example.com/story",
                    "Story",
                    None,
                    "en",
                    None,
                    None,
                    json.dumps({"points": 123}),
                    now,
                    now,
                ),
            )
            conn.commit()
            conn.close()

            rows = fetch_items_db(path, datetime.now(timezone.utc) - timedelta(hours=1))
            self.assertEqual(rows[0]["lang"], "en")
            self.assertEqual(rows[0]["raw"]["points"], 123)


if __name__ == "__main__":
    unittest.main()

