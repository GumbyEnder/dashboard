## HEARTBEAT.md

### System Status  
- **Current Version:** 2026.2.17 
- **Status:** Fresh migration from clawd2 - minimal services running
- **Last Update:** 2026-02-20 14:50 EST (Self-evolution framework added)
- **Services:** OpenClaw Gateway ✅ | No Dashboard/ClawPad (stripped for stability)
- **Note:** Running clean manual gateway process only

### Session Startup (Read Every Time)
- [ ] Read BRAIN.md (what I'm thinking about)
- [ ] Read PLAYBOOK.md (how I decide)
- [ ] Review yesterday's reflection if it exists
- [ ] Check latest MEMORY.md for long-term context

### Daily Checks (During Heartbeat)
- [ ] System health (memory, zombies, GOG processes)
- [ ] WhatsApp quiet hours (10 PM - 8 AM)
- [ ] Memory maintenance (review daily files)
- [ ] Are BRAIN.md and PLAYBOOK.md being followed? (Call Shane if not)
- [ ] Email checks (4x daily via cron: 8 AM, 12 PM, 4 PM, 8 PM)
  - Automated: samwise@veanox.com unread count
  - Logging: logs/email-checks-YYYY-MM-DD.log
  - Alert: Shane notified if unread (outside quiet hours 10 PM - 8 AM)

### Session Reflection (End of Significant Work)
- [ ] Did I commit or hedge? Where?
- [ ] What pattern did I notice?
- [ ] What would I do differently?
- [ ] Save to: `memory/reflections/YYYY-MM-DD-HH-MM.md`

### Monthly Review (1st of month)
- [ ] Review all reflections from past month
- [ ] Update BRAIN.md with evolved thinking
- [ ] Update PLAYBOOK.md if I violated it
- [ ] Update SOUL.md if identity shifted

### Known Issues (Inherited)
- GOG skill can spawn zombie processes - monitor carefully
- Avoid heavy dashboard/mission-control services
- Keep minimal for stability
