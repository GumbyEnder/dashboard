# Self-Review Log

## 2026-01-31
[2026-01-31] TAG: depth
MISS: Failed to log Moltbook post from 2026-01-30 - major memory gap for external actions
FIX: Implemented mandatory external action logging, heartbeat memory checks, cross-session sync protocols

## 2026-01-30  
Key learnings:
- Always dig into error patterns (Discord delivery was fixable)
- Verify fixes work (cron delivery confirmed successful)  
- Focus heartbeat alerts on time-sensitive items
- Don't assume API success = correct output

## 2026-02-11
TAG: stability
MISS: 2,777 GOG zombie processes consumed 55GB RAM, causing OOM killer to terminate services
FIX: Implemented process monitoring thresholds (GOG >10, zombies >5, memory >80%, total >500)
LESSON: Never run GOG gmail search without limit protection; auto-kill runaway processes

## 2026-02-12 (clawd2 closure)
TAG: migration
MISS: Instance became unstable with conflicting services (systemd, D-Bus, dashboard, ClawPad)
FIX: Migrated to minimal workspace (.openclaw/workspace) with only core gateway
LESSON: Keep it simple - strip out bloatware (Mission Control, ClawPad, PM2 ecosystem)
