#!/usr/bin/env bash
# Daily pull on the China box (cron 07:01): fetch the digests the collect workflow wrote to the
# `data` branch and place them where OpenClaw reads. It does NOT mark stories as pushed:
# check_openclaw_delivery.py does that only after a real group-delivery receipt succeeds.
#
#   01 7 * * * ~/ai-news-collector/scripts/sync_digest.sh >> ~/logs/ai-news-digest.log 2>&1
#
# Files:
#   digest/curated.md  -> $KB/daily-ai-news-curated.md   (<=20 ranked stories; what OpenClaw pushes)
#   digest/latest.md   -> $KB/daily-ai-news-summary.md   (full 24h list, ~160 stories; reference only)
#   digest/curated.json -> data/curated.json              (marked only after verified delivery)
set -u
REPO="xbbwa/ai-news-collector"
KB="${KB:-/mnt/data/openclaw-kb/openclawdata}"
cd "$(dirname "$0")/.." || exit 1
set -a; [ -f .env ] && . ./.env; set +a
mkdir -p "$KB" data
# The repo is public, so the downloads work anonymously; the PAT (if set) just lifts the rate limit
# when rate limits matter.
auth=(); [ -n "${GITHUB_TOKEN:-}" ] && auth=(-H "Authorization: Bearer $GITHUB_TOKEN")

fetch() {  # fetch <remote path> <local path> <expected first bytes regex>
  local remote="$1" local="$2" expect="$3" tmp url
  tmp="$(mktemp "$(dirname "$local")/.sync-XXXXXX")"
  for url in "https://raw.githubusercontent.com/$REPO/data/$remote" \
             "https://api.github.com/repos/$REPO/contents/$remote?ref=data"; do
    if curl -fsSL -m 90 --retry 2 ${auth[@]+"${auth[@]}"} -H "Accept: application/vnd.github.raw" -o "$tmp" "$url" \
       && head -c 300 "$tmp" | grep -qE "$expect"; then
      chmod 644 "$tmp"; mv "$tmp" "$local"
      echo "$(date '+%F %T') OK   $remote -> $local ($(wc -c < "$local") B)"
      return 0
    fi
  done
  rm -f "$tmp"
  echo "$(date '+%F %T') FAIL $remote (kept previous $local)" >&2
  return 1
}

fetch digest/curated.md   "$KB/daily-ai-news-curated.md" "^# Daily AI News" ; rc_curated=$?
fetch digest/latest.md    "$KB/daily-ai-news-summary.md" "^# Daily AI News" || true
fetch digest/curated.json "data/curated.json"            '"generated_at"'  || true
exit $rc_curated
