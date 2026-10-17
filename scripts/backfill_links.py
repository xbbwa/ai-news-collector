#!/usr/bin/env python3
"""Deterministically backfill canonical source URLs into an LLM-rendered Daily AI News text.

Keeps LLM inference fast and hallucination-free (the model only translates titles and writes
one-sentence Chinese summaries without copying long URLs), then injects each item's canonical
URL from curated.json or curated.md by matching (region, section_index).

Usage:
  python3 scripts/backfill_links.py --curated data/curated.json --in pushed.txt --out pushed-with-links.md
  cat pushed.txt | python3 scripts/backfill_links.py --curated data/curated.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from curate_digest import backfill_links, write_atomic  # noqa: E402


def load_curated_source(path: Path) -> dict | str:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return text


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--curated", type=Path, required=True, help="path to curated.json or curated.md")
    ap.add_argument("--in", dest="input_path", type=Path, help="LLM output text file (default: stdin)")
    ap.add_argument("--out", dest="output_path", type=Path, help="output file path (default: stdout)")
    ap.add_argument(
        "--style",
        choices=("line", "inline"),
        default="line",
        help="'line' adds an indented 🔗 URL line below each item; 'inline' appends ｜🔗 URL",
    )
    args = ap.parse_args()

    if not args.curated.exists():
        print(f"ERROR: curated file not found: {args.curated}", file=sys.stderr)
        return 1

    raw_text = (
        args.input_path.read_text(encoding="utf-8")
        if args.input_path
        else sys.stdin.read()
    )
    curated = load_curated_source(args.curated)
    enriched = backfill_links(raw_text, curated, style=args.style)

    if args.output_path:
        write_atomic(args.output_path, enriched + ("\n" if not enriched.endswith("\n") else ""))
    else:
        sys.stdout.write(enriched + ("\n" if not enriched.endswith("\n") else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
