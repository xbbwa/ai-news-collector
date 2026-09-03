from __future__ import annotations

import asyncio
import json
from datetime import datetime, timezone
from typing import Any

import trafilatura

from .http import HttpClients

MAX_HTML_BYTES = 5 * 1024 * 1024


class ExtractError(Exception):
    pass


def _extract_sync(html: str, url: str) -> dict[str, Any] | None:
    out = trafilatura.extract(
        html,
        url=url,
        output_format="json",
        with_metadata=True,
        include_comments=False,
        include_tables=True,
        include_images=False,
        favor_precision=True,
    )
    return json.loads(out) if out else None


def _parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


async def extract_article(url: str, http: HttpClients, use_proxy: bool) -> dict[str, Any]:
    """Download the page and return trafilatura's structured extraction.

    Keys used downstream: text, title, author, date, image, language, hostname, excerpt.
    Raises ExtractError on HTTP errors, non-HTML responses, or empty extraction.
    """
    page = await http.fetch_page(url, use_proxy)
    if page.status_code >= 400:
        raise ExtractError(f"HTTP {page.status_code} (via {page.via})")

    ctype = page.content_type.split(";")[0].strip().lower()
    if ctype and "html" not in ctype and "xml" not in ctype:
        raise ExtractError(f"unsupported content-type: {ctype}")
    if len(page.content) > MAX_HTML_BYTES:
        raise ExtractError(f"page too large: {len(page.content)} bytes")

    result = await asyncio.to_thread(_extract_sync, page.text, page.url)
    if not result or not (result.get("text") or "").strip():
        raise ExtractError(f"no main content extracted (via {page.via})")

    result["final_url"] = page.url
    result["fetched_via"] = page.via
    result["date_parsed"] = _parse_date(result.get("date"))
    return result
