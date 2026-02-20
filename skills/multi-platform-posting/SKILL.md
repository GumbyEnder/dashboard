# Multi-Platform Posting — Schedule Content Everywhere

**Purpose:** Move beyond single-platform tweets to coordinated multi-channel posting.

**Option A: Typefully (Twitter/X Optimized)**
- Best for: Long-form threads, sophisticated X strategy
- Platforms: X, LinkedIn, Mastodon, Threads, Bluesky (5 platforms)
- Strength: Built for thread creators, best X analytics
- API: Typefully API

**Option B: Postiz (Omnichannel)**
- Best for: Broadcast to many channels at once
- Platforms: 28+ (X, LinkedIn, Reddit, TikTok, Instagram, YouTube, etc.)
- Strength: True omnichannel, one post → everywhere
- Cost: More affordable at scale

**Recommendation:**
- **Start with Typefully** (focused on quality over reach)
- **Graduate to Postiz** when you want broader distribution

**Current Setup:**
- Manual cron posting to Twitter via API
- One post at a time

**Future Setup (Typefully):**
```bash
# Schedule a thread
typefully schedule --thread "tweet1,tweet2,tweet3" --time "2026-02-21 09:00"

# Schedule with analytics
typefully post "Your distributed systems take" \
  --platforms "x,linkedin" \
  --schedule "2026-02-21 09:00"
```

**Integration:**
- API key setup (Typefully or Postiz)
- Dashboard for scheduling
- Analytics tracking
- Auto-retry on failures

**Commands:**
```bash
typefully draft "Your take here"
typefully schedule --when "daily-9am"
typefully analytics --last-7-days
```

**Output:**
- Scheduled posts across platforms
- Performance analytics
- Audience engagement metrics
- Content calendar

---

**Status:** ⏳ Awaiting your choice (Typefully vs Postiz)
**Recommendation:** Start with Typefully, add Postiz when you want multi-channel broadcast
