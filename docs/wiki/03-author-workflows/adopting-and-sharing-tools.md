# Adopting, Sharing, and Building Author Tools

> **In plain words:** Authors increasingly swap tools with each other — a chapter-audit
> skill, a blurb pipeline, a series-bible script. This page covers the full loop:
> how to safely *adopt* a tool another author built (without inheriting their pen name
> and folder layout), how to *share* yours back without leaking personal data, and a
> simple ladder for deciding what an idea of your own should *become* — a prompt, a
> skill, a script, an MCP server, or a small app.

## What it is

Every author tool — whether it's a folder of prompts or a full repo — is really three
layers stacked together:

| Layer | What lives there | Example |
| :--- | :--- | :--- |
| **Engine** | Generic logic any author could use unchanged | "Audit each chapter against the outline and report drift" |
| **Conventions** | Genre or workflow defaults a user might reasonably swap | "Romance beats per Save the Cat", "chapters live in `manuscript/`" |
| **Personal** | Names, paths, voice, pen names — things that are *you* | "Pen name: J.R. Hale", `/Users/jana/books/`, voice samples |

Tools break when they travel because the personal layer is welded to the engine. The
original author's pen name is hardcoded in a prompt; their laptop's file paths are
baked into a script. The method on this page uses Claude itself to find those welds,
separate the layers, and make the tool portable — both when you adopt someone else's
tool and before you publish your own.

This is a working method developed in the indie-author community, not an Anthropic
feature — but it leans on Claude Code's strengths: reading a whole repo quickly and
refactoring it on instruction.

## Why authors care

- **Adopt faster.** Another author's chapter pipeline can work for you in an hour
  instead of an afternoon of "why does it keep calling me Brenda?"
- **Stop leaking.** Pen names, real names, draft excerpts, and API keys have all been
  accidentally published in shared author tools. A scrub pass catches them.
- **Survive updates.** When the original author improves their tool, a delta log lets
  you take the update without losing your customizations.
- **Build the right size of thing.** Most tool ideas should stay prompts. The decision
  ladder below stops you from building an app when a 40-line skill would do.

## Getting started

First win: interrogate a tool you just downloaded, before you run anything.

1. Get the tool's folder onto your machine (download ZIP from GitHub, or however the
   author shared it).
2. Open a terminal in that folder (macOS: open Terminal, type `cd `, drag the folder
   in, press Return; Windows: same idea in PowerShell) and run `claude`.
3. Paste this:

   ```text
   I just downloaded this author tool from another writer. Before I use it,
   interrogate it for me. Read through the files and answer:

   1. What does this tool actually do, in plain words?
   2. What does it assume about its author? (genre, pen names, file layout,
      operating system, installed software, subscriptions, writing process)
   3. What is hardcoded that should be configurable? List every personal name,
      file path, email, API key, genre default, and voice/style assumption —
      with the file it lives in.
   4. What would break first if I ran it as-is on my machine?

   Do not change anything yet. Give me the report first.
   ```

4. Read the report. You now know what the tool *is* and what it *assumes* — without
   having read a single file yourself.

## The three-phase adoption method

### Phase 1 — Intake interrogation

That's the prompt above. The principle: **never read a stranger's repo manually.**
Claude reads it and reports what it assumes about you. The two questions that matter
most are *"what does it assume about me?"* and *"what's hardcoded?"* — everything
else in adoption flows from those answers.

For large repos, this is a good job for a subagent so the file-reading doesn't bloat
your main session — see
[Subagents: Let Claude Delegate Work to Copies of Itself](../02-power-features/subagents-and-orchestration.md).

### Phase 2 — Cleanup and layer separation

Now sort everything the interrogation found into the three layers, and pull the
personal layer out into one file.

```text
Using your intake report, separate this tool into three layers:

- ENGINE: generic logic any author could use unchanged
- CONVENTIONS: genre or workflow defaults a user might reasonably swap
  (beat structure, folder names, chapter length targets)
- PERSONAL: names, pen names, paths, voice samples, contact info —
  anything that is the original author rather than the tool

For each file (or section of a file), tell me which layer it belongs to.
Then propose a cleanup plan: every PERSONAL item moves into a single
PROFILE.md at the tool's root, and the rest of the tool reads values from
PROFILE.md instead of hardcoding them. Show me the plan before editing,
then execute it file by file.
```

