from __future__ import annotations

import sys
import unittest
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_openclaw_delivery import TZ, delivered, run_date  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
