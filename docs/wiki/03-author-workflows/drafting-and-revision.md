# Drafting and Revision: Running a Novel Through Claude Code

> **In plain words:** This is the deep-dive on using Claude Code with Fable 5 to
> draft and revise a novel — not "AI, write my book," but a repeatable production
> loop where Claude drafts from *your* story bible, audits its own output, and you
> stay the author of record. Everything here builds on plain folders and text
> files; the feature docs explain each tool, this page wires them into a workflow.

## What it is

A drafting-and-revision workflow is the difference between chatting with an AI
about your book and running a **pipeline**: the same stages, in the same order,
for every chapter — plan, draft, audit, revise, QA, log continuity. Claude Code
suits this because your manuscript is just files in a folder, and every feature
maps to a stage:
[CLAUDE.md](../01-claude-code-basics/claude-md-and-memory.md) holds your voice
rules, [skills](../02-power-features/skills.md) package each stage's procedure,
[subagents](../02-power-features/subagents-and-orchestration.md) run audits in a
clean context (a fresh reader who never saw the drafting conversation),
[hooks](../02-power-features/hooks.md) enforce backups and QA gates every single
time, and [Fable 5](../../fable-documentation/fable-5-model-guide.md) supplies
the stamina for long multi-stage jobs.

The honest framing up front: AI drafts are raw material. The workflows below
exist so that *more* of your judgment gets applied, more systematically — not
less.

## Why authors care

- **Consistency per chapter.** Chapter 23 gets the same planning, the same audit
  checklist, and the same continuity sweep as chapter 1.
- **A story bible the AI actually uses.** Claude reads your dossier *before*
  drafting, instead of inventing eye colors mid-scene.
- **Audits without bias.** A subagent that critiques chapter 12 never saw you
  draft it, so it reads like a beta reader, not like a co-conspirator.
- **Your originals are physically safe.** Deny rules and hooks make "Claude
  overwrote my only copy" impossible, not just unlikely.
- **Series-scale continuity becomes routine** instead of a dreaded month of
  spreadsheet work.

## Getting started

Set up a book project folder for AI-assisted work. (Full background:
[CLAUDE.md & memory](../01-claude-code-basics/claude-md-and-memory.md) and
[settings & permissions](../01-claude-code-basics/settings-and-permissions.md) —
this section just applies them.)

1. **Create the layout.** In Terminal (same command works in PowerShell with
   the folders listed out):

   ```bash
   mkdir -p ~/Documents/hollow-crown/{chapters,drafts,originals,bible,reports,backups}
   cd ~/Documents/hollow-crown
   ```

   `chapters/` holds current working chapters (`ch01.md`…); `drafts/` is
   scratch space where Claude works freely; `originals/` is the untouchable
   archive (pre-AI text, published versions); `bible/` is the story
   bible/dossier (next section); `reports/` receives audit reports;
   `backups/` receives timestamped copies via a hook.

2. **Start Claude Code and initialize memory:** run `claude`, then `/init`, then
   edit `CLAUDE.md` so the top is a **voice firewall**:

   ```markdown
   ## Voice and style (do not homogenize)
   - Close third, past tense. My fragments and comma splices are deliberate — keep them.
   - Do not "improve" my rhythm, smooth my dialect spellings, or standardize
     my punctuation. When in doubt, preserve the original phrasing.
   - Em dashes: max ~1 per 1,000 words.

   ## Files
   - originals/ is read-only. Work in drafts/; I promote files to chapters/ myself.
   - Story bible: @bible/dossier.md

   ## Workflow
   - "Continuity pass" = check chapter against bible/, report findings BEFORE editing.
   ```

3. **Enforce the file rules** (CLAUDE.md is guidance; this is the lock). Ask
   Claude: *"Add permission rules to this project's settings: deny all edits to
   `originals/` and `bible/canon.md`, allow edits in `drafts/` and `reports/`."*
   Verify with `/permissions`.

