# Use-Case Catalog: Everything an Indie Author Can Do with Claude

> **In plain words:** This is the master menu. Every entry below is a real,
> achievable job — drafting, revising, publishing, marketing, running the business —
> matched to the *surface* where it works best (which Claude you open) and the
> *mechanism* that makes it repeatable (a one-off prompt, a saved skill, an
> automatic hook, and so on). Skim your category, find the row that sounds like
> your Tuesday, and follow the links to the how-to.

## How to read this catalog

**Surface** — where you do it. See [Which tool when](../00-start-here/which-tool-when.md):

- **CLI** — Claude Code in the terminal (full automation: hooks, agent teams, scripting)
- **Code tab** — Claude Code inside Claude Desktop (same engine, no terminal)
- **Cowork** — Claude Desktop's hands-off folder-work tab
- **Desktop-Chat** — Claude Desktop's chat tab (Projects, Artifacts, connectors)
- **web** — claude.ai in a browser · **mobile** — the phone app

**Mechanism** — what makes it work:

- **prompt** — just ask; sometimes with a built-in feature noted in parentheses
  (plan mode, permission rules, CLAUDE.md, a scheduled task)
- **skill** — a saved procedure folder → [skills.md](../02-power-features/skills.md)
- **hook** — an automatic rule that always fires → [hooks.md](../02-power-features/hooks.md)
- **subagent** — delegated parallel/isolated workers → [subagents-and-orchestration.md](../02-power-features/subagents-and-orchestration.md)
- **MCP** — a connector to another app → [mcp.md](../02-power-features/mcp.md)
- **Project** — a claude.ai/Desktop workspace with persistent knowledge
- **Artifact** — the versioned side-panel document in chat

**Difficulty** — *Starter* (type and go), *Intermediate* (one config file or saved
component), *Power* (multiple features wired together). ⚠️ marks a use case that
depends on something not verified in this wiki's feature docs.

---

## 1. Planning & Worldbuilding

| Use case | Best surface | Best mechanism | Difficulty |
|---|---|---|---|
| Voice-brainstorm premises and tropes from the couch, save keepers to a Project | mobile | prompt | Starter |
| Living one-book workspace: synopsis, comp notes, editor feedback, query drafts in one place | web / Desktop-Chat | Project | Starter |
| Series-bible Q&A against uploaded canon ("would Mira know about the harbor fire in book 2?") | Desktop-Chat | Project | Starter |
| Interrogate your magic system for loopholes in read-only plan mode | CLI / Code tab | prompt (plan mode) | Starter |
| Photograph a notebook page or Plottr/Aeon screenshot; get a structured outline back (Fable 5 vision) | Desktop-Chat | prompt | Starter |
| AI-facing story bible Claude reads every session: `CLAUDE.md` + `@series-bible.md` imports | CLI / Code tab | prompt (CLAUDE.md) | Intermediate |
| Character profile generation from a reusable template skill with your required fields | CLI / Code tab | skill | Intermediate |
| Build a chapter-by-chapter timeline file from already-drafted chapters | CLI / Code tab | prompt | Starter |
| World wiki maintenance inside an Obsidian vault (filesystem or Obsidian MCP server) | CLI | MCP | Intermediate |
| Per-pen-name worldbuilding defaults: each pen name's folder gets its own CLAUDE.md (heat level, genre conventions) | CLI | prompt (CLAUDE.md) | Intermediate |
| Outline stress test: one subagent per POV character checks the outline for that character's arc gaps | CLI | subagent | Power |
| NPE-style dossier loader: constraints, tension axes, and ghost-draft subtext notes imported via CLAUDE.md every session | CLI | prompt (CLAUDE.md imports) | Power |
| Generate import-ready timeline CSVs for Aeon Timeline from a story skeleton | CLI | skill | Power |

**Standouts and gotchas.** The Project-based bible Q&A is the fastest first win —
upload once, every chat knows your world. The CLAUDE.md story-bible loader is the
single highest-leverage setup in this category: it turns "re-explain my world every
session" into "Claude already knows" ([claude-md-and-memory.md](../01-claude-code-basics/claude-md-and-memory.md)).
Watch the import cost — pulling a 40k-word bible in full via `@import` eats the
context your chapters need; import a summary plus on-demand files instead. Deep
dive: [research-and-worldbuilding.md](../03-author-workflows/research-and-worldbuilding.md).

