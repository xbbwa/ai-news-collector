from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from sqlalchemy import JSON, DateTime, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def utcnow() -> datetime:
    # Stored naive in UTC so SQLite and PostgreSQL behave the same.
    return datetime.now(timezone.utc).replace(tzinfo=None)


def to_utc_naive(dt: datetime | None) -> datetime | None:
    if dt is None:
        return None
    if dt.tzinfo is not None:
        dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
    return dt


class Base(DeclarativeBase):
    pass


class SourceState(Base):
    __tablename__ = "source_state"

    source_id: Mapped[str] = mapped_column(String(64), primary_key=True)
    etag: Mapped[str | None] = mapped_column(String(512))
    last_modified: Mapped[str | None] = mapped_column(String(128))
    last_fetch_at: Mapped[datetime | None] = mapped_column(DateTime)
    last_success_at: Mapped[datetime | None] = mapped_column(DateTime)
    last_error: Mapped[str | None] = mapped_column(Text)
    consecutive_failures: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    total_items: Mapped[int] = mapped_column(Integer, default=0, nullable=False)


class Item(Base):
    __tablename__ = "items"

    # Monotonic id doubles as the cursor for incremental consumers.
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    source_id: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    source_tier: Mapped[int] = mapped_column(Integer, nullable=False)
    external_id: Mapped[str] = mapped_column(String(1024), nullable=False)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    url_hash: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str | None] = mapped_column(Text)
    lang: Mapped[str | None] = mapped_column(String(16))
    summary: Mapped[str | None] = mapped_column(Text)
    content: Mapped[str | None] = mapped_column(Text)
    top_image: Mapped[str | None] = mapped_column(Text)
    published_at: Mapped[datetime | None] = mapped_column(DateTime, index=True)
    fetched_at: Mapped[datetime] = mapped_column(DateTime, index=True, nullable=False)
    extract_status: Mapped[str] = mapped_column(
        String(16), default="pending", nullable=False
    )  # pending | ok | failed | skipped
    extract_error: Mapped[str | None] = mapped_column(Text)
    raw: Mapped[dict[str, Any] | None] = mapped_column(JSON)

    def to_dict(self) -> dict[str, Any]:
        def iso(dt: datetime | None) -> str | None:
            return dt.replace(tzinfo=timezone.utc).isoformat() if dt else None

        return {
            "id": self.id,
            "source_id": self.source_id,
            "source_tier": self.source_tier,
            "external_id": self.external_id,
            "url": self.url,
            "title": self.title,
            "author": self.author,
            "lang": self.lang,
            "summary": self.summary,
            "content": self.content,
            "top_image": self.top_image,
            "published_at": iso(self.published_at),
            "fetched_at": iso(self.fetched_at),
            "extract_status": self.extract_status,
            "extract_error": self.extract_error,
            "raw": self.raw,
        }
