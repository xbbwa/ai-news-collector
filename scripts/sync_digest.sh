#!/usr/bin/env bash
# Daily pull on the China box (cron 07:01): fetch the digests the collect workflow wrote to the
# `data` branch and place them where OpenClaw reads, then tell GitHub which stories were pulled
# (pushed-history.jsonl) so tomorrow's curated list excludes them.
#
#   01 7 * * * ~/ai-news-collector/scripts/sync_digest.sh >> ~/logs/ai-news-digest.log 2>&1
#
# Files:
#   digest/curated.md  -> $KB/daily-ai-news-curated.md   (<=20 ranked stories; what OpenClaw pushes)
#   digest/latest.md   -> $KB/daily-ai-news-summary.md   (full 24h list, ~160 stories; reference only)
#   digest/curated.json -> data/curated.json              (machine-readable copy for mark_pushed.py)
set -u
REPO="xbbwa/ai-news-collector"
KB="${KB:-/mnt/data/openclaw-kb/openclawdata}"
cd "$(dirname "$0")/.." || exit 1
set -a; [ -f .env ] && . ./.env; set +a
mkdir -p "$KB" data archive/digest
# The repo is public, so the downloads work anonymously; the PAT (if set) just lifts the rate limit
# and is required for the pushed-history upload below.
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

# Mark what we just pulled as pushed and send that list back to GitHub.
if [ "$rc_curated" -eq 0 ] && [ -s data/curated.json ]; then
  python3 scripts/mark_pushed.py --curated data/curated.json --history archive/digest/pushed-history.jsonl
  if [ -n "${GITHUB_TOKEN:-}" ]; then
    "${PYTHON:-$HOME/venvs/ai-news-collector/bin/python}" scripts/publish_archive.py --dir archive/digest \
      --pattern 'pushed-history.jsonl' --remote-dir digest --repo "$REPO" --branch data \
      --state data/publish_state_digest.json
  else
    echo "$(date '+%F %T') GITHUB_TOKEN not set: pushed-history not uploaded" >&2
  fi
fi
exit $rc_curated
