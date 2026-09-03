from __future__ import annotations

import asyncio
import logging
import random

from .config import SourceConfig
from .pipeline import Collector

log = logging.getLogger(__name__)

MAX_BACKOFF_MULTIPLIER = 16


async def run_forever(collector: Collector, sources: list[SourceConfig]) -> None:
    enabled = [s for s in sources if s.enabled]
    log.info("scheduling %d sources", len(enabled))
    tasks = [asyncio.create_task(_source_loop(collector, s), name=s.id) for s in enabled]
    await asyncio.gather(*tasks)


async def _source_loop(collector: Collector, source: SourceConfig) -> None:
    # Stagger start-up so hundreds of sources don't all fire in the same second.
    await asyncio.sleep(random.uniform(0, min(30, source.interval)))
    failures = 0
    while True:
        try:
            added = await collector.run_source(source)
            failures = 0
            if added:
                log.info("%s: +%d", source.id, added)
            else:
                log.debug("%s: no new items", source.id)
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            failures += 1
            log.warning("%s: fetch failed x%d: %s: %s", source.id, failures, type(exc).__name__, exc)

        multiplier = min(2**failures, MAX_BACKOFF_MULTIPLIER) if failures else 1
        delay = source.interval * multiplier
        await asyncio.sleep(delay + random.uniform(0, delay * 0.1))
