#!/usr/bin/env bash
# Update the code on the China box from GitHub without git: the codeload tarball is a plain HTTPS
# download that works there, while git-over-HTTPS and SSH both stall. Keeps data/, archive/ and
# .env, reinstalls requirements, restarts the collector service.
set -eu
REPO=xbbwa/ai-news-collector
BRANCH="${1:-main}"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV="${VENV:-$HOME/venvs/ai-news-collector}"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
curl -fsSL -m 180 "https://codeload.github.com/$REPO/tar.gz/refs/heads/$BRANCH" | tar -xz -C "$TMP" --strip-components=1
rsync -a --delete --exclude data --exclude archive --exclude .env --exclude .venv "$TMP/" "$DIR/"
chmod +x "$DIR"/scripts/*.sh

[ -x "$VENV/bin/python" ] || python3 -m venv "$VENV"
"$VENV/bin/pip" install -q -i "${PIP_INDEX_URL:-https://mirrors.aliyun.com/pypi/simple/}" -r "$DIR/requirements.txt"

systemctl --user daemon-reload
systemctl --user restart ai-news-collector.service
sha="$(curl -fsSL -m 30 "https://api.github.com/repos/$REPO/commits/$BRANCH" | python3 -c 'import sys, json; print(json.load(sys.stdin)["sha"][:7])' 2>/dev/null || echo unknown)"
echo "$sha" > "$DIR/DEPLOYED_COMMIT"
echo "$(date '+%F %T') updated $DIR to $BRANCH@$sha and restarted ai-news-collector.service"
