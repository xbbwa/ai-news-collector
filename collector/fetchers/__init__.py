from __future__ import annotations

import httpx

from ..config import Settings, SourceConfig
from .base import FetchResult, RawEntry
from .hackernews import fetch_hackernews
from .reddit import fetch_reddit
from .rss import fetch_rss

__all__ = ["FetchResult", "RawEntry", "fetch"]


async def fetch(
    source: SourceConfig,
    client: httpx.AsyncClient,
    settings: Settings,
    etag: str | None = None,
    last_modified: str | None = None,
) -> FetchResult:
    if source.type == "rss":
        return await fetch_rss(source, client, etag, last_modified)
    if source.type == "hackernews":
        return await fetch_hackernews(source, client)
    if source.type == "reddit":
        return await fetch_reddit(source, client, settings)
    raise ValueError(f"unknown source type {source.type!r} for {source.id}")