4. **First drafting run.** Switch to plan mode (`Shift+Tab`) and try:

   ```text
   Read bible/dossier.md and chapters/ch11.md. Propose a beat-level plan for
   chapter 12: POV, scene goals, what each scene reveals and withholds, where
   it ends. Don't draft yet — I want to approve the plan first.
   ```

   Approve or adjust, exit plan mode, then: *"Draft chapter 12 from the
   approved plan into drafts/ch12-draft1.md. Follow the voice rules in
   CLAUDE.md exactly."*

That's the minimum viable loop: bible → plan → approve → draft into `drafts/`.
The rest of this page hardens and extends it.

## Story bibles as AI-facing dossiers

A traditional story bible is written for *you*. An **AI-facing dossier** is the
same material reorganized for a reader with no intuition: explicit, structured,
and ruthless about what must never be contradicted. Claude drafts from what's on
the page of the dossier — not from what you meant. A workable split inside
`bible/`:

- `dossier.md` — the loader: premise, cast one-liners, current book state, links
  to the rest. This is what CLAUDE.md imports.
- `canon.md` — hard facts that must never drift (names, dates, eye colors,
  geography, magic/tech rules). Protect it with a deny rule.
- `voice.md` — prose-level rules with *examples* of your sentences, good and bad.
- `arcs.md` — each character's emotional position per chapter; what they want
  vs. what they'd never admit.
- `continuity-log.md` — append-only: one entry per finished chapter (see the
  production loop below).

Two refinements worth knowing about, both generic techniques you can apply with
plain markdown files:

- **Constraint- and tension-based dossiers.** Instead of describing what
  *happens*, document the forces: what each character cannot do, which tensions
  must stay unresolved until when. Constraints steer an AI better than
  summaries — a summary says what already happened; a constraint says what the
  next scene is *allowed* to do. Carlo's **NPE (Narrative Physics Engine)**
  method is a worked-out system of exactly this — story modeled through
  constraints, tension axes, and narrative "gravity" — packaged in his skill
  library as `npe-worksheet` and `story-dossier`.
- **The ghost draft: documenting the implied layer.** Most dossiers record what
  the reader is shown. A ghost-draft file records what is *implied but never
  stated* — off-page history, what characters know but won't say, the power
  dynamics under polite dialogue. This is the biggest single lever for
  show-don't-tell: an AI that knows the subtext can write a scene *around* it
  instead of announcing it. Generic version: add `bible/ghost.md` with sections
  like "What X believes but never says," "Scenes that happened off-page,"
  "What the reader should suspect by ch. 20." Packaged version: Carlo's
  `ghost_draft` skill.

You don't need those skills to use the techniques — a hand-written constraints
file and ghost file already outperform a prose-summary bible.

## The chapter production loop

The repeatable cycle, and which feature carries each stage:

| Stage | What happens | Feature that carries it |
|---|---|---|
| 1. Plan | Beat-level chapter plan from the dossier; you approve | Plan mode; a `chapter-plan` skill |
| 2. Draft | Draft into `drafts/`, voice rules enforced | CLAUDE.md voice firewall; a `chapter-draft` skill |
| 3. Audit | Continuity, repetition, style, and craft checks — each by a **subagent with clean context** | Custom subagents, run in parallel |
| 4. Revise | One revision consolidating audit findings you accepted | Main session; `acceptEdits` mode once agreed |
| 5. Final QA | Gate: did every audit pass? Blocks "done" if not | A `Stop`/QA hook, or a final checklist skill |
| 6. Continuity summary | Append new facts to `bible/continuity-log.md` | A `bible-update` skill |

Why subagents for stage 3: the drafting conversation is contaminated — Claude
just wrote the chapter and will defend it. A subagent starts blank, reads only
the chapter and the bible, and reports like an outside editor. Run the audits in
parallel; each writes to `reports/` (subagents share no memory — files are the
hand-off). Why a hook for stage 5: a checklist in a prompt is advisory; a hook
is deterministic. A `Stop` hook can refuse to let the session declare a chapter
finished until `reports/` contains a passing audit (worked example in Advanced).

