from __future__ import annotations

import asyncio
import logging
from typing import Any

import feedparser

from ..config import SourceConfig
from ..http import HttpClients
from .base import FetchResult, RawEntry, strip_html, struct_to_datetime

log = logging.getLogger(__name__)

# Bot gates answer these to plain HTTP clients (Vercel challenge mode -> 429, Cloudflare -> 403/503).
# A Chrome TLS fingerprint gets through the TLS-level ones, so retry once that way before giving up.
_IMPERSONATE_ON = {403, 429, 503}


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
    clients: HttpClients,
    etag: str | None,
    last_modified: str | None,
) -> FetchResult:
    headers: dict[str, str] = {}
    if etag:
        headers["If-None-Match"] = etag
    if last_modified:
        headers["If-Modified-Since"] = last_modified

    resp = await clients.for_source(source).get(source.url, headers=headers)  # type: ignore[arg-type]
    if resp.status_code == 304:
        return FetchResult([], etag=etag, last_modified=last_modified, not_modified=True)

    content = resp.content
    new_etag, new_last_modified = resp.headers.get("ETag"), resp.headers.get("Last-Modified")
    if resp.status_code in _IMPERSONATE_ON:
        page = await clients.fetch_impersonated(source.url, via_proxy=source.proxy)  # type: ignore[arg-type]
        if page.status_code == 200:
            log.info("%s: HTTP %s with plain client, ok with Chrome fingerprint", source.id, resp.status_code)
            content, new_etag, new_last_modified = page.content, None, None
        else:
            resp.raise_for_status()
    else:
        resp.raise_for_status()

    parsed = await asyncio.to_thread(feedparser.parse, content)
    if parsed.get("bozo") and not parsed.entries:
        raise ValueError(f"feed parse error: {parsed.get('bozo_exception')}")

    entries = [e for e in (_entry_from_feed(x, source) for x in parsed.entries) if e]
    return FetchResult(entries, etag=new_etag, last_modified=new_last_modified)
