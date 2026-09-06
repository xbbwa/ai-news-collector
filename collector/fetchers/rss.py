from __future__ import annotations

import asyncio
from typing import Any

import feedparser
import httpx

from ..config import SourceConfig
from .base import FetchResult, RawEntry, strip_html, struct_to_datetime


def _entry_from_feed(entry: Any, source: SourceConfig) -> RawEntry | None:
    link = (entry.get("link") or "").strip()
    if not link:
        return None

    title = strip_html(entry.get("title")) or "(untitled)"

    summary_html: str | None = None
    contents = entry.get("content") or []
    if contents and contents[0].get("value"):
        summary_html = contents[0]["value"]
    elif entry.get("summary"):
        summary_html = entry["summary"]

    published = struct_to_datetime(entry.get("published_parsed")) or struct_to_datetime(
        entry.get("updated_parsed")
    )

    tags = [t.get("term") for t in entry.get("tags") or [] if t.get("term")]
    enclosures = [e.get("href") for e in entry.get("enclosures") or [] if e.get("href")]
    media = [m.get("url") for m in entry.get("media_content") or [] if m.get("url")]

    return RawEntry(
        external_id=(entry.get("id") or link)[:1024],
        url=link,
        title=title,
        summary=strip_html(summary_html),
        author=entry.get("author") or None,
        published_at=published,
        lang=source.lang,
        raw={
            "summary_html": summary_html,
            "published_raw": entry.get("published") or entry.get("updated"),
            "tags": tags,
            "enclosures": enclosures,
            "media": media,
            "comments": entry.get("comments"),
        },
    )


async def fetch_rss(
    source: SourceConfig,
    client: httpx.AsyncClient,
    etag: str | None,
    last_modified: str | None,
) -> FetchResult:
    headers: dict[str, str] = {}
    if etag:
        headers["If-None-Match"] = etag
    if last_modified:
        headers["If-Modified-Since"] = last_modified

    resp = await client.get(source.url, headers=headers)  # type: ignore[arg-type]
    if resp.status_code == 304:
        return FetchResult([], etag=etag, last_modified=last_modified, not_modified=True)
    resp.raise_for_status()

    parsed = await asyncio.to_thread(feedparser.parse, resp.content)
    if parsed.get("bozo") and not parsed.entries:
        raise ValueError(f"feed parse error: {parsed.get('bozo_exception')}")

    entries = [e for e in (_entry_from_feed(x, source) for x in parsed.entries) if e]
    return FetchResult(
        entries,
        etag=resp.headers.get("ETag"),
        last_modified=resp.headers.get("Last-Modified"),
    )