Each stage's prompt, once stable, becomes a [skill](../02-power-features/skills.md)
(`/chapter-plan`, `/chapter-audit`…), and the whole loop becomes one
orchestrating prompt. Packaged end-to-end versions exist in Carlo's library as
`chapter-production-workflow` and `novel-production-loop` — the same stages,
hardened over many books.

## Author use cases

1. **Cold-read critique in plan mode.** `Shift+Tab` to plan mode, then: *"Read
   drafts/ch07-draft2.md as a first-time reader. Report where you were confused,
   bored, or unconvinced — with line references — before suggesting any fixes.
   Do not propose edits yet."* Plan mode guarantees zero stray edits while you
   argue with the critique.
2. **Multi-lens subagent critique.** *"Read chapter 14 with three subagents in
   parallel: one as a devoted romance reader judging emotional beats, one as a
   thriller reader judging pacing, one tracking only the timeline against
   bible/canon.md. Write each report to reports/ and give me a one-paragraph
   summary of each."* Clean contexts mean the lenses can't bleed into each other.
3. **Prose audit for AI-isms and tics.** *"Audit drafts/ch12-draft1.md for:
   filter words (saw, felt, noticed, realized), echo words repeated within 300
   words, 'not X but Y' constructions, and paragraphs that tell an emotion the
   scene already shows. Table with line numbers; change nothing."* Recurring
   version → package as a skill; Carlo's library has `ai-ism-helper`,
   `eqbench-js`, and `better-pwa-analyst` as worked examples.
4. **Em-dash and punctuation-tic reduction.** *"Count every em dash in
   chapters/ch01-ch10, classify by use (interruption, aside, appositive…), and
   propose a reduction plan to ~1 per 1,000 words that touches the weakest
   instances first. Show me the plan before changing anything."* (Packaged
   example: `em-dash-tightening`.)
5. **Voice-preservation pass.** When asking for line edits, pair the CLAUDE.md
   voice firewall with an explicit in-prompt instruction: *"Line-edit for
   clarity only. Do not homogenize my voice: keep fragments, keep comma
   splices, keep dialect spellings. List every change with a one-line reason."*
   Belt and suspenders: the backup hook (Advanced) means any pass is reversible.
6. **Per-chapter continuity sweep.** *"Spawn one subagent per chapter in
   chapters/. Each checks its chapter against bible/canon.md and
   bible/continuity-log.md and writes findings to reports/continuity-chNN.md.
   Then compile reports/continuity-summary.md."* Save the checker as a custom
   agent (file in Advanced) and this becomes one sentence per draft cycle.
7. **Whole-manuscript single-run audit (Fable 5).** This is what Fable 5's
   long-horizon capability changes: with a 1M-token context (roughly 500k+
   words) and the stamina to plan across stages, *"Read all 28 chapters plus
   the bible, build the timeline, and fix every dated reference"* is realistic
   as **one run** instead of a fan-out — and Fable 5 benefits unusually strongly
   from keeping working notes in a file (`revision-notes.md`) as it goes. See
   the [Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).
8. **External story bible via MCP.** If your bible lives in Notion or an
   Obsidian vault, connect it with [MCP](../02-power-features/mcp.md) and the
   same prompts work: *"Before drafting, fetch the timeline page from my
   Notion bible."*

## Common pitfalls

- **AI drafting is weakest exactly where novels live or die.** Expect emotional
  beats stated instead of dramatized, scene rhythms that repeat
  chapter-to-chapter, conflict that resolves too cleanly, and a drift toward
  generic "good prose" that sands off your voice. The loop catches much of this
  mechanically (audits, ghost-draft subtext, voice firewall) — but no pipeline
  replaces your read. Plan to touch every paragraph.
- **You review everything, always.** Continuity audits miss things; critiques
  can be confidently wrong; a "fixed" timeline can introduce a new error. Treat
  every agent report as a junior editor's memo: useful, checkable, not final.
- **Manuscript-scale work costs real usage.** Subagents run roughly **4× the
  tokens of a plain chat**, multi-agent fan-outs around **15×** (Anthropic's own
  engineering numbers). A 40-chapter parallel sweep is a heavy day against plan
  limits. Fable 5 burns usage faster still ($10/$50 per million tokens on the
  API; included free on paid plans only through June 22, 2026, then usage
  credits). Use Fable 5 for long-horizon jobs; route bulk mechanical checks to
  Haiku-tier subagents.
