"""Probe a URL the way the collector does and print status, content-type, and a body preview.

usage: python scripts/probe.py <url> [--ua "custom UA"] [--proxy http://...]
"""
import argparse
import asyncio

import feedparser
import httpx

DEFAULT_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36 ai-news-collector/0.1"
)


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--ua", default=DEFAULT_UA)
    ap.add_argument("--proxy")
    ap.add_argument("--feed", action="store_true", help="parse as feed and show first entry")
    args = ap.parse_args()

    async with httpx.AsyncClient(
        headers={"User-Agent": args.ua, "Accept": "*/*"},
        timeout=20,
        follow_redirects=True,
        proxy=args.proxy,
    ) as client:
        r = await client.get(args.url)
        print("status:", r.status_code, "| final:", r.url)
        print("content-type:", r.headers.get("content-type"))
        print("length:", len(r.content))
        body = r.text
        print("--- preview ---")
        print(body[:800])
        if args.feed:
            p = feedparser.parse(r.content)
            print("--- feed ---")
            print("bozo:", p.get("bozo"), p.get("bozo_exception"))
            print("entries:", len(p.entries))
            if p.entries:
                e = p.entries[0]
                print("title:", e.get("title"))
                print("link:", e.get("link"))
                summary = e.get("summary") or ""
                content = (e.get("content") or [{}])[0].get("value") or ""
                print("summary len:", len(summary), "| content len:", len(content))
                print("summary preview:", summary[:400])


asyncio.run(main())
