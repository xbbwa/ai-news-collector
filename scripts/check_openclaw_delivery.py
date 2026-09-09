#!/usr/bin/env python3
"""Verify the 08:00 OpenClaw AI-news job by its actual delivery receipt, then retry.

Unlike the old LLM healthcheck, this never trusts daily-push-history.md: the push job writes
that file before final delivery, so a failed run can leave a false-success date behind.

Run from the server's crontab at 08:20 Asia/Shanghai:

  20 8 * * * python3 ~/ai-news-collector/scripts/check_openclaw_delivery.py
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    import fcntl
except ImportError:  # pragma: no cover - production is Linux; allows Windows unit tests
    fcntl = None  # type: ignore[assignment]

PUSH_JOB_ID = "1b09cdd9-25f9-45fc-9fed-ff98074f8eef"
OPERATOR = "user:ou_6b013033efa0b30f20cbbf41fbebb5da"
TZ = ZoneInfo("Asia/Shanghai")
OPENCLAW = str(Path.home() / ".npm-global/bin/openclaw")
ROOT = Path(__file__).resolve().parent.parent


def load_env() -> None:
    path = ROOT / ".env"
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def run(*args: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [OPENCLAW, *args],
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def latest_run(job_id: str) -> dict | None:
    proc = run("cron", "runs", "--id", job_id, "--limit", "5")
    if proc.returncode != 0:
        raise RuntimeError(f"cannot read cron runs: {(proc.stderr or proc.stdout).strip()}")
    data = json.loads(proc.stdout)
    entries = data.get("entries") or []
    return max(entries, key=lambda item: int(item.get("runAtMs") or 0), default=None)


def run_date(entry: dict | None) -> str | None:
    if not entry or not entry.get("runAtMs"):
        return None
    return datetime.fromtimestamp(int(entry["runAtMs"]) / 1000, TZ).date().isoformat()


def delivered(entry: dict | None, today: str) -> bool:
    return bool(
        entry
        and run_date(entry) == today
        and entry.get("status") == "ok"
        and entry.get("delivered") is True
        and entry.get("deliveryStatus") == "delivered"
    )


def summarize(entry: dict | None) -> str:
    if not entry:
        return "no run"
    return (
        f"date={run_date(entry)} status={entry.get('status')} "
        f"delivered={entry.get('delivered')} deliveryStatus={entry.get('deliveryStatus')} "
        f"error={str(entry.get('error') or entry.get('deliveryError') or '')[:160]}"
    )


def notify(text: str) -> None:
    proc = run(
        "message",
        "send",
        "--channel",
        "feishu",
        "--target",
        OPERATOR,
        "--message",
        text,
        timeout=120,
    )
    if proc.returncode != 0:
        print(f"operator notification failed: {(proc.stderr or proc.stdout).strip()}", file=sys.stderr)


def record_delivered_history() -> bool:
    """Persist only content that has an actual successful group delivery receipt."""
    curated = ROOT / "data/curated.json"
    history_dir = ROOT / "archive/digest"
    history = history_dir / "pushed-history.jsonl"
    if not curated.exists():
        print(f"cannot mark delivery: {curated} is missing", file=sys.stderr)
        return False
    history_dir.mkdir(parents=True, exist_ok=True)
    commands = [
        [
            sys.executable,
            str(ROOT / "scripts/mark_pushed.py"),
            "--curated",
            str(curated),
            "--history",
            str(history),
            "--keep-days",
            "0",
        ],
        [
            sys.executable,
            str(ROOT / "scripts/publish_archive.py"),
            "--dir",
            str(history_dir),
            "--pattern",
            "pushed-history.jsonl",
            "--remote-dir",
            "digest",
            "--repo",
            "xbbwa/ai-news-collector",
            "--branch",
            "data",
            "--state",
            str(ROOT / "data/publish_state_digest.json"),
        ],
    ]
    for command in commands:
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=180)
        if proc.stdout.strip():
            print(proc.stdout.strip())
        if proc.returncode != 0:
            print((proc.stderr or "history command failed").strip(), file=sys.stderr)
            return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--job-id", default=PUSH_JOB_ID)
    parser.add_argument("--wait-seconds", type=int, default=900)
    parser.add_argument("--poll-seconds", type=int, default=10)
    args = parser.parse_args()
    load_env()

    lock_path = Path.home() / ".openclaw/ai-news-delivery-check.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("w") as lock:
        if fcntl is not None:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                print("another delivery check is already running")
                return 0

        today = datetime.now(TZ).date().isoformat()
        before = latest_run(args.job_id)
        if delivered(before, today):
            if record_delivered_history():
                print(f"{today}: push receipt verified and recorded ({summarize(before)})")
                return 0
            notify("⚠️ Daily AI News 已送达群，但去重历史写回 GitHub 失败，请检查服务器日志。")
            return 1

        print(f"{today}: push missing/failed ({summarize(before)}); retrying")
        notify(f"⚠️ Daily AI News 08:00 群推未成功，08:20 正在自动补推。\n{summarize(before)}")

        previous_at = int((before or {}).get("runAtMs") or 0)
        proc = run("cron", "run", args.job_id, timeout=60)
        if proc.returncode != 0:
            error = (proc.stderr or proc.stdout).strip()
            notify(f"❌ Daily AI News 自动补推无法启动：{error[:300]}")
            print(error, file=sys.stderr)
            return 1

        deadline = time.monotonic() + args.wait_seconds
        latest = before
        while time.monotonic() < deadline:
            time.sleep(args.poll_seconds)
            latest = latest_run(args.job_id)
            if int((latest or {}).get("runAtMs") or 0) <= previous_at:
                continue
            # A new entry is only written after the retry finishes.
            break

        if delivered(latest, today):
            if not record_delivered_history():
                notify("⚠️ Daily AI News 已补推到群，但去重历史写回 GitHub 失败，请检查服务器日志。")
                return 1
            notify("✅ Daily AI News 已自动补推到群，真实投递回执为 delivered。")
            print(f"{today}: retry delivered and recorded ({summarize(latest)})")
            return 0

        notify(f"❌ Daily AI News 自动补推仍失败，请人工处理。\n{summarize(latest)}")
        print(f"{today}: retry failed ({summarize(latest)})", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
