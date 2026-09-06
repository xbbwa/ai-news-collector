#!/usr/bin/env bash
# Pull the latest digest from GitHub (data branch) into the file a downstream reader (OpenClaw)
# consumes. The collector itself runs on GitHub Actions; the consuming box only downloads.
# Plain HTTPS file downloads work from mainland China even where the git protocol does not.
#
# Deployed on prod-ubuntu as ~/scripts/sync_ai_news_digest.sh, run by cron at 07:01:
#   01 7 * * * /home/yino/scripts/sync_ai_news_digest.sh >> /home/yino/logs/ai-news-digest.log 2>&1
set -u
OUT="${1:-/mnt/data/openclaw-kb/openclawdata/daily-ai-news-summary.md}"
REPO="xbbwa/ai-news-collector"
URLS=(
  "https://raw.githubusercontent.com/$REPO/data/digest/latest.md"
  "https://api.github.com/repos/$REPO/contents/digest/latest.md?ref=data"
)
mkdir -p "$(dirname "$OUT")"
TMP="$(mktemp "$(dirname "$OUT")/.digest-XXXXXX")"
trap 'rm -f "$TMP"' EXIT

for url in "${URLS[@]}"; do
  if curl -fsSL -m 90 --retry 2 -H "Accept: application/vnd.github.raw" -o "$TMP" "$url" \
     && head -c 200 "$TMP" | grep -q "^# Daily AI News" \
     && [ "$(wc -c < "$TMP")" -gt 1000 ]; then
    chmod 644 "$TMP"
    mv "$TMP" "$OUT"
    trap - EXIT
    echo "$(date '+%F %T') OK  $(wc -c < "$OUT")B via $url"
    exit 0
  fi
  echo "$(date '+%F %T') WARN download failed: $url" >&2
done
echo "$(date '+%F %T') FAIL all sources; kept previous $OUT" >&2
exit 1