## 2. Drafting

| Use case | Best surface | Best mechanism | Difficulty |
|---|---|---|---|
| Draft chapter 14 with the story bible, dossier, and previous chapters read from the project folder | CLI / Code tab | prompt | Starter |
| Voice firewall: "never smooth my sentence fragments; British spelling; em dashes max 1/1,000 words" enforced from CLAUDE.md | CLI / Code tab | prompt (CLAUDE.md) | Starter |
| One long Fable 5 brief that replaces ten prompts: outline → draft → self-critique → revise in a single run | CLI | prompt | Intermediate |
| Scene brief → scene draft via a skill with named arguments (`/scene-draft ch07-s2 "dock confrontation"`) | CLI / Code tab | skill | Intermediate |
| Chapter pipeline as one command: plan, draft, self-audit, save — encoded as `/draft-chapter` | CLI | skill | Intermediate |
| Timestamped auto-backup of every chapter file Claude edits | CLI | hook (PostToolUse) | Intermediate |
| Self-writing progress log: date, chapter, word count appended on every chapter edit | CLI | hook (PostToolUse) | Intermediate |
| House-style re-injection that survives long-session compaction (the `compact` matcher) | CLI | hook (SessionStart) | Power |
| Dictate a scene idea on your phone; Dispatch sends the drafting job to your desktop (Pro/Max) | mobile → Cowork | prompt (Dispatch) | Intermediate |
| Three alternate endings forked from your full current conversation (`/fork`) | CLI | subagent (fork) | Power |
| Overnight drafting or revision job that survives a closed laptop (cloud Code session) | Code tab (Remote) / web | prompt (cloud session) | Power |
| Deep revision-aware drafting: Fable 5 keeps a `revision-notes.md` working file and gets better as it goes | CLI | prompt | Intermediate |
| Co-author setup: shared CLAUDE.md, permission rules, and project skills committed to a shared repo | CLI | Project (shared repo) | Power |

**Standouts and gotchas.** Plain chapter drafting in a project folder is where Claude
Code beats web chat decisively — no re-uploading context, drafts land as real files.
The backup hook should be the first hook any drafting author installs: it is
deterministic, free, and removes the "what did that paragraph say before?" fear
([hooks.md](../02-power-features/hooks.md)). Don't draft long manuscripts in plain
web chat; canon evaporates between sessions. Full pipeline patterns:
[drafting-and-revision.md](../03-author-workflows/drafting-and-revision.md).

## 3. Revision & QA

| Use case | Best surface | Best mechanism | Difficulty |
|---|---|---|---|
| Developmental cold read in plan mode — Claude physically cannot edit a word while you discuss | CLI / Code tab | prompt (plan mode) | Starter |
| Approved line-edit list applied in one flow with `acceptEdits` mode (no twenty confirmations) | CLI / Code tab | prompt | Starter |
| `/rewind` as the undo button when an edit pass goes wrong — restore files and conversation to a checkpoint | CLI | prompt (rewind) | Starter |
| Beta-feedback triage: cluster reader notes by issue, map each to chapters and severity | Cowork / CLI | prompt | Starter |
| Whole-manuscript structural diagnosis on Fable 5: "where does tension flatten, and what's the structural cause?" | CLI | prompt | Intermediate |
| Multi-lens critique: parallel subagents read chapter 14 as a romance reader, a thriller reader, and a timeline tracker — no cross-contamination | CLI | subagent | Intermediate |
| Echo-word / crutch-word / filter-word audit with a bundled counting script (numbers, not vibes) | CLI | skill | Intermediate |
| Chapter "done" gate: an audit checklist skill only *you* can trigger (`disable-model-invocation: true`) | CLI | skill | Intermediate |
| Noisy bulk audit isolated in a subagent: prose-audit script across 40 chapters, only flagged passages return | CLI | subagent | Intermediate |
| Punctuation-tic reduction to a target density (em dashes per 1,000 words) with a changelog | CLI | skill | Power |
| AI-ism audit before publication: flag clustered AI-ish surface tics and rhythm habits | CLI | skill | Power |
| Adversarial verification: one agent proposes a plot fix, a skeptic agent attacks it before you decide | CLI | subagent | Power |
| Revision-checklist enforcement: a prompt-type Stop hook verifies Claude actually finished the checklist before declaring done | CLI | hook (Stop, prompt type) | Power |
| Cross-check a ProWritingAid-style report against the actual manuscript text with exact counts and line numbers | CLI | skill | Power |

