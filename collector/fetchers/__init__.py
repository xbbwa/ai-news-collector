from __future__ import annotations

from ..config import SourceConfig
from ..http import HttpClients
from .base import FetchResult, RawEntry
from .hackernews import fetch_hackernews
from .huggingface import fetch_huggingface
from .reddit import fetch_reddit
from .rss import fetch_rss

__all__ = ["FetchResult", "RawEntry", "fetch"]


async def fetch(
    source: SourceConfig,
    clients: HttpClients,
    etag: str | None = None,
    last_modified: str | None = None,
) -> FetchResult:
    if source.type == "rss":
        return await fetch_rss(source, clients, etag, last_modified)
    if source.type == "hackernews":
        return await fetch_hackernews(source, clients.for_source(source))
    if source.type == "reddit":
        return await fetch_reddit(source, clients.for_source(source))
    if source.type == "huggingface":
        return await fetch_huggingface(source, clients.for_source(source))
    raise ValueError(f"unknown source type {source.type!r} for {source.id}")
