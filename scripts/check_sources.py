"""Fetch every enabled source once, without touching the database, and print a health table.

usage: python scripts/check_sources.py [source_id ...]

Columns: TOTAL = entries the fetcher returned, KEPT = entries left after the keyword and
max_age_days filters (what would actually be stored), NEWEST = age of the most recent entry.
Sources served by RSSHub are skipped when RSSHUB_URL does not answer.
"""
from __future__ import annotations

import asyncio
import sys
import time
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402

from collector.config import Settings, SourceConfig, for_runner, load_sources  # noqa: E402
from collector.fetchers import FetchResult, fetch  # noqa: E402
from collector.http import HttpClients  # noqa: E402
from collector.models import to_utc_naive, utcnow  # noqa: E402
from collector.pipeline import is_fresh, matches_keywords  # noqa: E402


async def rsshub_reachable(settings: Settings) -> bool:
    try:
        async with httpx.AsyncClient(timeout=5) as c:
            return (await c.get(settings.rsshub_url + "/")).status_code < 500
    except httpx.HTTPError:
        return False


async def check_one(
    clients: HttpClients, sem: asyncio.Semaphore, source: SourceConfig
) -> tuple[SourceConfig, FetchResult | None, str | None, float]:
    async with sem:
        t0 = time.monotonic()
        try:
            result = await fetch(source, clients.for_source(source))
        except Exception as exc:  # report, don't abort the run
            return source, None, f"{type(exc).__name__}: {exc}"[:110], time.monotonic() - t0
        return source, result, None, time.monotonic() - t0


def describe(source: SourceConfig, result: FetchResult) -> tuple[int, int, str]:
    entries = result.entries
    if source.time_offset_hours:
        for e in entries:
            if e.published_at is not None:
                e.published_at += timedelta(hours=source.time_offset_hours)
    kept = [
        e
        for e in entries
        if e.url and matches_keywords(e, source.keywords) and is_fresh(e, source.max_age_days)
    ]
    dates = [to_utc_naive(e.published_at) for e in entries if e.published_at]
    if dates:
        hours = (utcnow() - max(d for d in dates if d)).total_seconds() / 3600
        newest = f"{hours:.0f}h ago" if hours >= 0 else f"{-hours:.0f}h AHEAD"
    else:
        newest = "no dates"
    return len(entries), len(kept), newest


async def main(only: list[str]) -> int:
    settings = Settings.from_env()
    sources = [s for s in for_runner(load_sources(settings), settings.runner) if s.enabled]
    if settings.runner:
        print(f"COLLECTOR_RUNNER={settings.runner}: checking only that side's {len(sources)} sources\n")
    if only:
        sources = [s for s in sources if s.id in set(only)]
    rsshub_ok = await rsshub_reachable(settings)
    if not rsshub_ok:
        print(f"RSSHub at {settings.rsshub_url} is not reachable; skipping ${{RSSHUB_URL}} sources.\n")

    clients = HttpClients(settings)
    sem = asyncio.Semaphore(8)
    try:
        tasks = [
            check_one(clients, sem, s)
            for s in sources
            if rsshub_ok or not (s.url or "").startswith(settings.rsshub_url)
        ]
        results = await asyncio.gather(*tasks)
    finally:
        await clients.aclose()

    print(f"{'STATUS':<6} {'ID':<26} {'TYPE':<11} {'TOTAL':>5} {'KEPT':>5} {'NEWEST':>10} {'TIME':>6}  NOTE")
    ok = failed = 0
    for source, result, error, elapsed in sorted(results, key=lambda r: (r[2] is None, r[0].id)):
        if result is None:
            failed += 1
            print(f"{'FAIL':<6} {source.id:<26} {source.type:<11} {'-':>5} {'-':>5} {'-':>10} {elapsed:5.1f}s  {error}")
            continue
        total, kept, newest = describe(source, result)
        note = ""
        if total == 0:
            note = "no entries"
        elif kept == 0:
            note = "nothing passes keyword/age filter"
        ok += 1
        print(f"{'ok':<6} {source.id:<26} {source.type:<11} {total:>5} {kept:>5} {newest:>10} {elapsed:5.1f}s  {note}")

    skipped = len(sources) - len(results)
    print(f"\n{ok} ok, {failed} failed, {skipped} skipped (RSSHub down)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main(sys.argv[1:])))
