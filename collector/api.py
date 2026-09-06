from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .config import Settings, load_sources
from .db import init_db, make_engine, make_session_factory
from .models import Item, SourceState, to_utc_naive


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or Settings.from_env()
    engine = make_engine(settings.database_url)
    init_db(engine)
    session_factory = make_session_factory(engine)
    sources = {s.id: s for s in load_sources(settings)}

    app = FastAPI(title="AI News Collector", version="0.1.0")

    def get_session():
        with session_factory() as s:
            yield s

    @app.get("/health")
    def health(s: Session = Depends(get_session)) -> dict[str, Any]:
        total = s.scalar(select(func.count(Item.id))) or 0
        latest = s.scalar(select(func.max(Item.fetched_at)))
        return {
            "status": "ok",
            "items": total,
            "latest_fetched_at": latest.replace(tzinfo=timezone.utc).isoformat() if latest else None,
        }

    @app.get("/sources")
    def list_sources(s: Session = Depends(get_session)) -> list[dict[str, Any]]:
        states = {st.source_id: st for st in s.scalars(select(SourceState)).all()}
        out = []
        for sid, cfg in sources.items():
            st = states.get(sid)
            out.append(
                {
                    "id": sid,
                    "name": cfg.name,
                    "type": cfg.type,
                    "tier": cfg.tier,
                    "lang": cfg.lang,
                    "interval": cfg.interval,
                    "proxy": cfg.proxy,
                    "enabled": cfg.enabled,
                    "last_success_at": _iso(st.last_success_at) if st else None,
                    "last_error": st.last_error if st else None,
                    "consecutive_failures": st.consecutive_failures if st else 0,
                    "total_items": st.total_items if st else 0,
                }
            )
        return out

    @app.get("/items")
    def list_items(
        since_id: int = Query(0, ge=0, description="Return items with id > since_id (cursor)"),
        limit: int = Query(100, ge=1, le=1000),
        source: str | None = None,
        tier: int | None = Query(None, ge=1, le=3),
        extract_status: str | None = Query(None, pattern="^(pending|ok|failed|skipped)$"),
        fetched_after: datetime | None = Query(
            None, description="Only items fetched at/after this ISO-8601 time (UTC if no offset)"
        ),
        include_content: bool = True,
        s: Session = Depends(get_session),
    ) -> dict[str, Any]:
        stmt = select(Item).where(Item.id > since_id).order_by(Item.id.asc()).limit(limit)
        if source:
            stmt = stmt.where(Item.source_id == source)
        if tier is not None:
            stmt = stmt.where(Item.source_tier == tier)
        if extract_status:
            stmt = stmt.where(Item.extract_status == extract_status)
        if fetched_after is not None:
            stmt = stmt.where(Item.fetched_at >= to_utc_naive(fetched_after))
        rows = s.scalars(stmt).all()
        items = [r.to_dict() for r in rows]
        if not include_content:
            for it in items:
                it.pop("content", None)
        return {
            "items": items,
            "count": len(items),
            "next_since_id": rows[-1].id if rows else since_id,
        }

    @app.get("/items/{item_id}")
    def get_item(item_id: int, s: Session = Depends(get_session)) -> dict[str, Any]:
        row = s.get(Item, item_id)
        if row is None:
            raise HTTPException(status_code=404, detail="item not found")
        return row.to_dict()

    return app


def _iso(dt) -> str | None:  # noqa: ANN001
    return dt.replace(tzinfo=timezone.utc).isoformat() if dt else None


app = create_app()