- **Don't fan out dependent chapters.** If revising chapter 12 depends on what
  changes in chapter 11, parallel agents will contradict each other. Parallel
  for independent audits; sequential for cascading revisions.
- **Long sessions blur.** After compaction, conversational nuance fades. Rules
  that matter live in CLAUDE.md (re-read from disk), not in chat. `/clear`
  between unrelated chapters beats one marathon session.
- **A bloated dossier backfires.** Importing a 40k-word bible via `@` eats the
  context your chapters need. Keep `dossier.md` short; let agents read the
  deep files on demand.

## Advanced

A complete worked pipeline you can adapt. All four artifacts plus the
orchestrating prompt.

### Directory tree

```text
hollow-crown/
├── CLAUDE.md                    # voice firewall, file rules, @bible/dossier.md
├── .claude/
│   ├── settings.json            # deny Edit(originals/**), hooks registration
│   ├── hooks/
│   │   └── backup-chapter.sh
│   ├── skills/
│   │   └── chapter-audit/SKILL.md
│   └── agents/
│       └── continuity-checker.md
├── bible/
│   ├── dossier.md  canon.md  voice.md  arcs.md  ghost.md  continuity-log.md
├── chapters/        ch01.md … ch12.md
├── drafts/          ch12-draft1.md  ch12-draft2.md
├── originals/       (read-only archive)
├── reports/         continuity-ch12.md  style-ch12.md  …
└── backups/         ch12-20260610-141502.md
```

### Chapter-audit skill — `.claude/skills/chapter-audit/SKILL.md`

```yaml
---
name: chapter-audit
description: Runs the four-part audit (continuity, repetition, style, craft) on a draft chapter and writes reports to reports/. Use when a chapter draft is ready for audit.
disable-model-invocation: true
argument-hint: "[draft-file]"
---

Audit $0 using four parallel subagents, each writing to reports/:

1. Continuity — use the continuity-checker agent against bible/canon.md
   and bible/continuity-log.md.
2. Repetition — echo words within 300 words, repeated sentence openers,
   reused imagery from the previous two chapters.
3. Style — violations of bible/voice.md; filter words; em-dash count vs.
   the 1-per-1,000-words budget.
4. Craft — scene goals vs. the approved plan; told-not-shown emotions;
   check each scene against bible/ghost.md: is the subtext present
   without being stated?

Each report: numbered findings with line references. No prose rewrites.
Finish with a one-screen summary table: PASS/FAIL per audit.
```

`disable-model-invocation: true` means only *you* fire it (`/chapter-audit
drafts/ch12-draft1.md`) — never mid-draft on Claude's initiative.

### Backup hook — `.claude/hooks/backup-chapter.sh`

```bash
#!/bin/bash
# Timestamped copy of any edited chapter or draft, before you ever need it.
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
case "$FILE_PATH" in
  */chapters/*|*/drafts/*)
    mkdir -p "$CLAUDE_PROJECT_DIR/backups"
    B=$(basename "$FILE_PATH")
    cp "$FILE_PATH" "$CLAUDE_PROJECT_DIR/backups/${B%.*}-$(date +%Y%m%d-%H%M%S).${B##*.}"
    ;;
esac
exit 0
```

Registered in `.claude/settings.json` under `PostToolUse` with matcher
`Edit|Write` (`chmod +x` it first; needs `jq` — `brew install jq`). For the QA
gate, add a `Stop` hook of `"type": "prompt"` asking *"Does reports/ contain a
PASS summary for the chapter just revised? If not, block with the missing
audits."* — exact JSON shapes in [hooks](../02-power-features/hooks.md).

### Continuity-checker subagent — `.claude/agents/continuity-checker.md`

