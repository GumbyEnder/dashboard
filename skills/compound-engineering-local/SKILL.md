# Compound Engineering — AI Self-Improvement Engine

**Purpose:** Auto-learn from sessions, extract insights, update memory files, compound knowledge over time.

**How It Works:**
1. Session completes
2. Extract learnings (what worked, what failed, patterns)
3. Update BRAIN.md + reflections
4. Next session reads updated files → improves automatically

**Triggers:**
- End of significant work session
- Daily midnight via cron
- On user request: "reflect on today"

**Integration:**
- Reads: Daily reflection files from `memory/reflections/`
- Updates: BRAIN.md with evolved patterns
- Stores: Session insights as JSON for trending

**Commands:**
```bash
# Manual trigger
compound-engineering --extract-today
compound-engineering --update-brain
compound-engineering --generate-report
```

**Output:**
- Updated BRAIN.md with new patterns
- Trending insights (most noticed patterns)
- Monthly evolution report

---

**Status:** ✅ Ready to integrate with daily-learnings-update.sh
