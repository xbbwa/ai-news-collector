from __future__ import annotations

from datetime import datetime, timezone

import httpx

from ..config import SourceConfig
from .base import FetchResult, RawEntry, strip_html

# Algolia's HN index is updated within seconds of a submission and supports
# server-side keyword search, which is far cheaper than walking the Firebase API.
ALGOLIA_SEARCH = "https://hn.algolia.com/api/v1/search_by_date"


async def fetch_hackernews(source: SourceConfig, client: httpx.AsyncClient) -> FetchResult:
    queries: list[str] = source.params.get("queries") or ["AI"]
    min_points: int = int(source.params.get("min_points", 0))
    hits_per_page: int = int(source.params.get("hits_per_page", 50))

    seen: dict[str, RawEntry] = {}
    for query in queries:
        resp = await client.get(
            ALGOLIA_SEARCH,
            params={
                "query": query,
                "tags": "story",
                "hitsPerPage": hits_per_page,
                "numericFilters": f"points>={min_points}",
            },
        )
        resp.raise_for_status()
        for hit in resp.json().get("hits", []):
            object_id = str(hit["objectID"])
            if object_id in seen:
                continue
            hn_url = f"https://news.ycombinator.com/item?id={object_id}"
            url = hit.get("url") or hn_url
            created = hit.get("created_at")
            published = (
                datetime.fromisoformat(created.replace("Z", "+00:00")).astimezone(timezone.utc)
                if created
                else None
            )
            seen[object_id] = RawEntry(
                external_id=f"hn:{object_id}",
                url=url,
                title=hit.get("title") or "(untitled)",
                summary=strip_html(hit.get("story_text")),
                author=hit.get("author"),
                published_at=published,
                lang="en",
                skip_fulltext=url == hn_url,
                raw={
                    "hn_url": hn_url,
                    "points": hit.get("points"),
                    "num_comments": hit.get("num_comments"),
                    "matched_query": query,
                },
            )
    return FetchResult(list(seen.values()))
