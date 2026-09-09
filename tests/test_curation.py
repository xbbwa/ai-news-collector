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
    cluster_region,
    entity_tokens,
    load_history,
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
