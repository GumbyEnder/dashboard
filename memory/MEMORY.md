# Long-Term Memory

## Key Integrations

### Google Drive (via rclone)
- **Remote:** `gdrive`
- **Project folder:** `/Personal/Samwise Bot/`
- **Purpose:** Project management, replacing Notion
- **Structure:** _inbox.md, _index.md, projects/, archive/

## Key People

- **Silja** — Shane's "Girl Friday" / trusted assistant, knows everything, admin in Discord channel
- **Zander** — Shane's son
- **Nikki** — Shane's wife, email: nikki@robinett.com

## Shane's Preferences
- Prefers professional but conversational tone
- Wants to move away from Notion → using markdown in Google Drive instead
- Timezone: America/New_York

### Software Lineage
- **OpenClaw** = Rebrand/fork of Clawdbot (newer ecosystem)

### Automated Monitoring
- **Process Monitor:** Every hour → WhatsApp alerts if thresholds exceeded
  - GOG processes >10, Memory >80%, Zombies >5, Total processes >500
  - Auto-kills runaway processes when safe

### Critical System Issue (RESOLVED 2026-02-11)
- **Problem:** 2,777 zombie GOG Gmail processes consumed 55GB RAM, causing OOM killer to terminate services
- **Symptoms:** Mission Control & ClawPad repeatedly getting SIGKILL'd  
- **Resolution:** `pkill -f "gog gmail search"` freed 20GB RAM
- **Lesson:** Monitor for runaway processes, especially GOG CLI commands
- **Prevention:** Need to investigate GOG skill to prevent zombie process spawning

## Important Paths
- Google Drive projects: `gdrive:/Personal/Samwise Bot/`
