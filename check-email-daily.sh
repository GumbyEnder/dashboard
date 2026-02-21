#!/bin/bash
# Email check script — runs 4x daily (8 AM, 12 PM, 4 PM, 8 PM)

EMAIL="samwise@veanox.com"
LOG_FILE="/home/gumbyender/.openclaw/workspace/logs/email-checks-$(date '+%Y-%m-%d').log"

mkdir -p "$(dirname "$LOG_FILE")"

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "[${TIMESTAMP}] Email check..." >> "$LOG_FILE"

# Check unread emails using gog Gmail
UNREAD=$(gog gmail list --query "is:unread" --format json 2>/dev/null | jq length || echo "0")

if [ "$UNREAD" -gt 0 ]; then
  echo "[${TIMESTAMP}] ⚠️  $UNREAD unread emails" >> "$LOG_FILE"
  
  # Get summary of unread
  gog gmail list --query "is:unread" --max-results 5 --format json 2>/dev/null | \
    jq -r '.[] | "\(.from): \(.subject)"' >> "$LOG_FILE" || true
  
  # Alert Shane via WhatsApp if during active hours (outside quiet hours 10 PM - 8 AM)
  HOUR=$(date +%H)
  if [ $HOUR -ge 8 ] && [ $HOUR -lt 22 ]; then
    # Will be sent via separate notification mechanism
    echo "[${TIMESTAMP}] Alert queued for Shane" >> "$LOG_FILE"
  fi
else
  echo "[${TIMESTAMP}] ✅ No unread emails" >> "$LOG_FILE"
fi

echo "" >> "$LOG_FILE"
