from __future__ import annotations

import asyncio
import hashlib
import logging
import re
from dataclasses import dataclass
from datetime import timedelta
from functools import lru_cache
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from .config import Settings, SourceConfig
from .extract import extract_article
from .fetchers import RawEntry, fetch
from .http import HttpClients
from .models import Item, SourceState, to_utc_naive, utcnow

log = logging.getLogger(__name__)

_TRACKING_PARAMS = {"fbclid", "gclid", "mc_cid", "mc_eid", "ref_src", "igshid", "spm"}


def normalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    query = [
        (k, v)
        for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if not k.lower().startswith("utm_") and k.lower() not in _TRACKING_PARAMS
    ]
    path = parts.path or "/"
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/")
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, urlencode(query), ""))


def url_hash(url: str) -> str:
    return hashlib.sha256(normalize_url(url).encode("utf-8")).hexdigest()


@lru_cache(maxsize=256)
def _keyword_pattern(keywords: tuple[str, ...]) -> re.Pattern[str]:
    """One alternation regex for a keyword list.

    Pure-ASCII words are matched as whole tokens (optionally plural), so "AI" hits
    "AI芯片", "AI-powered", "(AI)" and "AIGC" but not "said", "aim", "Airbnb" or "OpenAI".
    Everything else (CJK terms, phrases, "A.I.") is a plain case-insensitive substring.
    """
    parts = []
    for kw in keywords:
        kw = kw.strip()
        if not kw:
            continue
        if re.fullmatch(r"[A-Za-z]+", kw):
            parts.append(rf"(?<![A-Za-z])(?i:{re.escape(kw)}s?)(?![a-z])")
        else:
            parts.append(rf"(?i:{re.escape(kw)})")
    return re.compile("|".join(parts) or r"(?!x)x")


def matches_keywords(entry: RawEntry, keywords: list[str]) -> bool:
    if not keywords:
        return True
    haystack = f"{entry.title}\n{entry.summary or ''}"
    return _keyword_pattern(tuple(keywords)).search(haystack) is not None


def is_fresh(entry: RawEntry, max_age_days: int | None) -> bool:
    """Drop entries older than the cutoff. Entries without a date are kept."""
    if not max_age_days or entry.published_at is None:
        return True
    cutoff = utcnow() - timedelta(days=max_age_days)
    published = to_utc_naive(entry.published_at)
    return published is None or published >= cutoff


@dataclass
class NewItem:
    id: int
    url: str
    skip_fulltext: bool
    use_proxy: bool


