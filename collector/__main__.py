from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
from dataclasses import replace
from pathlib import Path

from sqlalchemy import select

from .config import Settings, for_runner, load_sources
from .db import init_db, make_engine, make_session_factory
from .http import HttpClients
from .models import Item
from .pipeline import Collector
from .scheduler import run_forever


def _setup_logging(level: str) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        stream=sys.stdout,
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("trafilatura").setLevel(logging.ERROR)


def _build(settings: Settings) -> tuple[Collector, HttpClients]:
    engine = make_engine(settings.database_url)
    init_db(engine)
    clients = HttpClients(settings)
    return Collector(settings, clients, make_session_factory(engine)), clients


async def cmd_run(settings: Settings) -> None:
    sources = for_runner(load_sources(settings), settings.runner)
    collector, clients = _build(settings)
    try:
        await run_forever(collector, sources)
    finally:
        await clients.aclose()


async def cmd_once(settings: Settings, only: list[str] | None) -> None:
    sources = [s for s in for_runner(load_sources(settings), settings.runner) if s.enabled]
    if only:
        wanted = set(only)
        sources = [s for s in sources if s.id in wanted]
        missing = wanted - {s.id for s in sources}
        if missing:
            raise SystemExit(f"unknown/disabled source ids: {sorted(missing)}")

    collector, clients = _build(settings)
    log = logging.getLogger("once")

    async def one(src):  # noqa: ANN001
        try:
            n = await collector.run_source(src)
            log.info("%-28s +%d", src.id, n)
            return n
        except Exception as exc:
            log.warning("%-28s FAILED %s: %s", src.id, type(exc).__name__, exc)
            return 0

    try:
        results = await asyncio.gather(*(one(s) for s in sources))
        log.info("done: %d sources, %d new items", len(sources), sum(results))
    finally:
        await clients.aclose()


async def cmd_retry_extract(settings: Settings, limit: int) -> None:
    sources = {s.id: s for s in load_sources(settings)}
    collector, clients = _build(settings)
    try:
        n = await collector.retry_failed_extractions(sources, limit)
        logging.getLogger("retry").info("re-attempted extraction for %d items", n)
    finally:
        await clients.aclose()


def cmd_sources(settings: Settings) -> None:
    for s in for_runner(load_sources(settings), settings.runner):
        flag = " " if s.enabled else "x"
        proxy = "proxy" if s.proxy else "     "
        print(f"[{flag}] T{s.tier} {s.type:<11} {s.runner:<6} {proxy} {s.interval:>5}s  {s.id:<28} {s.name}")


def cmd_export(settings: Settings, since_id: int, out: Path | None) -> None:
    engine = make_engine(settings.database_url)
    init_db(engine)
    fh = open(out, "w", encoding="utf-8") if out else sys.stdout
    try:
        with make_session_factory(engine)() as s:
            rows = s.scalars(select(Item).where(Item.id > since_id).order_by(Item.id)).all()
            for r in rows:
                fh.write(json.dumps(r.to_dict(), ensure_ascii=False) + "\n")
        if out:
            print(f"exported {len(rows)} items to {out}", file=sys.stderr)
    finally:
        if out:
            fh.close()


def cmd_api(settings: Settings, host: str | None, port: int | None) -> None:
    import uvicorn

    uvicorn.run(
        "collector.api:app",
        host=host or settings.api_host,
        port=port or settings.api_port,
        log_level=settings.log_level.lower(),
    )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="collector", description="AI news collector")
    parser.add_argument(
        "--runner",
        help="only sources with this `runner` (github|server); default $COLLECTOR_RUNNER, unset = all",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("run", help="run the scheduler forever")

    p_once = sub.add_parser("once", help="poll all (or selected) sources once and exit")
    p_once.add_argument("--source", "-s", action="append", help="source id (repeatable)")

    p_retry = sub.add_parser("retry-extract", help="retry failed/pending full-text extraction")
    p_retry.add_argument("--limit", type=int, default=100)

    sub.add_parser("sources", help="list configured sources")

    p_export = sub.add_parser("export", help="dump items as JSONL")
    p_export.add_argument("--since-id", type=int, default=0)
    p_export.add_argument("--out", type=Path)

    p_api = sub.add_parser("api", help="serve the HTTP API")
    p_api.add_argument("--host")
    p_api.add_argument("--port", type=int)

    args = parser.parse_args(argv)
    settings = Settings.from_env()
    if args.runner:
        settings = replace(settings, runner=args.runner)
    _setup_logging(settings.log_level)

    if args.cmd == "run":
        asyncio.run(cmd_run(settings))
    elif args.cmd == "once":
        asyncio.run(cmd_once(settings, args.source))
    elif args.cmd == "retry-extract":
        asyncio.run(cmd_retry_extract(settings, args.limit))
    elif args.cmd == "sources":
        cmd_sources(settings)
    elif args.cmd == "export":
        cmd_export(settings, args.since_id, args.out)
    elif args.cmd == "api":
        cmd_api(settings, args.host, args.port)


if __name__ == "__main__":
    main()
