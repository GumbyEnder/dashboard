# PARA Second Brain — Organized Knowledge System

**Purpose:** Structure knowledge using PARA (Projects, Areas, Resources, Archive) + make it all searchable.

**PARA Framework:**
- **Projects:** Active work (goals, deadlines, deliverables)
- **Areas:** Ongoing responsibilities (no deadline, indefinite)
- **Resources:** Reference materials (tools, templates, examples)
- **Archive:** Completed/inactive items

**Your Current Structure:**
```
workspace/
├── Projects/
│   ├── Darkness Emergent/
│   │   ├── character-profiles/ (189 images, markdown files)
│   │   └── event-data/
│   ├── SKYX/
│   └── By Night Studios/
├── Areas/
│   ├── Portfolio/ (tracking, updates)
│   ├── Self-Evolution/ (BRAIN.md, PLAYBOOK.md, reflections)
│   ├── Content/ (tweets, blog drafts)
│   └── Daily Operations/ (heartbeat checks, system health)
├── Resources/
│   ├── Tools/ (TOOLS.md, available skills)
│   ├── References/ (docs, guides)
│   └── Templates/ (reflection, project templates)
└── Archive/
    └── Completed Projects
```

**Searchability:**
- Semantic search across all areas
- Full-text indexing
- Quick retrieval: "What did I do on Darkness Emergent?"
- Trend analysis: "How have I grown?"

**Integration:**
- Symlink trick for unified search
- Automated indexing via cron
- Search interface (CLI + dashboard)

**Commands:**
```bash
# Search across PARA
para search "darkness emergent patterns"
para search --area "Self-Evolution" 
para index  # rebuild search index

# Organize
para move portfolio areas/portfolio  # move to Areas
para archive "Old Project"
```

**Output:**
- Indexed knowledge base
- Monthly PARA review report
- Growth metrics per area

---

**Status:** ✅ Ready to implement alongside memory system
