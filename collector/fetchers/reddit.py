from __future__ import annotations

import asyncio
import time
from datetime import datetime, timezone

import httpx

from ..config import Settings, SourceConfig
from .base import FetchResult, RawEntry

TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
API_BASE = "https://oauth.reddit.com"


class _TokenCache:
    """Application-only OAuth token, shared by all reddit sources in the process."""

    def __init__(self) -> None:
        self.token: str | None = None
        self.expires_at: float = 0.0
        self.lock = asyncio.Lock()

    async def get(self, client: httpx.AsyncClient, settings: Settings) -> str:
        async with self.lock:
            if self.token and time.time() < self.expires_at - 60:
                return self.token
            if not (settings.reddit_client_id and settings.reddit_client_secret):
                raise RuntimeError(
                    "Reddit now requires OAuth. Set REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET "
                    "(create a 'script' app at https://www.reddit.com/prefs/apps)."
                )
            resp = await client.post(
                TOKEN_URL,
                data={"grant_type": "client_credentials"},
                auth=(settings.reddit_client_id, settings.reddit_client_secret),
                headers={"User-Agent": settings.reddit_user_agent},
            )
            resp.raise_for_status()
            payload = resp.json()
            self.token = payload["access_token"]
            self.expires_at = time.time() + float(payload.get("expires_in", 3600))
            return self.token


_tokens = _TokenCache()


async def fetch_reddit(
    source: SourceConfig, client: httpx.AsyncClient, settings: Settings
) -> FetchResult:
    subreddit: str = source.params["subreddit"]
    listing: str = source.params.get("listing", "new")
    limit: int = int(source.params.get("limit", 50))

    token = await _tokens.get(client, settings)
    resp = await client.get(
        f"{API_BASE}/r/{subreddit}/{listing}",
        params={"limit": limit, "raw_json": 1},
        headers={
            "Authorization": f"bearer {token}",
            "User-Agent": settings.reddit_user_agent,
        },
    )
    if resp.status_code == 401:
        _tokens.token = None  # force refresh next round
    resp.raise_for_status()

    entries: list[RawEntry] = []
    for child in resp.json().get("data", {}).get("children", []):
        d = child.get("data") or {}
        if not d.get("permalink"):
            continue
        permalink = "https://www.reddit.com" + d["permalink"]
        is_self = bool(d.get("is_self"))
        url = permalink if is_self else (d.get("url") or permalink)
        entries.append(
            RawEntry(
                external_id=d.get("name") or permalink,
                url=url,
                title=d.get("title") or "(untitled)",
                summary=(d.get("selftext") or "").strip() or None,
                author=d.get("author"),
                published_at=datetime.fromtimestamp(d["created_utc"], tz=timezone.utc)
                if d.get("created_utc")
                else None,
                lang="en",
                skip_fulltext=is_self,
                raw={
                    "permalink": permalink,
                    "subreddit": subreddit,
                    "score": d.get("score"),
                    "num_comments": d.get("num_comments"),
                    "flair": d.get("link_flair_text"),
                    "is_self": is_self,
                },
            )
        )
    return FetchResult(entries)
