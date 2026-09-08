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

from curate_digest import Cluster, cluster_region, select  # noqa: E402
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
    def test_exact_half_and_interleaved(self) -> None:
        clusters = [
            *(make_cluster(f"cn-{i}", f"中国新闻{i}") for i in range(12)),
            *(make_cluster(f"intl-{i}", f"International story {i}") for i in range(12)),
        ]
        regions = {
            **{f"cn-{i}": "cn" for i in range(12)},
            **{f"intl-{i}": "intl" for i in range(12)},
        }
        chosen = select(
            clusters,
            datetime.now(timezone.utc),
            max_items=20,
            cn_items=10,
            per_source_cap=3,
            regions=regions,
        )
        actual = [cluster_region(c, regions) for c in chosen]
        self.assertEqual(actual, ["intl", "cn"] * 10)

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
