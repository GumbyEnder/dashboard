#!/bin/bash
# Daily learnings update - runs at 11:59 PM to capture day's reflection

set -e

WORKSPACE="/home/gumbyender/.openclaw/workspace"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "[${TIMESTAMP}] Starting daily learnings update..."

cd "$WORKSPACE"

# 1. Generate latest learnings data
echo "  → Generating learnings data..."
python3 generate-learnings-tab.py

# 2. Check if BRAIN.md or reflection files have been updated today
BRAIN_UPDATED=$(find memory/reflections -name "$(date '+%Y-%m-%d')*" -type f 2>/dev/null | wc -l)

if [ $BRAIN_UPDATED -gt 0 ]; then
    echo "  → Reflection file found, updating dashboard..."
    
    # 3. Commit learnings data
    git add learnings-data.json learnings-snippet.html BRAIN.md 2>/dev/null || true
    git commit -m "Daily learnings update - $(date '+%Y-%m-%d')" 2>/dev/null || true
    
    # 4. Push to GitHub
    git push origin master 2>/dev/null || true
    
    echo "  ✅ Daily learnings update complete"
else
    echo "  → No reflection file for today, skipping update"
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Done."