class Collector:
    def __init__(
        self, settings: Settings, clients: HttpClients, session_factory: sessionmaker[Session]
    ):
        self.settings = settings
        self.clients = clients
        self.session_factory = session_factory
        self._fulltext_sem = asyncio.Semaphore(settings.fulltext_concurrency)

    async def run_source(self, source: SourceConfig) -> int:
        """Poll one source once. Returns the number of newly stored items. Raises on fetch failure."""
        with self.session_factory() as s:
            state = s.get(SourceState, source.id)
            if state is None:
                state = SourceState(source_id=source.id)
                s.add(state)
                s.commit()
            etag, last_modified = state.etag, state.last_modified

        try:
            result = await fetch(source, self.clients, etag, last_modified)
        except Exception as exc:
            self._record_failure(source, exc)
            raise

        if result.not_modified:
            self._record_success(source, etag, last_modified, added=0)
            return 0

        if source.time_offset_hours:
            shift = timedelta(hours=source.time_offset_hours)
            for e in result.entries:
                if e.published_at is not None:
                    e.published_at += shift

        entries = [
            e
            for e in result.entries
            if e.url and matches_keywords(e, source.keywords) and is_fresh(e, source.max_age_days)
        ]
        new_items = self._store_new(source, entries)
        self._record_success(source, result.etag, result.last_modified, added=len(new_items))

        if source.fetch_fulltext and new_items:
            await asyncio.gather(*(self._extract_one(item) for item in new_items))
        return len(new_items)

    # -- storage -----------------------------------------------------------------

    def _store_new(self, source: SourceConfig, entries: list[RawEntry]) -> list[NewItem]:
        if not entries:
            return []

        by_hash: dict[str, RawEntry] = {}
        for e in entries:
            by_hash.setdefault(url_hash(e.url), e)  # dedupe within the batch, first wins

        now = utcnow()
        created: list[NewItem] = []
        with self.session_factory() as s:
            existing = set(
                s.scalars(select(Item.url_hash).where(Item.url_hash.in_(list(by_hash)))).all()
            )
            for h, e in by_hash.items():
                if h in existing:
                    continue
                item = Item(
                    source_id=source.id,
                    source_tier=source.tier,
                    external_id=e.external_id,
                    url=e.url,
                    url_hash=h,
                    title=e.title,
                    author=e.author,
                    lang=e.lang or source.lang,
                    summary=e.summary,
                    published_at=to_utc_naive(e.published_at),
                    fetched_at=now,
                    extract_status="skipped"
                    if (e.skip_fulltext or not source.fetch_fulltext)
                    else "pending",
                    raw=e.raw or None,
                )
                s.add(item)
                s.flush()
                created.append(
                    NewItem(
                        id=item.id,
                        url=e.url,
                        skip_fulltext=e.skip_fulltext,
                        use_proxy=source.proxy,
                    )
                )
            s.commit()
        return created

    def _record_success(
        self, source: SourceConfig, etag: str | None, last_modified: str | None, added: int
    ) -> None:
        now = utcnow()
        with self.session_factory() as s:
            state = s.get(SourceState, source.id)
            assert state is not None
            state.etag = etag
            state.last_modified = last_modified
            state.last_fetch_at = now
            state.last_success_at = now
            state.last_error = None
            state.consecutive_failures = 0
            state.total_items += added
            s.commit()

    def _record_failure(self, source: SourceConfig, exc: Exception) -> None:
        with self.session_factory() as s:
            state = s.get(SourceState, source.id)
            assert state is not None
            state.last_fetch_at = utcnow()
            state.last_error = f"{type(exc).__name__}: {exc}"[:2000]
            state.consecutive_failures += 1
            s.commit()

    # -- full text ---------------------------------------------------------------

    async def _extract_one(self, item: NewItem) -> None:
        if item.skip_fulltext:
            return
        async with self._fulltext_sem:
            try:
                data = await extract_article(item.url, self.clients, item.use_proxy)
            except Exception as exc:
                self._mark_extract_failed(item.id, exc)
                log.debug("extract failed for %s: %s", item.url, exc)
                return

        with self.session_factory() as s:
            row = s.get(Item, item.id)
            if row is None:
                return
            row.content = data.get("text")
            row.top_image = data.get("image") or row.top_image
            row.author = row.author or data.get("author")
            row.published_at = row.published_at or to_utc_naive(data.get("date_parsed"))
            if data.get("language"):
                row.lang = data["language"]
            if not row.summary and data.get("excerpt"):
                row.summary = data["excerpt"]
            row.extract_status = "ok"
            row.extract_error = None
            raw = dict(row.raw or {})
            raw["final_url"] = data.get("final_url")
            raw["sitename"] = data.get("sitename")
            raw["fetched_via"] = data.get("fetched_via")
            row.raw = raw
            s.commit()

    def _mark_extract_failed(self, item_id: int, exc: Exception) -> None:
        with self.session_factory() as s:
            row = s.get(Item, item_id)
            if row is None:
                return
            row.extract_status = "failed"
            row.extract_error = f"{type(exc).__name__}: {exc}"[:1000]
            s.commit()

    async def retry_failed_extractions(
        self, sources: dict[str, SourceConfig], limit: int = 100
    ) -> int:
        """Re-run full-text extraction for items that previously failed or were left pending."""
        with self.session_factory() as s:
            rows = s.scalars(
                select(Item)
                .where(Item.extract_status.in_(["failed", "pending"]))
                .order_by(Item.id.desc())
                .limit(limit)
            ).all()
            targets = [
                NewItem(
                    id=r.id,
                    url=r.url,
                    skip_fulltext=False,
                    use_proxy=sources[r.source_id].proxy if r.source_id in sources else False,
                )
                for r in rows
            ]
        await asyncio.gather(*(self._extract_one(t) for t in targets))
        return len(targets)
