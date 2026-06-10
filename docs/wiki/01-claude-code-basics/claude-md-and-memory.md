# CLAUDE.md and Memory: Teaching Claude Your Book

> **In plain words:** Claude starts every session with a blank slate — it does not
> remember yesterday's conversation. A `CLAUDE.md` file is a note you leave on its
> desk: your voice rules, series facts, and formatting preferences, read automatically
> at the start of every session. Claude also keeps its own notebook ("auto memory")
> of things it learns while working with you.

## What it is

`CLAUDE.md` is a plain markdown file (you can edit it in any text editor) that
Claude Code reads before doing anything else. Think of it as the **AI-facing page
of your story bible**: not the whole bible, but the standing orders — "British
spelling," "Mara's eyes are grey, not green," "never edit files in `originals/`."

There are two complementary memory systems, both loaded at the start of every session:

- **CLAUDE.md files** — instructions *you* write. Project-wide rules your future
  self (and Claude) must never forget.
- **Auto memory** — notes *Claude* writes for itself as it works: corrections you
  made, preferences it noticed, how your project is laid out. On by default, stored
  per project, fully readable and editable by you.

### Why Claude "forgets" — context windows in plain terms

Everything Claude knows during a session lives in its **context window** — a
working memory with a hard size limit (think of a desk that only holds so many
pages: roughly 200,000 tokens, about 150,000 words, on standard models). Your
messages, the chapters it reads, and its own replies all pile onto that desk.

When the desk gets full, Claude Code **compacts**: it summarizes the conversation
so far and continues from the summary. Details can blur in that summary — which is
exactly why memory files matter. Your project-root `CLAUDE.md` and auto memory are
**re-read from disk after compaction**, so rules stored there survive even when
conversational details don't. A rule you only said in chat ("remember, the heroine
limps") can fade; the same rule in `CLAUDE.md` cannot.

## Why authors care

- **Voice protection.** "Preserve my voice; never smooth out sentence fragments"
  applies to every session forever, not just the one where you said it.
- **Series continuity.** Eye colors, timeline anchors, magic-system rules, who
  knows which secret — stated once, enforced everywhere.
- **No re-briefing.** New session, zero ramp-up: Claude already knows your
  formatting, your file layout, and what "do a continuity pass" means to you.
- **It's just a text file.** Lives in your book folder, syncs with Dropbox/git,
  readable by you and by other AI tools.

## Getting started

1. In your book folder, start Claude and run:

   ```text
   /init
   ```

   Claude examines the folder and generates a starter `CLAUDE.md`. If one already
   exists, `/init` suggests improvements instead of overwriting.

2. Open it with `/memory` (lists every loaded memory file; pick one to edit) or in
   any text editor. Replace the scaffolding with writing-project content:

   ```markdown
   # The Hollow Crown — Book 2 of the Thornwood series

   ## Voice and style
   - Close third person, past tense. POV: Mara (odd chapters), Edmun (even).
   - British spelling. Em dashes sparingly — max ~1 per 1000 words.
   - Never replace my sentence fragments with full sentences.

   ## Series facts (do not contradict)
   - Mara: grey eyes, left-handed, widowed in Book 1, ch. 22.
   - The Thornwood cannot be entered after dusk. No exceptions yet.
   - Full canon: @series-bible.md

   ## Files and formatting
   - Chapters live in chapters/ as ch01.md, ch02.md ...
   - originals/ is untouchable. Never edit it; copy to drafts/ instead.
   - Scene breaks are *** on their own line.

   ## Workflow
   - When I say "continuity pass", check names, dates, eye colors,
     and travel times against series-bible.md and report findings
     before changing anything.
   ```

3. Ask Claude to remember things mid-session: *"Remember: chapter titles are
   always three words."* Claude saves that to **auto memory**. To put it in
   CLAUDE.md instead, say *"add this to CLAUDE.md."*

4. Verify with `/memory` — if a file isn't listed there, Claude can't see it.

> Older tutorials mention starting a message with `#` to quick-add a memory. That
> shortcut no longer appears in the current official docs (the only documented
> prefix shortcuts today are `/` for commands, `!` for shell, `@` for file
> mentions). Just ask Claude to remember, or edit the file via `/memory`.

## Where memory files live

| Scope | File | Use it for |
|---|---|---|
| **All your projects** | `~/.claude/CLAUDE.md` | Personal prefs: "always offer options on creative decisions," spelling conventions |
| **This project (shared)** | `CLAUDE.md` or `.claude/CLAUDE.md` in the book folder | Series facts, voice rules, file layout — anything a co-writer should also get |
| **This project (private)** | `CLAUDE.local.md` | Personal notes not for collaborators (add to `.gitignore` if you use git) |
| **Auto memory (Claude's notes)** | `~/.claude/projects/<project>/memory/` | Claude maintains it; you audit via `/memory` |

All applicable files load together (broad scope first, project last), so project
rules effectively refine your global ones. Claude also walks **up** the folder tree —
useful for a series: put `MySeries/CLAUDE.md` above `MySeries/Book2/`, and working
in Book2 loads both.

## Author use cases

1. **Voice firewall.** A "Voice and style" section listing your authentic tics —
   fragments, comma splices, dialect spellings — so every edit pass preserves them.
2. **Series bible hookup.** Keep the full bible in `series-bible.md` and reference
   it with `@series-bible.md` inside CLAUDE.md; it loads automatically every session.
3. **Protected originals.** State "never edit `originals/`" in CLAUDE.md *and*
   enforce it with a deny rule — see [Settings and permissions](settings-and-permissions.md).
   CLAUDE.md is guidance; permission rules are enforcement.
4. **Per-pen-name defaults.** Each pen name's folder gets its own CLAUDE.md (heat
   level, genre conventions, blurb formulas), while `~/.claude/CLAUDE.md` holds your
   universal preferences.
