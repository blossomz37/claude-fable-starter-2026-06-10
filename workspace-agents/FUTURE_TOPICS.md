# Future Topics (tabled, not scheduled)

Parked ideas for later development. Each entry preserves the verified research so
a future session doesn't repeat it. Facts verified against code.claude.com docs
2026-06-10 via claude-code-guide agent.

## 1. Caveman output style as a reusable standard

From `workspace-carlo/ideas/output-styles.md`. A compression codec for chat
responses: metaphor carries semantic load (skill = tribe rules, subagent = hunter,
workflow = carved stick), no function words, one idea per line. Best as a
switchable mode for status/plan/handoff outputs — not the default (readability
loss on educational answers; ambiguous referents in cold re-reads).

Verified mechanics:
- Output styles still exist. `/output-style` command deprecated v2.1.73,
  **removed v2.1.91** — switch via `/config` → Output style or `outputStyle`
  key in settings.json.
- Files: `~/.claude/output-styles/<name>.md` (global) or `.claude/output-styles/`
  (project). Frontmatter: `name`, `description`, `keep-coding-instructions`
  (set true to retain coding behavior).
- Draft style file content exists in the 2026-06-10 chat answer (Wave 3 session,
  after project completion).

## 2. Skills-library preload management (skills manager / INDEX.md)

From `workspace-carlo/ideas/skills-index.md`. Carlo's ~150-skill library bloats
session preload and risks silent truncation of skill descriptions.

Verified mechanics:
- Only frontmatter descriptions preload; shared budget = 1% of context window
  (`skillListingBudgetFraction`, default 0.01); per-description truncation at
  1,536 chars (`maxSkillDescriptionChars`). Overflow truncates least-used skills
  first → breaks their auto-triggering. Diagnose with `/doctor`.
- **`skillOverrides`** (settings.json, v2.1.129+): per-skill `"on"` /
  `"name-only"` / `"user-invocable-only"` / `"off"`; `/skills` menu toggles and
  persists to `.claude/settings.local.json`. This IS the per-project skills
  manager — no symlink scripts needed. Does not govern plugin skills.
- `disable-model-invocation: true` frontmatter: description NOT loaded at all;
  user-only via `/name`; Claude cannot invoke via Skill tool.
- `paths:` frontmatter: glob-scoped auto-loading.
- An INDEX.md cannot replace the frontmatter scan (no harness hook), but works
  as the discoverability layer for hidden skills.

Recommended architecture (undecided, not yet applied):
1. Tier the catalog: ~10–15 globals stay on; deliberate suites (ezpz-*, Twine,
   image-gen) get `disable-model-invocation: true`; long tail `"name-only"`.
2. Generated `~/.myagents/skills/INDEX.md` + global CLAUDE.md pointer ("when a
   task might match a hidden skill, read INDEX.md and suggest the /name").
3. Script-regenerate the index. Check `skills-consolidator` / `agent-commands`
   skills first — may already half-exist (duplication watch).

Crystallize candidate flagged: tiering policy + index generator as a reusable
skill/workflow once tiers are validated.
