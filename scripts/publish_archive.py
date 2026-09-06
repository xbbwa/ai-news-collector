"""Upload changed files to a branch of the public collector repo through the GitHub Contents API.

Used by scripts/sync_digest.sh to send digest/pushed-history.jsonl back to the `data` branch.
Works from machines that reach api.github.com but where git-over-HTTPS stalls (the China box).
Each changed file is PUT whole; a state file remembers what was already uploaded so unchanged
files cost nothing. Stdlib only. (Full-text items no longer go through here: they are pushed to
the private archive repo with git + a deploy key, see scripts/server_publish.sh.)

usage:
  GITHUB_TOKEN=... python3 scripts/publish_archive.py --dir archive/digest --pattern 'pushed-history.jsonl' \
      --remote-dir digest --repo xbbwa/ai-news-collector --branch data --state data/publish_state_digest.json

The token needs "Contents: read and write" on that one repository (fine-grained PAT).
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

API = "https://api.github.com"


def call(method: str, url: str, token: str, body: dict | None = None) -> tuple[int, dict]:
    data = json.dumps(body).encode() if body is not None else None
    req = Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urlopen(req, timeout=180) as resp:
            return resp.status, json.load(resp)
    except HTTPError as exc:
        try:
            payload = json.load(exc)
        except ValueError:
            payload = {}
        return exc.code, payload


def remote_shas(repo: str, branch: str, directory: str, token: str) -> dict[str, str]:
    """Blob sha of every file in <branch>:<directory>, via the trees API (works for any file size)."""
    status, tree = call("GET", f"{API}/repos/{repo}/git/trees/{branch}:{directory}", token)
    if status == 404:
        return {}
    if status != 200:
        raise RuntimeError(f"trees API {status}: {tree.get('message')}")
    return {entry["path"]: entry["sha"] for entry in tree.get("tree", []) if entry.get("type") == "blob"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", type=Path, required=True, help="local directory holding the files")
    ap.add_argument("--pattern", default="*.jsonl", help="glob within --dir")
    ap.add_argument("--repo", required=True, help="owner/name")
    ap.add_argument("--branch", default="data")
    ap.add_argument("--remote-dir", default=None, help="directory in the repo (default: basename of --dir)")
    ap.add_argument("--state", type=Path, required=True, help="json file remembering what was uploaded")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("ERROR: GITHUB_TOKEN is not set", file=sys.stderr)
        return 2
    remote_dir = args.remote_dir or args.dir.name

    state: dict[str, dict] = json.loads(args.state.read_text()) if args.state.exists() else {}
    pending = []
    for path in sorted(args.dir.glob(args.pattern)):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if state.get(path.name, {}).get("sha256") == digest:
            continue
        pending.append((path, digest))
    if not pending:
        print("nothing to upload")
        return 0

    shas = remote_shas(args.repo, args.branch, remote_dir, token)
    failures = 0
    for path, digest in pending:
        content = base64.b64encode(path.read_bytes()).decode()
        lines = sum(1 for line in path.read_bytes().splitlines() if line.strip())
        body = {
            "message": f"server: {remote_dir}/{path.name} ({lines} items)",
            "content": content,
            "branch": args.branch,
        }
        for attempt in (1, 2):
            if path.name in shas:
                body["sha"] = shas[path.name]
            status, resp = call("PUT", f"{API}/repos/{args.repo}/contents/{remote_dir}/{path.name}", token, body)
            if status in (200, 201):
                state[path.name] = {"sha256": digest, "size": path.stat().st_size, "remote_sha": resp["content"]["sha"]}
                print(f"uploaded {path.name} ({path.stat().st_size} B, {lines} items)")
                break
            if status == 409 and attempt == 1:  # someone changed the file meanwhile: refresh sha and retry
                shas = remote_shas(args.repo, args.branch, remote_dir, token)
                continue
            failures += 1
            print(f"FAILED {path.name}: HTTP {status} {resp.get('message')}", file=sys.stderr)
            break

    args.state.parent.mkdir(parents=True, exist_ok=True)
    args.state.write_text(json.dumps(state, indent=1, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
