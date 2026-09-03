from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")


def strip_html(text: str | None) -> str | None:
    if not text:
        return None
    import html

    cleaned = _WS_RE.sub(" ", _TAG_RE.sub(" ", html.unescape(text))).strip()
    return cleaned or None


@dataclass
class RawEntry:
    external_id: str
    url: str
    title: str
    summary: str | None = None
    author: str | None = None
    published_at: datetime | None = None
    lang: str | None = None
    skip_fulltext: bool = False  # e.g. Reddit self-posts: the URL has no article to extract
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class FetchResult:
    entries: list[RawEntry]
    etag: str | None = None
    last_modified: str | None = None
    not_modified: bool = False
