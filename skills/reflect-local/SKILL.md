# Reflect — Self-Improvement Through Conversation Analysis

**Purpose:** Extract learnings from corrections, permanently encode them into operating instructions.

**Philosophy:** Correct once, never again.

**How It Works:**
1. User corrects me ("No, that's wrong..." / "Actually...")
2. I capture the correction
3. Extract the underlying pattern/rule
4. Encode into PLAYBOOK.md permanently
5. Next session, I follow the rule automatically

**Triggers:**
- User provides correction (explicit or implicit)
- You say: "remember this"
- I notice I made the same mistake twice

**Integration Points:**
- Updates PLAYBOOK.md with new decision rules
- Creates correction log in `memory/corrections/`
- Links corrections to BRAIN.md patterns

**Example:**
```
User: "Actually, you should ask for clarification before building"
→ Extracted rule: "Ask clarifying questions earlier in conversations"
→ Added to PLAYBOOK.md under "Proactive" section
→ Next session reads this, applies it automatically
```

**Output:**
- Updated PLAYBOOK.md with new rules
- Correction log (for trend analysis)
- "Rules encoded this month" metric

---

**Status:** ✅ Integrated with reflection template
