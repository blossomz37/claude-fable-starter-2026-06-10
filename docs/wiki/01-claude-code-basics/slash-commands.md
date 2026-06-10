# Slash Commands: The Buttons and Dials of Claude Code

> **In plain words:** Type `/` in Claude Code and a menu of commands appears —
> switch models, clear the conversation, open settings, resume yesterday's session.
> Slash commands are how you operate the app itself, as opposed to talking to
> Claude. You only need about ten of them.

## What it is

Anything you type normally goes to Claude as conversation. A message that *starts*
with `/` is a command to Claude Code instead — like reaching for a dial rather than
asking the assistant. Type `/` alone to see everything available, or keep typing to
filter (`/mo` → `/model`). Text after the command name becomes its arguments
(`/compact focus on the romance subplot`).

The `/` menu actually contains three kinds of entries:

- **Built-in commands** — behavior coded into the app (`/clear`, `/model`, `/config`).
- **Bundled and custom skills** — prompts packaged as reusable commands. Your own
  skills appear here too (`/continuity-pass`), and Claude can also invoke them
  automatically when relevant. See [Skills](../02-power-features/skills.md).
- **Plugin and MCP commands** — added by extensions you install.

## Why authors care

- **Session hygiene** (`/clear`, `/compact`, `/resume`) keeps long writing
  projects from drowning in stale conversation — and saves usage.
- **One keystroke to safety:** `/plan` puts Claude in read-only critique mode.
- **Cost visibility:** `/usage` shows where your plan limits stand before you
  launch a manuscript-wide job.
- **Your rituals become commands:** a revision checklist you run every chapter can
  be `/revision-pass` instead of a paragraph you re-paste forever.

## Getting started

1. Start Claude in your book folder and type `/` — browse the menu with arrow keys.
2. Run `/help` for an overview, and `/status` to see your model, account, and version.
3. Memorize the daily six:

   | Command | What it does |
   |---|---|
   | `/clear` | Start a fresh conversation (old one stays in `/resume`). Use between unrelated tasks. |
   | `/compact` | Summarize the conversation to free space but keep going. Accepts focus instructions: `/compact keep the chapter 9 edit decisions`. |
   | `/resume` | Pick a past conversation to continue. (From the command line: `claude --continue` reopens the latest.) |
   | `/model` | Switch brains — e.g. `/model fable` for `claude-fable-5` on a hard job. See [Installation & setup](installation-setup.md). |
   | `/memory` | View/edit the CLAUDE.md files and auto memory Claude loaded. See [CLAUDE.md and memory](claude-md-and-memory.md). |
   | `/permissions` | Review and edit what Claude may do. See [Settings and permissions](settings-and-permissions.md). |

4. Learn the keyboard basics (verified current):

   | Key | Effect |
   |---|---|
   | `Esc` | Interrupt Claude mid-response; work done so far is kept. Your main brake. |
   | `Esc Esc` | With text in the box: clear the draft. With an empty box: open the **rewind menu** to restore conversation/files to an earlier point (same as `/rewind`). |
   | `Shift+Tab` | Cycle permission modes (default → acceptEdits → plan → ...). |
   | `Ctrl+C` | Interrupt; press twice to exit. `Ctrl+D` or `/exit` also quits. |
   | `↑` / `↓` | Walk back through your previous prompts. `Ctrl+R` searches them. |
   | `\` then `Enter`, or `Shift+Enter` | New line without sending (multi-paragraph prompts). |
   | `@` | File autocomplete: `look at @chapters/ch07.md` pulls the file in precisely. |
   | `!` | Shell mode — run a terminal command directly, output lands in the conversation. |
   | `Ctrl+O` | Toggle the transcript viewer (see details of what Claude actually did). |

## The built-ins most useful for authors

Beyond the daily six (full catalog: type `/` or see the official commands reference):

- **`/init`** — generate a starter CLAUDE.md for a project ([details](claude-md-and-memory.md)).
- **`/plan [task]`** — enter plan mode, optionally with the task: `/plan critique act two`.
- **`/context`** — a visual gauge of how full Claude's working memory is and what's
  eating it.
- **`/rewind`** (aliases `/checkpoint`, `/undo`) — restore code/conversation to a
  checkpoint. The undo button after an edit pass goes wrong.
- **`/usage`** (aliases `/cost`, `/stats`) — plan limits and session cost.
- **`/export [filename]`** — save the conversation as plain text; `/copy` copies
  Claude's last response (handy for pulling a generated blurb out cleanly).
- **`/config`** (alias `/settings`) — tabbed settings UI: theme, model, editor
  mode, notifications.
- **`/btw <question>`** — quick side question that does *not* clutter the
  conversation ("what was that comp title you mentioned?").
- **`/rename`** — name the session ("ch7-revision") so it's findable in `/resume`.
- **`/effort`** — dial reasoning depth up/down (`low`–`max`) on supported models.
- **`/doctor`** — diagnose installation problems.
- **`/login` / `/logout`**, **`/theme`**, **`/release-notes`** — what they sound like.
- **`/add-dir <path>`** — let Claude also see another folder (your research vault)
  this session; **`/cd <path>`** — move the whole session to another project (v2.1.169+).
- **`/feedback`** — report a bug to Anthropic.

Power-user honorable mentions: `/agents` (subagents), `/mcp` (external tool
connections), `/hooks`, `/skills`, `/plugin`, `/background`, `/schedule` — each has
a wiki page in [02-power-features](../02-power-features/) where written.

## Custom slash commands (your own rituals)

Custom commands and skills have **merged**: a skill is a folder with a `SKILL.md`
file, and its name becomes a command. Project skills live in
`.claude/skills/<name>/SKILL.md`; personal everywhere-skills in
`~/.claude/skills/<name>/SKILL.md`. A minimal example —
`.claude/skills/continuity-pass/SKILL.md`:

```yaml
---
description: Check the named chapter against the series bible and report
  contradictions before suggesting fixes.
