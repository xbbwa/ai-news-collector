from __future__ import annotations

from datetime import datetime, timezone

import httpx

from ..config import SourceConfig
from .base import FetchResult, RawEntry

# Public, unauthenticated Hub API (anonymous quota: 500 requests / 5 min). Most labs -
# especially Chinese ones without any RSS - publish weights here hours before or right
# as they announce, so per-organisation model listings are the earliest first-party signal.
API_URL = "https://huggingface.co/api/models"


def _parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


async def fetch_huggingface(source: SourceConfig, client: httpx.AsyncClient) -> FetchResult:
    authors: list[str] = source.params.get("authors") or []
    if not authors:
        raise ValueError(f"source {source.id!r}: huggingface source requires params.authors")
    limit: int = int(source.params.get("limit", 20))

    entries: list[RawEntry] = []
    for author in authors:
        # Sort by lastModified rather than createdAt: repos are usually created private
        # weeks ahead and flipped public (with a final commit) at release time.
        resp = await client.get(
            API_URL,
            params={"author": author, "sort": "lastModified", "direction": -1, "limit": limit},
        )
        resp.raise_for_status()
        for model in resp.json():
            model_id: str | None = model.get("id") or model.get("modelId")
            if not model_id:
                continue
            pipeline = model.get("pipeline_tag")
            library = model.get("library_name")
            tags: list[str] = model.get("tags") or []
            summary_bits = list(dict.fromkeys([b for b in (pipeline, library) if b] + tags))
            modified = _parse_ts(model.get("lastModified"))
            created = _parse_ts(model.get("createdAt"))
            entries.append(
                RawEntry(
                    external_id=f"hf:{model_id}",
                    url=f"https://huggingface.co/{model_id}",
                    title=model_id,
                    summary=", ".join(summary_bits) or None,
                    author=author,
                    published_at=modified or created,
                    lang="en",
                    raw={
                        "model_id": model_id,
                        "author": author,
                        "pipeline_tag": pipeline,
                        "library_name": library,
                        "tags": tags,
                        "likes": model.get("likes"),
                        "downloads": model.get("downloads"),
                        "created_at": model.get("createdAt"),
                        "last_modified": model.get("lastModified"),
                        "gated": model.get("gated"),
                    },
                )
            )
    return FetchResult(entries)