```markdown
---
name: continuity-checker
description: Checks a draft chapter against bible/canon.md and bible/continuity-log.md for contradictions. Use proactively after any chapter is drafted or revised.
tools: Read, Grep, Glob, Write
model: haiku
---

You are a continuity editor for a fiction series. Compare the chapter you
are given against bible/canon.md and bible/continuity-log.md. Report
contradictions in character details, timeline, geography, injuries,
who-knows-what, and established world rules. Cite chapter line and bible
entry for each finding. Write the full report to reports/ as instructed;
return only a numbered summary. Never rewrite prose.
```

`model: haiku` keeps the sweep cheap; `tools` limited to read + report-writing
means it physically cannot touch the manuscript.

### The orchestrating prompt

With the pieces in place, one chapter through the whole loop is a single
message in your main session:

```text
Run chapter 12 through the full loop:

1. PLAN — read bible/dossier.md, bible/arcs.md, bible/ghost.md, and
   chapters/ch11.md. Give me a beat plan for ch12 and STOP for my approval.
2. DRAFT — after approval, draft to drafts/ch12-draft1.md per CLAUDE.md voice rules.
3. AUDIT — /chapter-audit drafts/ch12-draft1.md
4. REVISE — show me the audit summaries; I'll mark which findings to apply.
   Apply only those to drafts/ch12-draft2.md.
5. QA — re-run only the audits that failed, on draft2. All PASS required.
6. LOG — append new canon facts and character-state changes from the final
   draft to bible/continuity-log.md, then tell me it's ready to promote.

Never write into chapters/ — I promote drafts myself.
```

The two human gates (approve the plan, choose which findings to apply) are the
point: the pipeline automates the drudgery, not the decisions. On Fable 5 this
runs comfortably as one session; on smaller models, expect to `/clear` between
stages 2 and 3.

### Scaling to a series

Put a series-level `CLAUDE.md` and `bible/` one folder above the per-book
folders — Claude Code walks up the tree and loads both. Give the
continuity-checker `memory: project` so it accumulates series quirks across
sessions ([subagents](../02-power-features/subagents-and-orchestration.md),
frontmatter table). And cross-book audits are the flagship Fable 5 job: a
trilogy plus its bible fits the 1M context, so "reconcile the bible against
what books 1–3 actually say" becomes one long-horizon run instead of a
re-stitched fan-out.

## Sources

This page is a synthesis; platform facts were verified in the linked feature
docs against official sources (all accessed 2026-06-10):

- [skills.md](../02-power-features/skills.md) — skill anatomy, frontmatter,
  invocation (via https://code.claude.com/docs/en/skills)
- [hooks.md](../02-power-features/hooks.md) — PostToolUse/Stop events, exit
  codes, prompt-type hooks, backup pattern (via https://code.claude.com/docs/en/hooks)
- [subagents-and-orchestration.md](../02-power-features/subagents-and-orchestration.md)
  — agent file format, clean-context behavior, `memory` field, 4×/15× token
  multipliers (via https://code.claude.com/docs/en/sub-agents and
  https://www.anthropic.com/engineering/multi-agent-research-system)
- [claude-md-and-memory.md](../01-claude-code-basics/claude-md-and-memory.md) —
  CLAUDE.md locations, `@` imports, upward folder walking, compaction
  (via https://code.claude.com/docs/en/memory)
- [settings-and-permissions.md](../01-claude-code-basics/settings-and-permissions.md)
  — deny rules, plan mode, `acceptEdits` (via https://code.claude.com/docs/en/permissions)
- [fable-5-model-guide.md](../../fable-documentation/fable-5-model-guide.md) —
  1M context, long-horizon claims, pricing, free window through 2026-06-22
  (via https://www.anthropic.com/news/claude-fable-5-mythos-5 and platform docs)
- ⚠️ Unverified by nature: NPE, ghost draft, and the named skills
  (`npe-worksheet`, `story-dossier`, `ghost_draft`,
  `chapter-production-workflow`, `novel-production-loop`, `ai-ism-helper`,
  `em-dash-tightening`, `eqbench-js`, `better-pwa-analyst`) describe Carlo's
  methods and installed library — author-craft guidance, not platform fact.
