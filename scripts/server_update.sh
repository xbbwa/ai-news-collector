#!/usr/bin/env bash
# Update the code on the China box from GitHub without git: the tarball is a plain HTTPS download
# that works there, while git-over-HTTPS and SSH both stall. Keeps data/, archive/ and .env,
# reinstalls requirements, restarts the collector service.
# The repo is private, so the tarball is fetched through api.github.com with the PAT from .env
# (it answers with a signed codeload URL that curl follows).
set -eu
REPO=xbbwa/ai-news-collector
BRANCH="${1:-main}"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV="${VENV:-$HOME/venvs/ai-news-collector}"
set -a; [ -f "$DIR/.env" ] && . "$DIR/.env"; set +a
auth=(); [ -n "${GITHUB_TOKEN:-}" ] && auth=(-H "Authorization: Bearer $GITHUB_TOKEN")

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
curl -fsSL -m 180 ${auth[@]+"${auth[@]}"} "https://api.github.com/repos/$REPO/tarball/$BRANCH" | tar -xz -C "$TMP" --strip-components=1
rsync -a --delete --exclude data --exclude archive --exclude .env --exclude .venv "$TMP/" "$DIR/"
chmod +x "$DIR"/scripts/*.sh

[ -x "$VENV/bin/python" ] || python3 -m venv "$VENV"
"$VENV/bin/pip" install -q -i "${PIP_INDEX_URL:-https://mirrors.aliyun.com/pypi/simple/}" -r "$DIR/requirements.txt"

systemctl --user daemon-reload
systemctl --user restart ai-news-collector.service
sha="$(curl -fsSL -m 30 ${auth[@]+"${auth[@]}"} "https://api.github.com/repos/$REPO/commits/$BRANCH" | python3 -c 'import sys, json; print(json.load(sys.stdin)["sha"][:7])' 2>/dev/null || echo unknown)"
echo "$sha" > "$DIR/DEPLOYED_COMMIT"
echo "$(date '+%F %T') updated $DIR to $BRANCH@$sha and restarted ai-news-collector.service"