5. **NPE-style dossiers.** If you maintain an AI-facing story dossier (constraints,
   tension axes, ghost-draft notes), CLAUDE.md is the loader: a short summary plus
   `@dossier/constraints.md` imports.
6. **Defined rituals.** Teach Claude named procedures ("do a 'cold read'" = read the
   chapter fresh and report confusions before suggesting edits). For long multi-step
   procedures, package them as a [skill](../02-power-features/skills.md) instead —
   skills load only when invoked, saving context space.

## Common pitfalls

- **Bloat.** Target **under 200 lines** per CLAUDE.md. It loads into every session
  and consumes context (which costs usage); long, rambling files also reduce how
  reliably Claude follows them. Move bulk reference into imports or path-scoped rules.
- **Vague rules.** "Keep my style" does little. "Never convert single quotes in
  dialect dialogue to double quotes" works.
- **Contradictions.** If your global file says "Oxford comma" and the project file
  says otherwise, Claude may pick arbitrarily. Audit with `/memory` occasionally.
- **It's guidance, not law.** Claude *tries* to follow CLAUDE.md; nothing technically
  blocks it. For hard guarantees ("never touch originals/") use
  [permission deny rules](settings-and-permissions.md) or hooks.
- **Conversation-only instructions die at compaction.** If it matters past today,
  get it into CLAUDE.md or let auto memory capture it.
- **Imports still cost context.** `@file` imports keep things organized but load in
  full at launch — importing your entire 40k-word bible eats the desk space your
  chapters need.

## Advanced

- **Full location list (load order: broadest → most specific):**
  managed policy (`/Library/Application Support/ClaudeCode/CLAUDE.md` on macOS,
  `C:\Program Files\ClaudeCode\CLAUDE.md` on Windows) → `~/.claude/CLAUDE.md` →
  `./CLAUDE.md` or `./.claude/CLAUDE.md` → `./CLAUDE.local.md`. Files in parent
  directories load in full at launch; files in *subdirectories* load on demand when
  Claude reads files there.
- **Imports:** `@path/to/file` anywhere in a CLAUDE.md; relative paths resolve from
  the importing file; recursive up to 4 hops; `@~/...` works for home-directory
  files (handy for sharing personal notes across git worktrees). First external
  import in a project triggers a one-time approval dialog. Claude reads `CLAUDE.md`,
  not `AGENTS.md` — bridge with a one-line `@AGENTS.md` import or a symlink.
- **`/init` interactive flow:** set `CLAUDE_CODE_NEW_INIT=1` for a multi-phase
  setup that also proposes skills and hooks, with a reviewable proposal before
  writing files.
- **Rules directory:** `.claude/rules/*.md` (project) and `~/.claude/rules/*.md`
  (personal) split instructions into topic files; discovered recursively; symlinks
  supported. Add YAML frontmatter to scope a rule to matching files only:

  ```markdown
  ---
  paths:
    - "chapters/**/*.md"
  ---
  # Chapter formatting rules
  - Scene breaks are *** on their own line.
  ```

  Path-scoped rules load only when Claude reads matching files — the main tool for
  keeping startup context lean.
- **Auto memory mechanics:** requires v2.1.59+; on by default. Storage:
  `~/.claude/projects/<project>/memory/` with a `MEMORY.md` index plus topic files.
  Only the first **200 lines or 25 KB** of MEMORY.md load at startup; topic files
  are read on demand. Toggle in `/memory`, or `"autoMemoryEnabled": false` in
  settings, or env `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`. Relocate with
  `"autoMemoryDirectory": "~/path"`. Machine-local; shared across git worktrees of
  the same repo. "Writing memory" / "Recalled memory" in the UI = Claude touching
  these files.
- **What survives compaction:** system prompt and project-root CLAUDE.md +
  unscoped rules + auto memory are re-injected from disk; path-scoped rules and
  nested CLAUDE.md files are lost until a matching file is read again; invoked
  skill bodies re-inject capped at 5,000 tokens each / 25,000 total.
- **Context controls:** `/context` visualizes current usage; `/compact focus on
  the chapter 12 revision` compacts with your emphasis; `/clear` starts fresh
  between unrelated tasks (cheaper than dragging old conversation along). 1M-token
  context models exist for huge sessions — see
  [installation & setup](installation-setup.md) Advanced.
- **Monorepo-style series folders:** `claudeMdExcludes` (glob patterns, any
  settings layer) skips irrelevant CLAUDE.md files. HTML comments
  (`<!-- note to self -->`) in CLAUDE.md are stripped before reaching Claude —
  free human-only annotations.

Related: [Slash commands](slash-commands.md) for `/init`, `/memory`, `/compact`,
`/context`; [Settings and permissions](settings-and-permissions.md) for turning
guidance into enforcement.

## Sources

- https://code.claude.com/docs/en/memory (locations, load order, imports, rules, auto memory, /init, /memory, troubleshooting) — accessed 2026-06-10
- https://code.claude.com/docs/en/context-window (what survives compaction, /context, when context fills) — accessed 2026-06-10
- https://code.claude.com/docs/en/settings (autoMemoryEnabled, autoMemoryDirectory, claudeMdExcludes) — accessed 2026-06-10
- https://code.claude.com/docs/en/interactive-mode (current prefix shortcuts: `/`, `!`, `@`) — accessed 2026-06-10
- ⚠️ Unverified: the retirement of the `#` quick-add memory shortcut is inferred from its absence in current official docs (it no longer appears on the memory or interactive-mode pages); no changelog entry confirming removal was located.
- ⚠️ Unverified: "200K tokens ≈ 150,000 words" is an approximation, not an official figure.