---
Read series-bible.md, then read the chapter file the user names.
List every contradiction (names, dates, eye colors, travel times) with
file and line references. Do not edit anything until I approve.
```

Now `/continuity-pass ch07` works — and Claude can also invoke the skill on its
own when it's clearly relevant. The older `.claude/commands/*.md` format still
works, but skills are the recommended path (supporting files, invocation control,
auto-loading). Full treatment: [Skills](../02-power-features/skills.md).

## Common pitfalls

- **Slash only counts at the start.** "`Can you run /compact`" is just chat; type
  the command as its own message.
- **`/clear` vs `/compact`:** `/clear` forgets the conversation (recoverable via
  `/resume`); `/compact` summarizes and continues. Mid-task, you want `/compact`.
- **Letting auto-compact decide.** Claude compacts automatically when context
  fills, but the automatic summary guesses what matters. Running `/compact` with
  focus instructions at a natural break keeps *your* priorities.
- **Switching models mid-conversation re-reads history without cached context** —
  the picker warns you; it's a usage-cost bump, not a data loss.
- **Not every command appears for everyone.** Availability depends on platform and
  plan (e.g. `/desktop` needs macOS/Windows + subscription).
- **Skill names collide:** if a skill and a legacy command share a name, the skill
  wins; personal beats project.

## Advanced

- **Aliases (verified):** `/clear` = `/reset` = `/new` · `/resume` = `/continue` ·
  `/rewind` = `/checkpoint` = `/undo` · `/usage` = `/cost` = `/stats` · `/config` =
  `/settings` · `/permissions` = `/allowed-tools` · `/exit` = `/quit` · `/feedback`
  = `/bug`.
- **CLI counterparts:** `claude --continue` / `claude --resume [id]`,
  `claude --model <alias>`, `claude --permission-mode plan`,
  `claude -p "prompt"` (non-interactive print mode, scriptable: pipe a chapter in,
  get analysis out).
- **Skill frontmatter highlights:** `description` (drives auto-invocation),
  `argument-hint`, `arguments` (named positional `$name` substitution),
  `disable-model-invocation: true` to make a skill user-only (a pure slash
  command), `model` / `effort` overrides per skill. `/reload-skills` re-scans
  directories mid-session; live change detection picks up edits to existing skill
  folders automatically.
- **MCP prompts as commands:** connected MCP servers can expose prompts that
  appear as `/mcp__<server>__<prompt>`.
- **Deeper keyboard tricks:** `Ctrl+G` edits your prompt in your default text
  editor (long synopses!), `Ctrl+B` sends a running task to the background,
  `Ctrl+T` toggles the task list, `Option+P`/`Alt+P` switches model without
  clearing your draft, `Ctrl+L` redraws a garbled screen. Vim editing mode:
  `/config` → Editor mode. Custom keybindings: `~/.claude/keybindings.json` via
  `/keybindings`.
- **Removed/renamed (don't trust old tutorials):** `/vim` (gone in v2.1.92 — use
  `/config`), `/pr-comments` (gone in v2.1.91), `/ultrareview` → `/code-review
  ultra`, `/extra-usage` → `/usage-credits`. The `#` memory shortcut no longer
  appears in current docs — see [CLAUDE.md and memory](claude-md-and-memory.md).

## Sources

- https://code.claude.com/docs/en/commands (full command table, aliases, removed commands, MCP prompts) — accessed 2026-06-10
- https://code.claude.com/docs/en/interactive-mode (keyboard shortcuts, Esc/Esc-Esc, Shift+Tab, `!` shell mode, `@` mentions, history, /btw) — accessed 2026-06-10
- https://code.claude.com/docs/en/skills (commands-merged-into-skills, skill locations, frontmatter, legacy `.claude/commands/` support) — accessed 2026-06-10
- https://code.claude.com/docs/en/context-window (auto-compaction behavior, /compact focus) — accessed 2026-06-10
- https://code.claude.com/docs/en/model-config (/model behavior and cache warning) — accessed 2026-06-10
- ⚠️ Unverified: none.