**Standouts and gotchas.** Plan mode is the most underused safety feature in
revision: one keystroke (`Shift+Tab`) gives you a beta reader who can see everything
and touch nothing. Multi-lens subagent critique is the signature trick — clean
context per reader means the thriller reader's complaints can't bleed into the
romance reader's verdict — but remember the cost: multi-agent runs use roughly 15×
chat tokens. Keep prose-preserving rules ("never homogenize my voice") in CLAUDE.md
so every audit pass inherits them. Deep dive:
[drafting-and-revision.md](../03-author-workflows/drafting-and-revision.md).

## 4. Continuity & Series Management

| Use case | Best surface | Best mechanism | Difficulty |
|---|---|---|---|
| Per-chapter continuity sweep against the series bible — one subagent per chapter, findings compiled to `reports/continuity.md` | CLI | subagent | Intermediate |
| Series-bible reconciliation: feed books 1–3 plus the bible into Fable 5's 1M context; update the bible to match the page and list every disagreement | CLI | prompt | Intermediate |
| Who-knew-what-when matrix: build a per-character knowledge table from drafted chapters | CLI | prompt | Intermediate |
| Series-wide rules that every book inherits: `MySeries/CLAUDE.md` above the per-book folders | CLI | prompt (CLAUDE.md hierarchy) | Intermediate |
| Series-bible auto-update ritual: `/bible-update chapter-12` extracts new characters, settings, timeline facts and appends them | CLI | skill | Intermediate |
| Live canon lookups mid-draft from a Notion story bible ("what color are Mara's eyes in book 3?") | CLI / Desktop-Chat | MCP | Intermediate |
| Make `originals/` and `published/` untouchable: deny rules plus a PreToolUse blocking hook | CLI | hook (PreToolUse) + permission rules | Intermediate |
| Reusable continuity-checker custom agent with read-only tools (`Read, Grep, Glob`) — physically cannot rewrite prose | CLI | subagent (custom) | Power |
| Weekly scheduled continuity-log refresh: `/schedule` a Friday Cowork task that re-reads the chapters folder | Cowork | prompt (scheduled task) | Intermediate |
| Trilogy-wide timeline reconciliation in one session (travel times, ages, seasons) | CLI | prompt | Power |
| Bible-change alarm: a FileChanged hook flags whenever `series-bible.md` is modified | CLI | hook (FileChanged) | Power |

**Standouts and gotchas.** The per-chapter subagent sweep is the canonical author
use of orchestration — "use subagents to check every chapter against the series
bible" replaces an afternoon of copy-paste, and saving it as a custom agent makes it
one sentence per draft. Note that the built-in Explore agent skips CLAUDE.md, so
restate critical canon rules in the sweep request itself. Protection rules belong in
permissions and hooks, not prose: CLAUDE.md is guidance, a deny rule is a locked
door ([settings-and-permissions.md](../01-claude-code-basics/settings-and-permissions.md)).

## 5. Publishing & Formatting

