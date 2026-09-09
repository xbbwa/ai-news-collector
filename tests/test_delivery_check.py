from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_openclaw_delivery import TZ, curated_fresh, delivered, run_date  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