`PROFILE.md` is just a plain Markdown file of labeled values — pen name, genre,
manuscript folder, voice notes. One file to edit when the tool changes hands.

### Phase 3 — Portability re-architecture

Make the tool installable by a *stranger* — including future-you on a new machine.

```text
Re-architect this tool for portability:

1. Confirm PROFILE.md now holds every personal value, with a placeholder
   example for each (e.g. "Pen name: [YOUR PEN NAME — e.g. J.R. Hale]").
2. Confirm no engine or convention file contains a hardcoded personal value.
3. Write ADAPTING.md — a self-onboarding interview. It should instruct a NEW
   user's Claude to: ask the user one question per PROFILE.md value, explain
   why each value matters, fill in PROFILE.md from the answers, and finish
   with a smoke test that proves the tool works for them.
4. Create CUSTOMIZATIONS.md — a dated delta log. From now on, every change I
   make versus the original gets one dated entry: what changed, which file,
   and why. Start it with today's date and "adopted from [source]".

Work file by file and show me diffs as you go.
```

The three companion files, in one line each:

- **`PROFILE.md`** — every user-specific value, in one place, with placeholders.
- **`ADAPTING.md`** — the interview a new user's Claude runs to configure the tool
  for them. Their first prompt is just: *"Read ADAPTING.md and onboard me."*
