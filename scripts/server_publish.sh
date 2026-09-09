#!/usr/bin/env bash
# Hourly job on the China box (cron): append the items the local collector service stored since
# last time to <archive>/items/<date>.cn.jsonl and push them to the PRIVATE archive repo
# (xbbwa/ai-news-archive). Everything else (digest, merge with the GitHub-side items) happens in
# the collect workflow, which checks out both repos on every run.
#
# The archive is a plain git clone pushed over SSH on port 443 with its own deploy key
# (~/.ssh/config alias `github-ai-news-archive`, see README "服务器侧"). The fine-grained PAT in .env
# only covers the public collector repo, so it is not used here.
#
#   15 * * * * ~/ai-news-collector/scripts/server_publish.sh >> ~/logs/ai-news-publish.log 2>&1
set -u
cd "$(dirname "$0")/.." || exit 1
mkdir -p data
exec 9>data/.publish.lock
flock -n 9 || { echo "$(date '+%F %T') previous publish still running, skipping"; exit 0; }

set -a; [ -f .env ] && . ./.env; set +a
PY="${PYTHON:-$HOME/venvs/ai-news-collector/bin/python}"
ARCHIVE_DIR="${ARCHIVE_DIR:-$HOME/ai-news-archive}"

if [ ! -d "$ARCHIVE_DIR/.git" ]; then
  echo "$(date '+%F %T') ERROR: $ARCHIVE_DIR is not a git clone of the archive repo (see README)"; exit 1
fi

echo "$(date '+%F %T') sync"
git -C "$ARCHIVE_DIR" pull --rebase -q origin main || echo "$(date '+%F %T') WARN pull failed, exporting anyway"

echo "$(date '+%F %T') export"
"$PY" scripts/export_daily.py --db data/collector.db --out-dir "$ARCHIVE_DIR/items" \
  --cursor data/export_cursor --prune-days 30 --file-suffix .cn || exit 1

cd "$ARCHIVE_DIR" || exit 1
git add -A items
if git diff --cached --quiet; then echo "$(date '+%F %T') nothing to push"; exit 0; fi
files=$(git diff --cached --name-only | sed 's#^items/##' | tr '\n' ' ')
git commit -qm "server: ${files% }" || exit 1
echo "$(date '+%F %T') push"
for attempt in 1 2 3; do
  git pull --rebase -q origin main && git push -q origin HEAD:main && { echo "$(date '+%F %T') pushed ${files% }"; exit 0; }
  echo "$(date '+%F %T') push attempt $attempt failed, retrying"; sleep 10
done
echo "$(date '+%F %T') FAILED to push; commit kept locally, next run will retry" >&2
exit 1
