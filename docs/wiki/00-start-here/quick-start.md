# Quick Start: Your First 30 Minutes with Claude Code

> **In plain words:** This page takes you from "nothing installed" to "Claude just
> read my chapter and found a continuity error" in about half an hour. Along the
> way it sets up the one book-project folder layout that every other guide in this
> wiki builds on, so you never have to reorganize later.

## What it is

Claude Code is Anthropic's terminal-based AI assistant — a program that runs on
your own computer and can read, edit, and organize the files in a folder you
point it at. For an author, that means it can read your actual manuscript files,
not pasted excerpts: your chapters, your story bible, your blurbs, your research
notes. Think of it as an editorial assistant who has the whole project on their
desk, not just the page you photocopied for them.

A "terminal" is the text-based command window on your computer (Terminal on
macOS, PowerShell on Windows). You type a request in plain English; Claude does
the work and asks permission before changing anything.

This page is the on-ramp. The deep dives — drafting, publishing, marketing,
research — each get their own guide, all linked below.

## Why authors care

- **First win in minutes:** "Read chapter 12 and list continuity errors" works on
  day one, with no setup beyond a folder of files.
- **One folder, whole career:** the layout below holds your manuscript, story
  bible, marketing copy, and retailer-ready files side by side, so every later
  workflow slots in without restructuring.
- **It asks before it touches:** Claude Code shows proposed changes and waits for
  your approval before editing any file.
- **Costs are real and manageable:** usage limits exist on every plan. Read
  [Managing usage and cost](managing-usage-and-cost.md) early — five minutes
  there prevents the most common new-user frustration (hitting a limit
  mid-session and not knowing why).

## Getting started

The 30-minute path: install → open your book folder → set up the canonical
layout → first useful task.

### Minute 0–10: Install and log in

Full install detail (every method, Windows specifics, troubleshooting) lives in
[Installation & setup](../01-claude-code-basics/installation-setup.md). The short
version, verified against the official docs on 2026-06-10:

1. Open a terminal and run the official installer:

   ```bash
   # macOS / Linux
   curl -fsSL https://claude.ai/install.sh | bash
   ```

   ```powershell
   # Windows PowerShell
   irm https://claude.ai/install.ps1 | iex
   ```

2. Start it by typing `claude` and pressing Enter. On first run it walks you
   through logging in via your browser (a Claude Pro/Max/Team subscription or a
   Console account). You only log in once.

If anything goes sideways, stop here and use the
[installation guide](../01-claude-code-basics/installation-setup.md) — it covers
the failure modes.

### Minute 10–15: Set up the one book-project folder

This is the canonical layout for this entire wiki. Each workflow guide goes deep
on its own subfolders; **they all assume this single tree.** One folder = one
book (or one series — see Advanced).

```text
my-novel/                        # one folder = one book project
├── CLAUDE.md                    # standing instructions Claude reads every session
├── .claude/                     # settings, hooks, skills, agents (added as you grow)
│
│  — WRITING —                     owned by: Drafting & Revision
├── manuscript/                  # current working chapters: ch01.md, ch02.md …
├── drafts/                      # in-progress versions: ch12-draft1.md, ch12-draft2.md
├── bible/                       # story bible / dossier: canon, voice, arcs, continuity log
├── originals/                   # read-only archive — Claude never writes here
├── backups/                     # timestamped automatic copies (hook-driven)
├── reports/                     # audit output: continuity-ch12.md, style-ch12.md …
│
│  — WORLD & RESEARCH —            owned by: Research & Worldbuilding
├── world/                       # CANON — established facts, chapter-cited
├── research/                    # PROVISIONAL — cited, dated, not yet canon
│
│  — MARKETING —                   owned by: Marketing & Launch
├── marketing/                   # raw-material.md, marketing-bible.md, channel copy
│
│  — PUBLISHING —                  owned by: Publishing Ops
├── front-matter/  back-matter/  # title page, copyright, also-by, newsletter CTA
├── metadata.yaml                # book metadata for EPUB/DOCX builds
├── scripts/                     # build-epub.sh, format-check.sh …
├── output/                      # everything generated lands here, versioned
└── published/                   # what actually shipped — Claude never writes here
```

