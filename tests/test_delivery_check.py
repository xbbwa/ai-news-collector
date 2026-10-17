from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_openclaw_delivery import (  # noqa: E402
    TZ,
    backfill_delivered_summary,
    curated_fresh,
    delivered,
    run_date,
)


def entry(**overrides):
    item = {
        "runAtMs": int(datetime(2026, 9, 9, 8, 0, tzinfo=TZ).timestamp() * 1000),
        "status": "ok",
        "delivered": True,
        "deliveryStatus": "delivered",
    }
    item.update(overrides)
    return item


class DeliveryReceiptTests(unittest.TestCase):
    def test_valid_receipt(self) -> None:
        value = entry()
        self.assertEqual(run_date(value), "2026-09-09")
        self.assertTrue(delivered(value, "2026-09-09"))

    def test_history_style_success_without_receipt_is_rejected(self) -> None:
        self.assertFalse(delivered(entry(status="error", delivered=False), "2026-09-09"))
        self.assertFalse(delivered(entry(deliveryStatus="not-delivered"), "2026-09-09"))
        self.assertFalse(delivered(entry(delivered=None), "2026-09-09"))

    def test_yesterdays_success_is_rejected(self) -> None:
        value = entry(
            runAtMs=int(datetime(2026, 9, 8, 8, 0, tzinfo=TZ).timestamp() * 1000)
        )
        self.assertFalse(delivered(value, "2026-09-09"))

    def test_candidate_must_be_today_and_recent(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "curated.json"
            now = datetime(2026, 9, 9, 8, 20, tzinfo=TZ)
            path.write_text(
                json.dumps({"generated_at": "2026-09-08T23:30:00+00:00"}),
                encoding="utf-8",
            )
            self.assertTrue(curated_fresh(path, "2026-09-09", now=now)[0])

            path.write_text(
                json.dumps({"generated_at": "2026-09-08T05:30:00+00:00"}),
                encoding="utf-8",
            )
            self.assertFalse(curated_fresh(path, "2026-09-09", now=now)[0])

            self.assertFalse(
                curated_fresh(path, "2026-09-08", now=datetime(2026, 9, 10, tzinfo=timezone.utc))[0]
            )

    def test_backfill_delivered_summary_writes_enriched_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            curated_path = Path(temp) / "curated.json"
            out_path = Path(temp) / "pushed-latest.md"
            curated_path.write_text(
                json.dumps(
                    {
                        "generated_at": "2026-09-09T00:00:00+00:00",
                        "items": [
                            {"region": "intl", "url": "https://openai.com/gpt6"},
                            {"region": "cn", "url": "https://deepseek.com/v4"},
                        ],
                    }
                ),
                encoding="utf-8",
            )
            run_entry = entry(
                summary=(
                    "📰 Daily AI News · 2026-09-09（国外 1 条｜国内 1 条）\n\n"
                    "国外：\n"
                    "1. 【OpenAI 发布 GPT-6】\n"
                    "   推理性能翻倍｜来源：OpenAI（共 1 家）\n\n"
                    "国内：\n"
                    "1. 【DeepSeek 发布 V4】\n"
                    "   长上下文成本减半｜来源：DeepSeek（共 1 家）"
                )
            )
            written = backfill_delivered_summary(run_entry, curated_path, out_path=out_path)
            self.assertEqual(written, out_path)
            content = out_path.read_text(encoding="utf-8")
            self.assertIn("   🔗 https://openai.com/gpt6", content)
            self.assertIn("   🔗 https://deepseek.com/v4", content)


if __name__ == "__main__":
    unittest.main()

