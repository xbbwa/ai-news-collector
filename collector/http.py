from __future__ import annotations

import logging
from dataclasses import dataclass

import httpx

from .config import Settings, SourceConfig

log = logging.getLogger(__name__)

# Status codes that usually mean "bot protection", where a browser TLS fingerprint helps.
_IMPERSONATE_ON = {403, 503}


@dataclass
class Page:
    status_code: int
    url: str
    content: bytes
    content_type: str
    via: str  # "httpx" | "impersonate"

    @property
    def text(self) -> str:
        for enc in ("utf-8", "gb18030"):
            try:
                return self.content.decode(enc)
            except UnicodeDecodeError:
                continue
        return self.content.decode("utf-8", errors="replace")


class HttpClients:
    """Shared HTTP clients.

    - `direct` / `proxied`: plain httpx clients (proxied uses PROXY_URL for sources marked proxy=true).
    - `fetch_page`: robust page download used for full-text extraction. Falls back to a
      Chrome-impersonating client (curl_cffi) when a site answers 403/503, which is what
      Cloudflare-fronted sites such as openai.com return to ordinary HTTP clients.
    """

    def __init__(self, settings: Settings):
        self.settings = settings
        headers = {
            "User-Agent": settings.user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8",
        }
        timeout = httpx.Timeout(settings.request_timeout)
        limits = httpx.Limits(max_connections=64, max_keepalive_connections=20)
        # HTTP/2 disabled on purpose: httpx+h2 connection reuse under high concurrency
        # produced ConnectionState.CLOSED protocol errors in testing.
        self.direct = httpx.AsyncClient(
            headers=headers, timeout=timeout, limits=limits, follow_redirects=True
        )
        if settings.proxy_url:
            self.proxied = httpx.AsyncClient(
                headers=headers,
                timeout=timeout,
                limits=limits,
                follow_redirects=True,
                proxy=settings.proxy_url,
            )
        else:
            self.proxied = self.direct

    @property
    def has_proxy(self) -> bool:
        return self.proxied is not self.direct

    def for_source(self, source: SourceConfig) -> httpx.AsyncClient:
        return self.proxied if source.proxy else self.direct

    async def aclose(self) -> None:
        await self.direct.aclose()
        if self.has_proxy:
            await self.proxied.aclose()

    # -- page download with fallbacks ---------------------------------------------

    async def fetch_page(self, url: str, use_proxy: bool) -> Page:
        """Download a page. Order of attempts:

        1. httpx on the requested route (direct or proxy)
        2. Chrome-impersonated request on the same route (if 403/503 or transport error)
        3. If route was direct and a proxy exists: repeat 1-2 through the proxy
        """
        routes = [use_proxy]
        if not use_proxy and self.has_proxy:
            routes.append(True)

        last_exc: Exception | None = None
        last_page: Page | None = None
        for via_proxy in routes:
            client = self.proxied if via_proxy else self.direct
            try:
                resp = await client.get(url)
                page = Page(
                    resp.status_code,
                    str(resp.url),
                    resp.content,
                    resp.headers.get("content-type", ""),
                    "httpx",
                )
                if page.status_code not in _IMPERSONATE_ON:
                    return page
                last_page = page
            except httpx.TransportError as exc:
                last_exc = exc

            try:
                page = await self._fetch_impersonated(url, via_proxy)
                if page.status_code < 400 or page.status_code not in _IMPERSONATE_ON:
                    return page
                last_page = page
            except Exception as exc:  # curl_cffi raises its own error types
                last_exc = exc

        if last_page is not None:
            return last_page
        assert last_exc is not None
        raise last_exc

    async def _fetch_impersonated(self, url: str, via_proxy: bool) -> Page:
        from curl_cffi.requests import AsyncSession

        proxy = self.settings.proxy_url if via_proxy else None
        async with AsyncSession(impersonate="chrome", proxy=proxy) as s:
            resp = await s.get(
                url,
                timeout=self.settings.request_timeout,
                allow_redirects=True,
                headers={"Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8"},
            )
        return Page(
            resp.status_code,
            str(resp.url),
            resp.content,
            resp.headers.get("content-type", ""),
            "impersonate",
        )
