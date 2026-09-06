#!/usr/bin/env bash
# Hourly job on the China box (cron): append the items the local collector service stored since
# last time to archive/items/<date>.cn.jsonl, then upload the changed files to the `data` branch
# through the GitHub API. Everything else (digest, merge with the GitHub-side items) happens in
# the collect workflow, which checks out the data branch on every run.
#
#   15 * * * * /home/yino/ai-news-collector/scripts/server_publish.sh >> /home/yino/logs/ai-news-publish.log 2>&1
set -u
cd "$(dirname "$0")/.." || exit 1
mkdir -p data archive/items
exec 9>data/.publish.lock
flock -n 9 || { echo "$(date '+%F %T') previous publish still running, skipping"; exit 0; }

set -a; [ -f .env ] && . ./.env; set +a
PY="${PYTHON:-$HOME/venvs/ai-news-collector/bin/python}"

echo "$(date '+%F %T') export"
"$PY" scripts/export_daily.py --db data/collector.db --out-dir archive/items \
  --cursor data/export_cursor --prune-days 30 --file-suffix .cn || exit 1

if [ -z "${GITHUB_TOKEN:-}" ]; then
  echo "$(date '+%F %T') GITHUB_TOKEN not set in .env - exported locally, upload skipped (will catch up once set)"
  exit 0
fi
echo "$(date '+%F %T') upload"
"$PY" scripts/publish_archive.py --dir archive/items --pattern '*.cn.jsonl' \
  --repo xbbwa/ai-news-collector --branch data --state data/publish_state.json
