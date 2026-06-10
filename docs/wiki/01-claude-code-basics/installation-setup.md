# Installing Claude Code and Starting Your First Session

> **In plain words:** Claude Code is an AI assistant that works directly with the
> files on your computer — your manuscript, your series bible, your blurbs — instead
> of making you copy-paste into a chat window. This guide gets it installed, logged
> in, and pointed at your book folder, even if you have never opened a terminal in
> your life.

## What it is

Claude Code is Anthropic's "agentic" assistant. Where the Claude website is a chat
box, Claude Code is more like an editorial assistant sitting at your desk: it can
open your chapter files, read your story bible, make edits, rename files, and run
small tasks for you — always asking permission before it changes anything.

It comes in several forms, all powered by the same engine:

- **Terminal (CLI)** — the full-featured version. You type to Claude in a text
  window called a terminal. This is what most of this wiki covers. ("CLI" just
  means "command-line interface" — a program you talk to by typing.)
- **Desktop app** — a regular Mac/Windows app, no terminal required. Good if the
  terminal feels intimidating; it shows file changes visually.
- **VS Code / Cursor extension and JetBrains plugin** — Claude inside a code editor.
  Useful if you already draft in VS Code or use it for Vellum-adjacent tinkering.
- **Web** — [claude.ai/code](https://claude.ai/code) runs sessions in the cloud on
  a copy of a GitHub repository. Handy for long tasks you check on later; also
  available in the Claude iOS app.

They all read the same configuration, so a story bible you set up for the terminal
also works in the desktop app (see [CLAUDE.md and memory](claude-md-and-memory.md)).

## Why authors care

- Claude can read your **whole manuscript folder**, not just what fits in a chat box.
- It remembers your **voice rules and series facts** between sessions via memory files.
- It can do tedious file work: split a manuscript into chapter files, convert
  formats, build a timeline, compile notes — with your approval at each step.
- One subscription covers it: Claude Code requires a **paid plan** (Pro, Max, Team,
  or Enterprise) or an Anthropic Console/API account. The free Claude.ai plan does
  **not** include Claude Code.

## Getting started

### Step 0: Open a terminal (first-timers start here)

A terminal is a window where you type commands instead of clicking. That's all it is.

- **macOS:** press `Cmd + Space` (Spotlight), type `Terminal`, press `Enter`.
  A window appears with a blinking cursor.
- **Windows:** press `Win + X` and choose **Windows PowerShell** (or **Terminal**).
  Note: Windows has two lookalikes — PowerShell shows `PS C:\Users\You>` at the
  start of each line; CMD shows `C:\Users\You>` without the `PS`. Use PowerShell.

You can't click on things inside the terminal — use arrow keys and `Enter`.

### Step 1: Install Claude Code

The official recommended method is the **native installer** (no extra software needed):

**macOS** (and Linux/WSL) — paste this into the terminal and press `Enter`:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

```powershell
irm https://claude.ai/install.ps1 | iex
```

When it finishes you'll see "Claude Code successfully installed!" Native installs
auto-update in the background, so you never have to do this again.

Prefer no terminal at all? Download the **desktop app** for
[macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect) or
[Windows](https://claude.com/download), sign in, and click the **Code** tab.

### Step 2: Go to your book folder

`cd` means "change directory" — it points the terminal at a folder. If your novel
lives in `Documents/MyNovel`:

```bash
cd ~/Documents/MyNovel
```

(`~` is shorthand for your home folder. On Windows PowerShell the same command works.)
Tip: type `cd ` (with a space), then drag the folder from Finder/Explorer into the
terminal window — it fills in the path for you. Type `pwd` to confirm where you are,
and `ls` to list the files there.

### Step 3: Start Claude and log in

```bash
claude
```

On Windows, close and reopen PowerShell first so it finds the new `claude` command.
The first time, Claude opens your browser to sign in with your Claude account.
After that, you're in: type a message and press `Enter`. Try:

```text
Read through the files in this folder and tell me what you see.
```

### Step 4: Know how to stop things

- **`Esc`** — interrupt Claude mid-response. It keeps the work done so far; you can redirect.
- **`Ctrl+C`** — interrupt a running operation; press twice to exit Claude Code.
- **`exit` or `Ctrl+D`** — leave Claude Code. Your conversation is saved automatically.
- **`/help`** — list available commands (see [Slash commands](slash-commands.md)).

Claude always asks before editing files or running commands unless you change the
defaults — see [Settings and permissions](settings-and-permissions.md).

## What is a "session"?

A session is one continuous conversation with Claude in one folder — like one
sitting with an assistant. Each session starts with a blank memory of your
conversation (your memory files reload automatically). When you quit, the session
is saved. To pick up where you left off:

- `claude --continue` (or `claude -c`) — reopen the most recent session in this folder
- `claude --resume` or `/resume` inside Claude — pick from a list of past sessions

## Choosing a model

Models are the "brains" available to Claude Code, trading speed against depth:

- **Sonnet** — fast, capable; the default on Pro plans. Fine for most drafting help.
- **Opus** — deeper reasoning; the default on Max plans.
- **Haiku** — fastest and cheapest, for simple tasks.
- **Fable 5** (`claude-fable-5`) — Anthropic's most capable model, built for long
  autonomous tasks. It is **never the default**; you select it deliberately.

Type `/model` inside a session to open a picker, or jump straight there:

```text
/model fable
```

Heavier models burn through plan usage limits faster (`/usage` shows where you
stand), so a sensible author pattern is Sonnet for routine work and Fable 5 or Opus
for a full-manuscript continuity audit.

## Author use cases

1. **First reconnaissance.** `cd` into your manuscript folder, run `claude`, and ask:
   "Summarize each chapter file in two sentences and flag any files that look like
   duplicates or stray versions."
2. **Project setup.** Run `/init` to have Claude create a starter memory file, then
   add your voice rules — see [CLAUDE.md and memory](claude-md-and-memory.md).
3. **Desktop app for the terminal-averse.** Install the desktop app, open your book
   folder, and review Claude's proposed edits as visual before/after diffs.
4. **Long jobs on the web.** Kick off "produce a full series timeline from these
   five books" at claude.ai/code and check the result after dinner.
5. **A second terminal, a second project.** Open a new terminal window, `cd` into a
   different pen name's folder, run `claude` — sessions are independent.

## Common pitfalls

- **"command not found: claude"** — close the terminal and open a new one. If it
  persists on macOS: `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc` then
  `source ~/.zshrc`.
- **Free plan won't work.** Claude Code needs Pro, Max, Team, Enterprise, or a
  Console (API) account. API use is pay-per-token; subscription plans have usage
  limits that reset periodically.
- **Wrong folder.** If Claude says it can't find your chapters, you probably ran
  `claude` from your home folder. Quit, `cd` into the book folder, rerun `claude`
  (or use `/cd <path>` inside a session on recent versions).
- **PowerShell vs CMD confusion on Windows.** The install commands differ; check
  for the `PS` prefix in your prompt.
- **Old macOS.** Requires macOS 13.0 or later (Windows 10 1809+, 4 GB RAM).

## Advanced

**All install methods (verified 2026-06-10):**

| Method | Command | Auto-updates? |
|---|---|---|
| Native (recommended) | `curl -fsSL https://claude.ai/install.sh \| bash` | Yes |
| Native, Windows PS | `irm https://claude.ai/install.ps1 \| iex` | Yes |
| Native, Windows CMD | `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` | Yes |
| Homebrew | `brew install --cask claude-code` (stable) or `claude-code@latest` | No — `brew upgrade claude-code` |
| WinGet | `winget install Anthropic.ClaudeCode` | No — `winget upgrade Anthropic.ClaudeCode` |
| npm | `npm install -g @anthropic-ai/claude-code` (Node 18+; installs the same native binary) | Partial |
| Linux | signed apt/dnf/apk repos at `downloads.claude.ai` | Via system updates |

- **Verify / diagnose:** `claude --version`, `claude doctor`, manual update with
  `claude update`. Uninstall (native): `rm -f ~/.local/bin/claude && rm -rf ~/.local/share/claude`.
- **Release channels:** `autoUpdatesChannel` setting (`"latest"` default, `"stable"`
  ~1 week behind), set via `/config` → Auto-update channel. `minimumVersion` pins a floor.
- **Pin or script a version:** `curl -fsSL https://claude.ai/install.sh | bash -s stable`
  or `... | bash -s 2.1.89`.
- **Model selection precedence:** `/model <alias|name>` in-session (saves as your
  default for new sessions; press `s` in the picker for session-only) →
  `claude --model <alias>` at launch → `ANTHROPIC_MODEL` env var → `"model"` in
  settings.json. Aliases: `default`, `best` (Fable 5 where available, else Opus),
  `fable`, `opus`, `sonnet`, `haiku`, `opus[1m]`/`sonnet[1m]` (1M-token context),
  `opusplan` (Opus for plan mode, Sonnet for execution).
- **Fable 5 notes:** requires Claude Code v2.1.170+; thinking is always on and the
  default effort level is `high` (adjust via `/effort`: `low`–`xhigh`, session-only
  `max`/`ultracode`). Safety classifiers may auto-fall back flagged requests to Opus 4.8.
- **Defaults by plan:** Max/Team Premium/API → Opus 4.8; Pro/Team Standard → Sonnet 4.6.
- **Login management:** `/login`, `/logout`, `/status` (account + model + version).
  Auth supports claude.ai subscriptions and Anthropic Console; third-party routes
  (Bedrock, Vertex, Foundry) exist for enterprise.
- **Resume semantics:** resumed sessions keep the model they were saved with,
  regardless of your current default.
- **Windows shell detail:** installing Git for Windows gives Claude a Bash tool;
  without it, Claude uses PowerShell as its shell tool. Optional, not required.

Next: teach Claude your project with [CLAUDE.md and memory](claude-md-and-memory.md),
tame the permission prompts in [Settings and permissions](settings-and-permissions.md),
and learn the [slash commands](slash-commands.md) you'll use daily.

## Sources

- https://code.claude.com/docs (overview: surfaces, install tabs, desktop/web links) — accessed 2026-06-10
- https://code.claude.com/docs/en/setup (system requirements, all install/update/uninstall commands, auth) — accessed 2026-06-10
- https://code.claude.com/docs/en/terminal-guide (first-time terminal walkthrough, troubleshooting) — accessed 2026-06-10
- https://code.claude.com/docs/en/model-config (aliases, /model behavior, Fable 5, effort, defaults by plan) — accessed 2026-06-10
- https://code.claude.com/docs/en/interactive-mode (Esc/Ctrl+C/Ctrl+D behavior) — accessed 2026-06-10
- ⚠️ Unverified: exact dollar pricing per plan (not restated here; see claude.com/pricing).
