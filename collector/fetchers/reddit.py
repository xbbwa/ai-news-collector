from __future__ import annotations

import asyncio
import html
import re
import time

import feedparser
import httpx

from ..config import SourceConfig
from .base import FetchResult, RawEntry, strip_html, struct_to_datetime

# Reddit's OAuth API and the ".json" listings both require an account now, but the
# Atom feed of any listing is still served anonymously. Its entry body is a small
# HTML blob whose "[link]" anchor is the submitted URL (for self-posts it points back
# at the permalink) and whose <div class="md"> holds the self-text.
#
# Use the plain httpx client only: a Chrome TLS fingerprint without browser cookies
# makes www.reddit.com answer 403 with its app shell, so the impersonation fallback
# in HttpClients.fetch_page hurts here rather than helps.
FEED_URL = "https://www.reddit.com/r/{subreddit}/{listing}/.rss"

_LINK_RE = re.compile(r'<a href="([^"]+)">\[link\]</a>')
_SELFTEXT_RE = re.compile(r'<div class="md">(.*?)</div>\s*<!-- SC_ON -->', re.DOTALL)


class _Throttle:
    """Anonymous clients get one request per minute per IP (x-ratelimit-remaining hits 0
    after a single fetch; the window is aligned to wall-clock minutes), so every reddit
    source in the process takes turns and leaves a full window between requests."""

    def __init__(self, gap: float) -> None:
        self.gap = gap
        self.lock = asyncio.Lock()
        self.next_at = 0.0

    async def __aenter__(self) -> None:
        await self.lock.acquire()
        delay = self.next_at - time.monotonic()
        if delay > 0:
            await asyncio.sleep(delay)

    async def __aexit__(self, *exc: object) -> None:
        self.next_at = time.monotonic() + self.gap
        self.lock.release()


_throttle = _Throttle(gap=61.0)


async def fetch_reddit(source: SourceConfig, client: httpx.AsyncClient) -> FetchResult:
    # "subreddit" may be a multireddit ("MachineLearning+LocalLLaMA+..."): one request covers
    # them all, which matters with a one-request-per-minute budget.
    subreddit: str = source.params["subreddit"]
    listing: str = source.params.get("listing", "new")
    limit: int = int(source.params.get("limit", 50))

    url = FEED_URL.format(subreddit=subreddit, listing=listing)
    async with _throttle:
        resp = await client.get(url, params={"limit": limit})
    resp.raise_for_status()

    parsed = await asyncio.to_thread(feedparser.parse, resp.content)
    if parsed.get("bozo") and not parsed.entries:
        raise ValueError(f"feed parse error: {parsed.get('bozo_exception')}")

    entries: list[RawEntry] = []
    for entry in parsed.entries:
        permalink = (entry.get("link") or "").strip()
        if not permalink:
            continue

        contents = entry.get("content") or []
        body: str = (contents[0].get("value") if contents else None) or entry.get("summary") or ""
        link_match = _LINK_RE.search(body)
        target = html.unescape(link_match.group(1)) if link_match else permalink
        is_self = target.rstrip("/") == permalink.rstrip("/")
        selftext = _SELFTEXT_RE.search(body)
        thumbnails = entry.get("media_thumbnail") or []
        # Atom <category term="LocalLLaMA"> names the post's own subreddit.
        tags = [t.get("term") for t in entry.get("tags") or [] if t.get("term")]

        entries.append(
            RawEntry(
                # Atom <id> is the post fullname ("t3_xxx"), same value the JSON API exposed as "name".
                external_id=entry.get("id") or permalink,
                url=permalink if is_self else target,
                title=strip_html(entry.get("title")) or "(untitled)",
                summary=strip_html(selftext.group(1)) if selftext else None,
                author=(entry.get("author") or "").strip().removeprefix("/u/") or None,
                published_at=struct_to_datetime(entry.get("published_parsed"))
                or struct_to_datetime(entry.get("updated_parsed")),
                lang="en",
                skip_fulltext=is_self,
                raw={
                    "permalink": permalink,
                    "subreddit": tags[0] if tags else subreddit,
                    "is_self": is_self,
                    "thumbnail": thumbnails[0].get("url") if thumbnails else None,
                },
            )
        )
    return FetchResult(entries)
