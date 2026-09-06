from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Settings:
    database_url: str = "sqlite:///data/collector.db"
    proxy_url: str | None = None
    rsshub_url: str = "http://localhost:1200"
    sources_file: Path = ROOT / "config" / "sources.yaml"
    user_agent: str = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36 ai-news-collector/0.1"
    )
    request_timeout: float = 20.0
    fulltext_concurrency: int = 8
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    log_level: str = "INFO"
    # Only poll sources whose `runner` matches (COLLECTOR_RUNNER). None = all sources.
    # Lets two machines split the list: GitHub Actions takes `github`, the China box `server`.
    runner: str | None = None

    @classmethod
    def from_env(cls) -> "Settings":
        try:
            from dotenv import load_dotenv

            load_dotenv(ROOT / ".env")
        except ImportError:
            pass
        env = os.environ
        return cls(
            database_url=env.get("DATABASE_URL", cls.database_url),
            proxy_url=env.get("PROXY_URL") or None,
            rsshub_url=env.get("RSSHUB_URL", cls.rsshub_url).rstrip("/"),
            sources_file=Path(env.get("SOURCES_FILE", str(cls.sources_file))),
            user_agent=env.get("USER_AGENT", cls.user_agent),
            request_timeout=float(env.get("REQUEST_TIMEOUT", cls.request_timeout)),
            fulltext_concurrency=int(env.get("FULLTEXT_CONCURRENCY", cls.fulltext_concurrency)),
            api_host=env.get("API_HOST", cls.api_host),
            api_port=int(env.get("API_PORT", cls.api_port)),
            log_level=env.get("LOG_LEVEL", cls.log_level).upper(),
            runner=env.get("COLLECTOR_RUNNER") or None,
        )


@dataclass
class SourceConfig:
    id: str
    name: str
    type: str  # rss | hackernews | reddit | huggingface
    url: str | None = None
    tier: int = 2  # 1 = first-party, 2 = professional media, 3 = social/aggregator
    lang: str = "en"
    interval: int = 300  # seconds between polls
    proxy: bool = False  # route through PROXY_URL (for sources blocked in China)
    fetch_fulltext: bool = True
    max_age_days: int | None = 7  # drop entries published earlier than this; None = keep all
    keywords: list[str] = field(default_factory=list)  # if set, keep only matching entries
    params: dict[str, Any] = field(default_factory=dict)  # fetcher-specific options
    # Added to every published_at. For feeds that stamp local time as GMT (infoq.cn is
    # Beijing time labelled "GMT"), -8 turns it back into real UTC.
    time_offset_hours: float = 0
    # Which machine polls this source: "github" (Actions runner in the US; default) or
    # "server" (the box in mainland China, for domestic media and sites that block
    # datacenter IPs). See Settings.runner.
    runner: str = "github"
    enabled: bool = True


SOURCE_FIELDS = {f for f in SourceConfig.__dataclass_fields__}


def load_sources(settings: Settings) -> list[SourceConfig]:
    with open(settings.sources_file, "r", encoding="utf-8") as fh:
        doc = yaml.safe_load(fh) or {}

    defaults: dict[str, Any] = doc.get("defaults") or {}
    sources: list[SourceConfig] = []
    seen_ids: set[str] = set()

    for raw in doc.get("sources") or []:
        merged = {**defaults, **raw}
        unknown = set(merged) - SOURCE_FIELDS
        if unknown:
            raise ValueError(f"source {merged.get('id')!r}: unknown fields {sorted(unknown)}")
        if merged.get("url"):
            merged["url"] = merged["url"].replace("${RSSHUB_URL}", settings.rsshub_url)
        src = SourceConfig(**merged)
        if src.id in seen_ids:
            raise ValueError(f"duplicate source id {src.id!r}")
        if src.type == "rss" and not src.url:
            raise ValueError(f"source {src.id!r}: rss source requires url")
        seen_ids.add(src.id)
        sources.append(src)
    return sources


def for_runner(sources: list[SourceConfig], runner: str | None) -> list[SourceConfig]:
    """Sources assigned to this machine; None means everything (single-machine setup)."""
    return sources if runner is None else [s for s in sources if s.runner == runner]