| Use case | Best surface | Best mechanism | Difficulty |
|---|---|---|---|
| Organize five years of messy drafts: sort by book, rename to `Title_ChNN_vN`, flag duplicates, delete nothing | Cowork | prompt | Starter |
| Retailer metadata pack: title/subtitle, 7 keywords, category/BISAC suggestions, series fields | Desktop-Chat | prompt | Starter |
| Read your KDP dashboard or proof screenshots and extract the exact numbers (Fable 5 vision) | Desktop-Chat | prompt | Starter |
| Markdown manuscript → properly styled Word (.docx) submission file via the document skills | CLI / Cowork | skill | Intermediate |
| Front matter / back matter generation per retailer (copyright page, also-by, newsletter plug) | CLI | skill | Intermediate |
| Compile scene files into a single ordered manuscript with scene-break normalization | CLI | prompt (scripted) | Intermediate |
| Publication-day checklist as a user-only skill — never fires accidentally mid-draft | CLI | skill | Intermediate |
| ARC reviewer tracker: real .xlsx with working formulas that flag overdue follow-ups | Cowork | prompt | Starter |
| PDF proof QA: render the PDF to images and visually verify layout before upload | CLI | skill | Power |
| Backlist re-formatting batch dispatched as a background session you monitor from one screen | CLI | subagent (background session) | Power |
| ⚠️ EPUB generation/validation directly in Claude (no EPUB tooling is documented in this wiki's feature docs; route via .docx → Vellum/Calibre, or script `pandoc`/`epubcheck` yourself) | CLI | prompt (scripted) | Power |
| ⚠️ Vellum-specific automation (Vellum has no documented API/MCP; file-level workarounds only) | CLI | skill | Power |

**Standouts and gotchas.** Cowork is the publishing-ops hero for non-terminal
authors: real deliverables — formatted Word docs, working spreadsheets, organized
folders — saved straight to disk. Always point it at a *copy* until you trust a
workflow, and keep "Ask before acting" on. The two ⚠️ rows are honest gaps: EPUB and
Vellum jobs work today only by driving external tools through shell commands, which
is Power-user territory. Deep dive: [publishing-ops.md](../03-author-workflows/publishing-ops.md).

## 6. Marketing & Launch

| Use case | Best surface | Best mechanism | Difficulty |
|---|---|---|---|
| Back-cover blurb iteration in an Artifact — versions stack, flip between them, copy the winner | Desktop-Chat / web | Artifact | Starter |
| Ad copy variant sets (Meta, Amazon) generated from blurb + comps, labeled for A/B testing | Desktop-Chat | prompt | Starter |
| Launch email sequence drafted inside a Project that already knows the book and your voice | web / Desktop-Chat | Project | Starter |
| Cover-comp visual trend read: drop 10 subgenre cover screenshots, get the conventions you must hit | Desktop-Chat | prompt | Starter |
| Newsletter analytics summary: drop the platform CSV export, get open/click trends and three concrete recommendations | Cowork / Desktop-Chat | prompt | Starter |
| Blurb-writer skill encoding your hook-stakes-twist formula, two labeled variants every time | CLI / Code tab | skill | Intermediate |
| Query-letter formatter with arguments: `/query-letter "Saltwater Crown" 92000 fantasy` | CLI | skill | Intermediate |
| Comp-title positioning memo: one subagent per comp researches blurb structure, tropes, review themes; a closer synthesizes | CLI | subagent | Intermediate |
| ARC/launch packet: back-matter page + ARC email + three social captions from the finished manuscript, voice-matched | CLI | skill | Intermediate |
| "Chapter 12 revised, ready for beta" posted automatically to your ARC/accountability Slack channel | CLI | MCP | Intermediate |
| Series marketing page: reading order, cross-book hooks, box-set blurb from the full series text | CLI | prompt | Intermediate |
| Blurb tournament: three subagents draft from different angles (character-, stakes-, voice-first); a fourth judges against your subgenre's top blurbs | CLI | subagent | Power |
| Pen-name brand audit: bio consistency, name collisions, voice drift across retailer pages and socials | CLI | subagent | Power |
| Launch-week war room: a scheduled Cowork task updates the checklist status every morning | Cowork | prompt (scheduled task) | Power |

**Standouts and gotchas.** Artifacts are the right tool for any short copy you'll
iterate ten times — blurbs, taglines, bios; don't burn Code-session tokens on them.
The comp-research fan-out is the highest-value subagent pattern in marketing
(breadth-first web research is exactly what multi-agent setups excel at), but it's
also the most token-hungry — budget for it. Carlo-style note: a full marketing suite
(blurbs → email → ads → series) is exactly the kind of thing that graduates from
prompts into a family of skills. Deep dive:
[marketing-and-launch.md](../03-author-workflows/marketing-and-launch.md).

## 7. Research

| Use case | Best surface | Best mechanism | Difficulty |
|---|---|---|---|
| Quick period/craft fact-check mid-draft without leaving the session (built-in web search) | CLI / Desktop-Chat | prompt | Starter |
| Research chat that can see your Google Drive / Notion notes | web / Desktop-Chat | MCP (connectors) | Starter |
| Pull a craft essay or comp description into a planning session as clean text | CLI | MCP (fetch) | Starter |
| Extract structured facts from a scanned document, old map, or handwritten research page | Desktop-Chat | prompt | Starter |
| Build a reusable era/location detail dossier (sensory details, idiom, prices, travel times) saved as project notes | CLI | prompt | Starter |
| Search your Obsidian research vault: "everything tagged #lighthouse-research, give me sensory details for scene 3" | CLI | MCP | Intermediate |
| Read-only research vault: `/add-dir` your vault, deny all edits to it | CLI | prompt (permission rules) | Intermediate |
| Genre/market deep-dive: parallel subagents map reader expectations, tropes, and opportunities; one synthesis report | CLI | subagent | Power |
| Closed-world mode: deny `WebFetch` and `Bash(curl *)` so a project's worldbuilding stays purely internal | CLI | prompt (permission rules) | Power |

**Standouts and gotchas.** The Obsidian-vault connection is the sleeper hit — your
vault is just Markdown, so even the plain filesystem route works with zero extra
setup. One Fable 5-specific note for thriller and SF writers: questions about
hacking or engineered plagues can trip the safety classifiers and get answered by
Opus 4.8 instead — it's labeled, expected, and still a top-tier answer, not a bug
([fable-5-model-guide.md](../../fable-documentation/fable-5-model-guide.md)).
Deep dive: [research-and-worldbuilding.md](../03-author-workflows/research-and-worldbuilding.md).

## 8. Author Business & Admin

| Use case | Best surface | Best mechanism | Difficulty |
|---|---|---|---|
| Royalty CSV analysis: drop KDP/D2D/Kobo exports, get per-title and per-platform monthly trends | Cowork | prompt | Starter |
| Contract or retailer-terms plain-language explanation — clause by clause, flagging what to ask a professional about (**not legal advice**; have a lawyer review anything you sign) | Desktop-Chat | prompt | Starter |
| "Find the editorial letter my editor emailed in March" | web / Desktop-Chat | MCP (Gmail connector) | Starter |
| Submission/query tracker spreadsheet: agents, dates, status, nudge dates | Cowork | prompt | Starter |
| Deadline and promo-date calendar management across pen names | web / Desktop-Chat | MCP (Calendar connector) | Starter |
| Consolidated royalty dashboard .xlsx with working formulas across all platforms | Cowork | prompt | Intermediate |
| Tax-season expense categorization from a receipts/statements folder | Cowork | prompt | Intermediate |
| Backlist metadata audit: one subagent per book checks keywords, categories, and blurb freshness; one report | CLI | subagent | Intermediate |
| Session-end word-count logging to an Airtable writing log, fired automatically | CLI | MCP + hook | Power |
| Weekly word-count and progress report that runs in the cloud on a timer, even with the laptop off | CLI | prompt (routine) | Power |
| Pen-name P&L snapshot: combine royalty CSVs with an ad-spend export, per-book profitability table | Cowork | prompt | Intermediate |

**Standouts and gotchas.** This is the category authors forget — and where Cowork's
"real spreadsheet with working formulas" capability pays for itself fastest. The
contract-explanation use case is genuinely useful for orientation but is **not legal
advice**: use it to arrive at your lawyer's office with better questions, not to
skip the lawyer. Privacy note for ghostwriters and NDA work: all Fable 5 traffic is
retained for 30 days for safety monitoring (not used for training) — factor that in
or use another model for sensitive material.

## 9. Teaching & Community

| Use case | Best surface | Best mechanism | Difficulty |
|---|---|---|---|
| Draft course lessons from your own real workflow transcripts (`/export` a session, turn it into a lesson) | CLI | prompt | Starter |
| Conference-talk prep: outline, slide notes, and demo script in a Project holding your past talks and voice samples | Desktop-Chat | Project | Starter |
| FAQ and handout generation from a folder of recorded-Q&A transcripts | Cowork | prompt | Starter |
| Newsletter teaching-tips column drafted in a Project that knows your course catalog | web | Project | Starter |
| Package your blurb/revision process as a skill folder and share it with students (zip or git) | CLI | skill | Intermediate |
| Workshop critique batches: one subagent per student submission, parallel, consistent rubric, separate reports | CLI | subagent | Intermediate |
| Live-demo safety rig: plan mode plus deny rules so an on-stage session cannot touch real files | CLI | prompt (plan mode + permission rules) | Intermediate |
| Cohort starter kit: a repo with shared CLAUDE.md, `.mcp.json`, permission rules, skills, and hooks — students clone one setup | CLI | Project (shared repo) | Power |
| Publish your course skills as an installable plugin marketplace (`/plugin marketplace add you/your-skills`) | CLI | skill (plugin) | Power |

**Standouts and gotchas.** The cohort starter kit is the teaching pattern with the
most leverage: a committed `.mcp.json` plus project skills means every student gets
an identical, working setup on day one (Claude Code prompts them once to approve the
repo's servers and skills — by design). If you teach AI-assisted authoring, the
skill → plugin path turns your curriculum into something students install rather
than transcribe. Remind students that skills from unknown sources should be audited
like any software ([skills.md](../02-power-features/skills.md)).

---

## Where to start

Brand new to all of this? Do these five, in order — each is a real win in under an
hour, and together they touch every concept you'll need later:

1. **Series-bible Q&A in a Project** (Planning, Starter). Upload your bible to a
   Project on Desktop-Chat and interrogate your own canon. Teaches: Projects,
   persistent context.
2. **Blurb iteration in an Artifact** (Marketing, Starter). Paste a synopsis, refine
   the blurb version by version. Teaches: Artifacts, iterative copy work.
3. **Plan-mode cold read** (Revision, Starter). Open your book folder in the Code
   tab or CLI, hit `Shift+Tab` to plan mode, ask for a structural critique. Teaches:
   Claude Code, permission modes, safe read-only analysis.
4. **Cowork folder cleanup** (Publishing, Starter). Point Cowork at a *copy* of your
   messiest drafts folder and have it sort, rename, and report. Teaches: agentic
   file work, approval flow.
5. **Your first skill: a blurb-writer** (Marketing, Intermediate). Follow the
   five-minute walkthrough in [skills.md](../02-power-features/skills.md). Teaches:
   the mechanism behind every repeatable workflow in this catalog.

From there, the deep dives take over:
[drafting-and-revision.md](../03-author-workflows/drafting-and-revision.md) ·
[publishing-ops.md](../03-author-workflows/publishing-ops.md) ·
[marketing-and-launch.md](../03-author-workflows/marketing-and-launch.md) ·
[research-and-worldbuilding.md](../03-author-workflows/research-and-worldbuilding.md)

## Sources

This catalog is a synthesis document: every use case was checked against the
feature documentation in this wiki (which carries its own official-source
citations), all accessed 2026-06-10:

- [which-tool-when.md](../00-start-here/which-tool-when.md) — surfaces, Cowork,
  Dispatch, cloud sessions, capability matrix
- [claude-desktop.md](../02-power-features/claude-desktop.md) — Cowork deliverables,
  scheduled tasks, Code tab, Projects/Artifacts, connectors
- [skills.md](../02-power-features/skills.md) — skill anatomy, invocation control,
  arguments, plugins/marketplaces
- [hooks.md](../02-power-features/hooks.md) — PreToolUse/PostToolUse/SessionStart/
  Stop/FileChanged events, backup/protection/logging patterns
- [subagents-and-orchestration.md](../02-power-features/subagents-and-orchestration.md)
  — parallel sweeps, custom agents, forks, background sessions, routines, token costs
- [mcp.md](../02-power-features/mcp.md) — Notion/Obsidian/Airtable/Slack/Gmail/
  Calendar connections, scopes, shared `.mcp.json`
- [claude-md-and-memory.md](../01-claude-code-basics/claude-md-and-memory.md) —
  CLAUDE.md hierarchy, imports, rules, auto memory
- [settings-and-permissions.md](../01-claude-code-basics/settings-and-permissions.md)
  — permission modes, deny rules, plan mode
- [slash-commands.md](../01-claude-code-basics/slash-commands.md) — /rewind, /export,
  /add-dir, /fork-adjacent commands
- [fable-5-model-guide.md](../../fable-documentation/fable-5-model-guide.md) —
  1M context, vision, long-horizon work, classifier fallback, 30-day retention
- ⚠️ Unverified items are marked inline: EPUB generation/validation tooling and
  Vellum automation have no documented support in the feature docs above; both rows
  describe shell-scripted workarounds, not built-in capabilities.