- **`CUSTOMIZATIONS.md`** — the dated log of every change you made from the original,
  so when the original author ships an update you can re-apply your changes cleanly
  (see [Advanced](#advanced)).

## Sharing it back: scrub before reshare

Before you publish a tool — yours or your adapted copy of someone else's — run a
scrub pass. Personal data hides in odd places: example prompts, test files, screenshots,
git history.

```text
I want to publish this tool publicly for other authors. Run a scrub pass:

1. Search every file for: my real name, pen names, email addresses, file
   paths containing my username, API keys or tokens, manuscript excerpts,
   character names from my books, and private notes.
2. Replace each with a neutral placeholder, and confirm PROFILE.md is the
   only file that ever held personal values.
3. If this folder is a git repository, check whether any of those values
   appear in past commits — committed-then-deleted secrets are still in
   the history. Tell me what you find before changing anything.
4. Verify ADAPTING.md works from a blank PROFILE.md, then give me a final
   "safe to publish" checklist with anything still outstanding.
```

If a real secret (an API key) ever made it into git history, treat it as exposed:
revoke and replace the key. Rewriting history is not enough on its own.

## The decision ladder: prompt → skill → script → MCP → app

The other half of the loop: you have an idea for a tool of your own. Climb only as
high as the idea forces you. Each rung costs more to build and maintain than the last.

### Rung 0 — Stays a prompt

**When:** you do it occasionally, it fits in one message, and the wording barely
matters. **Example:** "Give me three sharper hooks for this blurb." Don't build
anything. Keep a notes file of prompts you like if you want.

### Rung 1 — Becomes a skill

**When:** you keep re-explaining the same multi-step procedure or checklist, and
Claude's judgment is part of the job. **Examples:** your chapter continuity audit
(12 checks, in order, report format you like); your back-matter assembly procedure;
your beat-sheet review. **Prototype it:** in the project, say *"Turn the procedure I
just described into a skill at `.claude/skills/chapter-audit/SKILL.md` — write the
description so you'll trigger on 'audit this chapter'."* Done in minutes. Full
walkthrough: [Skills: Teach Claude Your Procedures Once](../02-power-features/skills.md).

### Rung 2 — Becomes a script

**When:** the job is mechanical and must come out *identical every time* — counting,
renaming, converting, compiling. No judgment involved. **Examples:** word counts per
chapter into a CSV; stitch `chapters/*.md` into one manuscript file; count em-dashes
per 1,000 words. **Prototype it:** *"Write a small script in `scripts/` that does X;
test it on chapter 3."* Scripts pair naturally with the other rungs: a skill can run
a bundled script instead of re-deriving the logic, and a hook can run one automatically
after every edit (auto-backup, word-count logging) — see
[Hooks: Automatic Guardrails for Your Writing Projects](../02-power-features/hooks.md).

### Rung 3 — Becomes an MCP server

**When:** Claude needs *live access to data or another system*, across many sessions
or surfaces — not a procedure, a connection. **Examples:** a server that exposes your
series bible database so Claude can query character facts mid-draft; a reader for your
Plottr or Aeon Timeline files; your sales dashboard. **Prototype it:** Anthropic ships
an official scaffolding plugin — in Claude Code run
`/plugin install mcp-server-dev@claude-plugins-official`, then
`/mcp-server-dev:build-mcp-server`; Claude interviews you about the use case and
scaffolds a local (stdio) or remote (HTTP) server. Concepts, `claude mcp add`
commands, and scopes: [MCP: Connecting Claude to Your Other Tools](../02-power-features/mcp.md).

### Rung 4 — Becomes a small app

**When:** the users aren't you (or aren't Claude users at all), it needs a visual
interface, or it must run with no AI in the loop. **Examples:** an interactive widget
embedded in your course platform; a timeline viewer your ARC team opens in a browser;
a desktop tool for formatting. **Prototype it:** vibecode it with Claude Code — start
with a single plain HTML file ("make me a one-page app that does X, no frameworks"),
iterate by describing what's wrong, only add complexity when the single file can't
hold it. This is the rung where maintenance becomes real work; make sure rungs 1–3
genuinely don't fit first.

**A side rung — subagent, not tool:** if the idea is really "too much reading for one
chat" (research a genre, read all 40 chapters), it's a delegation problem, not a tool
problem — see [Subagents](../02-power-features/subagents-and-orchestration.md).

## Author use cases

1. **Adopting a friend's drafting pipeline.** Run the Phase 1 interrogation; it reveals
   her romance beat sheet (conventions) and her pen name in six prompts (personal).
   Phases 2–3 give you a `PROFILE.md` with *your* pen name and a thriller beat sheet
   swapped in — engine untouched.
2. **Onboarding without the original author.** You publish your chapter-audit tool with
   `ADAPTING.md`. A stranger downloads it, tells their Claude "read ADAPTING.md and
   onboard me," and is configured in ten minutes — you never answer a support email.
3. **Taking an upstream update.** The original author ships v2 of the tool you adapted
   months ago. Your `CUSTOMIZATIONS.md` lists your nine changes; Claude re-applies
   them to the new version one entry at a time (prompt in [Advanced](#advanced)).
4. **Idea triage on the ladder.** "Check my chapters for POV slips" → skill (judgment,
   repeatable). "Total word count by week" → script (mechanical). "Let Claude query my
   series bible from any project" → MCP server. "Let my ARC team browse the timeline"
   → small app.
5. **Scrubbing before a course release.** You're packaging your tools for students. The
   scrub pass finds your real name in a test file and a manuscript excerpt in an example
   prompt — both replaced with placeholders before upload.

## Common pitfalls

- **Running a downloaded tool before interrogating it.** Skills and scripts can execute
  commands on your machine. Phase 1 doubles as a safety review — ask Claude explicitly
  "does anything here run commands, install software, or send data anywhere?"
- **Skipping `CUSTOMIZATIONS.md` because "I'll remember."** You won't. Without the delta
  log, every upstream update forces a choice between their improvements and your
  customizations.
- **Scrubbing files but not git history.** Deleted ≠ gone. Anything ever committed is
  retrievable from history; check it, and revoke any exposed keys.
- **Over-building.** The most common failure is jumping to rung 3 or 4 when a skill
  would do. Climb the ladder reluctantly.
- **Token cost.** Interrogating a large repo means reading many files; on Fable 5
  ($10 in / $50 out per million tokens) that adds up. Point Phase 1 at the tool's
  folder only (not your whole workspace), and use a subagent for big repos so the raw
  file contents don't sit in your main conversation.
- **Half-separated layers.** If even one engine file still hardcodes a personal value,
  `ADAPTING.md` onboarding silently produces a tool that's part-you, part-stranger.
  Make Phase 3 step 2 (the "no hardcoded personal values" check) a real verification,
  not a formality.

## Advanced

### Suggested portable-tool layout

```text
my-author-tool/
├── README.md            # what it does, for humans browsing the repo
├── PROFILE.md           # ALL personal values, placeholders shipped
├── ADAPTING.md          # self-onboarding interview for a new user's Claude
├── CUSTOMIZATIONS.md    # dated delta log vs. upstream
├── .claude/
│   └── skills/
│       └── <skill-name>/SKILL.md   # engine: procedures
└── scripts/             # engine: deterministic helpers
```

### `CUSTOMIZATIONS.md` entry format and the update prompt

```markdown
## 2026-06-10 — adopted from github.com/originalauthor/chapter-pipeline (v1.3)

## 2026-06-12 — swapped beat structure
- File: .claude/skills/chapter-audit/SKILL.md
- Change: romance beats → thriller beats (see PROFILE.md "genre")
- Why: I write thrillers
```

When upstream ships an update:

```text
I've downloaded v2 of the original tool into ./upstream-v2/. My adapted copy
is in the current folder and CUSTOMIZATIONS.md lists every change I made.
For each entry: check whether it still applies in v2, re-apply it if so,
flag it if v2 made it obsolete or conflicts. Then update CUSTOMIZATIONS.md
with a dated entry for this merge.
```

### Skill frontmatter that matters for shared tools

Verified against code.claude.com docs, 2026-06-10 (full table in
[skills.md](../02-power-features/skills.md#advanced)):

- `description` — the trigger; for a shared tool, write it generically ("audit a
  chapter against its outline"), not in your own shorthand.
- `disable-model-invocation: true` — for side-effect skills (publishing, sending),
  so a new user's Claude can't fire them uninvited.
- `allowed-tools` — pre-approves specific commands while the skill runs; audit this
  field carefully in any tool you adopt.
- Project skills live at `.claude/skills/<skill-name>/SKILL.md` and travel with the
  repo — that's what makes skills the natural unit of sharing. Personal skills at
  `~/.claude/skills/` do *not* travel.

### Sharing an MCP server with a tool

A project-scoped `.mcp.json` committed at the repo root ships the server config with
the tool (`claude mcp add --transport stdio <name> --scope project -- <command>`).
Claude Code prompts the new user for approval before using servers that arrived with
a repo — good; tell your users to expect the prompt, not to fear it. Scopes and
commands: [mcp.md](../02-power-features/mcp.md#advanced).

### Beyond a repo: plugins

If your tool grows to bundle skills + hooks + MCP config together, the next packaging
step up from "a repo with ADAPTING.md" is a Claude Code plugin with a marketplace
entry — see the plugins section of [skills.md](../02-power-features/skills.md#advanced).
The three-layer separation still applies; plugins just formalize the engine layer.

## Sources

- https://code.claude.com/docs/en/skills — skill locations (`.claude/skills/`,
  `~/.claude/skills/`), frontmatter fields (`description`, `disable-model-invocation`,
  `allowed-tools`), commands-merged-into-skills. Accessed 2026-06-10.
- https://code.claude.com/docs/en/mcp — MCP concepts, `claude mcp add` syntax, scopes
  (`local`/`project`/`user`, `.mcp.json`), project-scope approval prompt, and the
  official `mcp-server-dev` plugin (`/plugin install mcp-server-dev@claude-plugins-official`,
  `/mcp-server-dev:build-mcp-server`). Accessed 2026-06-10.
- The three-phase adoption method, three-layer model, and the
  `PROFILE.md`/`ADAPTING.md`/`CUSTOMIZATIONS.md` convention are community practice
  (this wiki's recommended workflow), not an Anthropic specification — file names are
  conventions, not platform requirements.