Who owns what (each guide explains its subfolders in depth):

| Subfolders | Deep dive |
| --- | --- |
| `manuscript/`, `drafts/`, `bible/`, `originals/`, `backups/`, `reports/` | [Drafting & Revision](../03-author-workflows/drafting-and-revision.md) |
| `world/`, `research/` | [Research & Worldbuilding](../03-author-workflows/research-and-worldbuilding.md) |
| `marketing/` | [Marketing & Launch](../03-author-workflows/marketing-and-launch.md) |
| `front-matter/`, `back-matter/`, `metadata.yaml`, `scripts/`, `output/`, `published/` | [Publishing Ops](../03-author-workflows/publishing-ops.md) |

`manuscript/` is shared ground: drafting writes it, research cites it, marketing
mines it, publishing builds from it. (The drafting guide's worked example calls
this folder `chapters/`; this wiki's canonical name is `manuscript/` — same
folder, same job.)

You don't need to create all of it today. Start with what the first task needs:

```text
mkdir -p my-novel/manuscript my-novel/bible
```

Then copy (don't move) a chapter or two into `manuscript/` as plain text or
Markdown files. Keep your real originals wherever they live now — that's your
safety net until you set up `originals/` and backups properly.

### Minute 15–25: The first useful task

1. In the terminal, go to the folder and start Claude:

   ```bash
   cd my-novel
   claude
   ```

2. Type a real author request at the prompt:

   ```text
   Read manuscript/ch01.md and manuscript/ch02.md. List every continuity issue
   you find: names, ages, eye colors, timeline, objects that appear or vanish,
   and anything a careful beta reader would flag. Cite the line for each. Do not
   change any files.
   ```

3. Claude reads the files and reports back. That's the win: a tireless
   continuity pass on your actual manuscript, with citations.

Other good first tasks, same pattern:

```text
Read manuscript/ch01.md. List every named character with a one-line description
of what we learn about them. Save it to bible/characters.md.
```

```text
Read all files in manuscript/. Give me a one-paragraph synopsis per chapter and
flag any chapter that ends without a hook.
```

When Claude wants to create or edit a file, it shows you the change and asks
first. Approve with Enter; decline anything you didn't ask for.

### Minute 25–30: Two finishing touches

1. **Give Claude standing instructions.** Inside the session, type `/init` to
   generate a starter `CLAUDE.md` — the file Claude reads at the start of every
   session in this folder. Add author rules: "Never edit files in originals/ or
   published/. British spelling. My voice notes are in bible/voice.md." Details:
   [CLAUDE.md & memory](../01-claude-code-basics/claude-md-and-memory.md).
2. **Skim the cost guide.** [Managing usage and cost](managing-usage-and-cost.md)
   explains limits, what burns usage fastest (long sessions, re-reading big
   files), and the habits that stretch a plan. Worth it before your first long
   session.

## Author use cases

Where to go next, by what you want to do first:

1. **"I'm mid-draft and want help revising."** →
   [Drafting & Revision](../03-author-workflows/drafting-and-revision.md):
   story bibles as AI-facing dossiers, the chapter production loop, continuity
   and style audits, protecting your voice.
2. **"My draft is done; I need EPUB/DOCX and clean files."** →
   [Publishing Ops](../03-author-workflows/publishing-ops.md): repeatable
   builds into `output/`, format checks, front/back matter, and why
   `published/` is write-protected.
3. **"Launch is coming; I need blurbs, ads, email."** →
   [Marketing & Launch](../03-author-workflows/marketing-and-launch.md): build
   `marketing/marketing-bible.md` once, generate every channel from it.
4. **"I'm planning the next book/series."** →
   [Research & Worldbuilding](../03-author-workflows/research-and-worldbuilding.md):
   genre research, comp analysis, and the `research/` (provisional) vs `world/`
   (canon) discipline.
5. **"Which Claude product should I even be using?"** →
   [Which tool, when](which-tool-when.md) — Claude Code vs Desktop vs claude.ai.
6. **"I want Claude to do recurring jobs automatically."** → Skills, hooks, and
   subagents in [Power features](../02-power-features/skills.md) — but get a
   week of manual wins first.

## Common pitfalls

- **Pointing Claude at your only copy.** Until `originals/` + backups are set up
  (the [drafting guide](../03-author-workflows/drafting-and-revision.md) shows
  the protective hooks), work on copies. Approve edits one at a time at first.
- **Skipping the folder layout "for now."** Five books later you have five
  incompatible folder schemes and none of the wiki's prompts work as written.
  The tree above takes two minutes; do it on day one.
- **Marathon first session.** Long conversations re-send their whole history
  with every reply, which burns usage fast. Do one task, close, start fresh.
  See [Managing usage and cost](managing-usage-and-cost.md).
- **Vague requests.** "Fix chapter 3" gets vague results. "Tighten the pacing in
  the dinner scene in manuscript/ch03.md without cutting the argument about the
  will" gets useful ones.
- **Letting Claude rewrite your voice.** Ask for *reports and options* before
  asking for edits. The drafting guide's voice-firewall pattern exists for
  exactly this.
- **Expecting it to know your book without being told.** Claude reads files when
  asked or when `CLAUDE.md` points to them. If the story bible matters, say
  "read bible/ first" — or put that rule in `CLAUDE.md` once.

## Advanced

- **Where settings live:** project-level configuration sits in
  `.claude/settings.json` inside the book folder; per-user overrides in
  `.claude/settings.local.json`. Deny rules like `"Edit(originals/**)"` and
  `"Edit(published/**)"` make the read-only folders genuinely read-only — see
  [Settings & permissions](../01-claude-code-basics/settings-and-permissions.md)
  and the layered protection in
  [Publishing Ops](../03-author-workflows/publishing-ops.md).
- **Series, not single book:** keep one folder per book, plus a shared
  `series-bible/` (and publishing's `series-metadata.yaml`) one level up. The
  scaling pattern is in
  [Drafting & Revision](../03-author-workflows/drafting-and-revision.md) under
  "Scaling to a series."
- **Useful CLI shortcuts** (official, verified 2026-06-10): `claude -c`
  continues the most recent conversation in the current folder; `claude -r`
  picks from past sessions; `claude -p "query"` runs a one-off question and
  exits; `/help` inside a session lists commands; `exit` or Ctrl+D quits.
- **Reconciliation note for deep-dive readers:** the worked trees in the four
  workflow guides are project-local examples (`hollow-crown/`, `my-book/`,
  `my-novel/`). This page's unified tree is the canonical merge: drafting's
  `chapters/` ≡ `manuscript/` here, and drafting's and publishing's `originals/`
  are the same folder. Everything else maps one-to-one.
- **Growing into automation:** once a prompt has earned reuse, package it — a
  continuity pass becomes a [skill](../02-power-features/skills.md), pre-edit
  backups become a [hook](../02-power-features/hooks.md), heavy read-throughs go
  to [subagents](../02-power-features/subagents-and-orchestration.md).

## Sources

- https://code.claude.com/docs/en/quickstart (install commands, `claude` login
  flow, first-question pattern, permission-before-edit behavior, essential
  commands table: `claude -c`, `claude -r`, `claude -p`, `/help`, `exit`) —
  accessed 2026-06-10
- https://code.claude.com/docs/en/setup — via
  [Installation & setup](../01-claude-code-basics/installation-setup.md), which
  verified all install methods against it on 2026-06-10
- `/init` and `CLAUDE.md` behavior per
  [CLAUDE.md & memory](../01-claude-code-basics/claude-md-and-memory.md) and
  [Slash commands](../01-claude-code-basics/slash-commands.md) (both verified
  against official docs 2026-06-10)
- The unified folder tree is this wiki's own convention, merged from the four
  workflow deep dives — it is a recommendation, not an official Anthropic
  structure.
