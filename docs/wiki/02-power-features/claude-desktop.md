# Claude Desktop: The App That Works in Your Folders

> **In plain words:** Claude Desktop is the Claude app you install on your Mac or
> Windows PC. It does everything the claude.ai website does, plus things a website
> can't: it can open your actual manuscript folders, rename and organize your files,
> run long jobs while you make coffee, and even run Claude Code in a friendly
> point-and-click window — no terminal required.

## What it is

There are three main ways to use Claude on a computer, and they're easy to confuse:

- **claude.ai (the website)** — Claude in a browser tab. You chat, upload files by
  hand, and download results by hand. It never touches your hard drive directly.
- **Claude Desktop (this doc)** — an installed app for macOS and Windows. Same chat
  experience as the website, but it can also reach into folders you choose on your
  computer and work on the files inside them.
- **Claude Code** — Claude as a hands-on assistant that lives *inside* a project
  folder and edits files directly. It started as a terminal (command-line) tool, but
  it now also runs as a tab inside Claude Desktop.

As of June 2026, Claude Desktop has **three tabs** across the top:

| Tab | What it's for | Author translation |
|---|---|---|
| **Chat** | Regular conversations, Projects, Artifacts, file uploads | Your brainstorming and feedback room |
| **Cowork** | Hands-off, multi-step tasks on your local folders | An assistant you hand a messy folder and a to-do |
| **Code** | Claude Code with a graphical interface | The chapter-drafting workhorse, without the terminal |

Think of it as one building with three rooms: a sitting room for conversation, a
back office where an assistant quietly processes your files, and a workshop where
the heavy drafting and revision machinery lives.

## Why authors care

- **No more upload/download shuffle.** Cowork reads and writes files in folders you
  approve — Claude can organize your manuscript folder instead of telling you how to.
- **Real deliverables.** Cowork produces formatted Word docs, spreadsheets with
  working formulas, and organized folders — saved straight to your disk.
- **Claude Code without the terminal.** The Code tab gives you the same drafting
  pipeline power (skills, CLAUDE.md, connectors) in a windowed app with visible
  file changes.
- **Scheduled tasks.** "Every Monday, summarize the week's new scenes" — Cowork can
  run recurring jobs (while the app is open).
- **Send tasks from your phone.** With Dispatch (Pro/Max), you can text a task from
  the Claude mobile app and your desktop at home does the work.
- **Everything from the website still works** — Projects, Artifacts, connectors,
  skills — so there's little reason for an author with a paid plan *not* to use the
  desktop app as their main door into Claude.

## Getting started

1. Go to **claude.ai/download** (or claude.com/download) and grab the installer —
   macOS 11+ or Windows 10+. There is no Linux desktop app; Linux users use the
   Claude Code CLI instead.
2. Open the downloaded file, install, and launch Claude from Applications (Mac) or
   the Start menu (Windows).
3. Sign in with your Claude account. A paid plan (Pro, Max, Team, or Enterprise) is
   required for Cowork and the Code tab; Chat works on Free.
4. Try Chat first: start a conversation, ask Claude to draft three blurb options
   for your current book. They'll appear as an **Artifact** — a document panel beside
   the chat you can iterate on.
5. Now try **Cowork**: click the Cowork tab, point it at a *copy* of a low-stakes
   folder (say, a folder of old story notes), and ask: *"Read everything in this
   folder and create an INDEX.md summarizing what each file contains."* Approve its
   plan and watch it work.
6. When you're ready for drafting pipelines, click the **Code** tab, choose your
   book's project folder, and you're running Claude Code — see
   [installation-setup](../01-claude-code-basics/installation-setup.md) for the
   project-folder fundamentals that apply there.

## Author use cases

**1. Series bible Q&A with Projects (Chat tab).**
Create a Project called "Ashford Saga," upload your series bible, character sheets,
and timeline to its project knowledge. Every chat inside that Project starts already
knowing your world — ask "would Mira realistically know about the harbor fire in
book 2?" without re-uploading anything. Projects support custom instructions
(e.g., "always answer in terms of what's on the page, not what I intended").

**2. Blurb and query-letter iteration with Artifacts (Chat tab).**
Paste your synopsis, ask for a back-cover blurb. The blurb lands in an Artifact
panel; say "tighten paragraph two, make the hook a question" and watch versions
stack up. You can flip between versions and copy the winner straight to your
retailer dashboard.

**3. Cowork organizes a messy manuscript folder.**
Point Cowork at the folder where five years of drafts live and say: *"Sort these
into subfolders by book, rename files to BookTitle_ChapterNN_vN, flag duplicates in
a report, and don't delete anything."* Cowork shows you its plan first, asks before
each risky step (in "Ask before acting" mode), and must get your explicit "Allow"
before it can permanently delete any file.

**4. Cowork builds your launch tracker.**
"Read the back matter of these five EPUB-exported chapters and my promo notes,
then build me an Excel sheet tracking ARC reviewers: name, contact, book, status,
follow-up date — with a formula that flags anyone overdue." Cowork delivers a real
.xlsx with working formulas to your folder.

**5. Research chats with connectors (Chat tab).**
Connect Google Drive or Notion via **Settings → Connectors**, then ask Claude to
pull your existing research notes into a worldbuilding discussion. Connectors are
MCP (Model Context Protocol — a standard plug for hooking Claude up to other apps)
with a one-click setup screen.

**6. Chapter drafting in the Code tab.**
Open your book project in the Code tab, pick Fable 5 from the model dropdown, and
run the same skills and CLAUDE.md-driven workflow you'd use in the CLI — with a
visible diff of every file change before you accept it. Your chapter pipeline
skills work here too; this is the friendliest on-ramp to the workflows described
elsewhere in this wiki. (This can be packaged as a skill — see your chapter
production skills.)

**7. Scheduled weekly continuity sweep (Cowork).**
Type `/schedule` in a Cowork task: "Every Friday at 4pm, re-read the chapters
folder and update CONTINUITY_LOG.md with any new character details." Caveat: it
only runs while your computer is awake and the app is open.

## Common pitfalls

- **Cowork eats usage faster than chat.** Multi-step agentic tasks are
  token-hungry; Anthropic says so explicitly. Batch related work, use plain Chat
  for simple questions, and watch **Settings → Usage**.
- **Fable 5's free-inclusion window is closing.** Fable 5 (launched June 9, 2026)
  is included at no extra cost on Pro, Max, Team, and seat-based Enterprise plans
  **only through June 22, 2026**. From June 23 it requires usage credits on
  subscription plans (API access is unaffected, at $10/M input, $50/M output
  tokens). Pick it from the model picker while the window lasts; after that, decide
  per-task whether it's credit-worthy.
- **Closing the app kills Cowork tasks.** Cowork runs on *your* machine; the app
  must stay open and the computer awake. (Code-tab *cloud* sessions are the
  exception — they keep running on Anthropic's servers.)
- **Cowork memory is per-project.** Memory persists inside Cowork projects but not
  across standalone Cowork sessions — put recurring context in a Cowork project or
  in folder instructions.
- **Give Cowork copies first.** It really edits your files. Until you trust a
  workflow, point it at a duplicated folder, keep "Ask before acting" on, and keep
  backups (you keep backups anyway, right?).
- **"Act without asking" is for supervised, trusted work only.** Faster, but Claude
  proceeds without pausing. Never combine it with your only copy of a manuscript.
- **Desktop ≠ offline.** An active internet connection is required throughout;
  the model still runs in the cloud. Only the file access is local.

## Advanced

### Settings map (June 2026)

| What | Where |
|---|---|
| Skills on/off, code execution | Settings → Capabilities; manage individual skills under Customize → Skills (browse/install from the skills directory via "+" → Browse skills) |
| Desktop extensions (one-click local MCP) | Settings → Extensions (packaged as `.mcpb` files) |
| Connectors (remote MCP) | Settings → Connectors, or "+" button → Connectors in a chat/session |
| Manual MCP config file | Settings → Developer → Edit Config |
| Cowork global instructions | Settings → Cowork → Global instructions → Edit |
| Usage meter | Settings → Usage |
| Claude Code options (bypass permissions, worktree location, preview, auto-archive) | Settings → Claude Code |
| Computer use toggle (research preview, Pro/Max) | Settings → General (under Desktop app) |

### MCP configuration file paths

The Desktop chat app's manual MCP config lives at:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Format (same `mcpServers` shape as everywhere else):

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/you/Manuscripts"]
    }
  }
}
```

Anthropic now steers most users to **Settings → Extensions** (`.mcpb` packages,
installed like browser extensions) instead of hand-editing this JSON — but the
file still works and is still read.

**Cross-surface MCP behavior (verified):** the Desktop app loads servers from
`claude_desktop_config.json` into **Code tab** sessions too, alongside servers from
`~/.claude.json` and project `.mcp.json`. The standalone CLI does **not** read
`claude_desktop_config.json`; on macOS/WSL run `claude mcp add-from-claude-desktop`
to copy those servers into `~/.claude.json`.

### The Code tab in depth

The Code tab is full Claude Code with a GUI — same engine as the CLI, and the two
share `CLAUDE.md`, settings (`~/.claude/settings.json`, `~/.claude.json`), hooks,
skills, and MCP servers. Highlights:

- **Sessions**: each is an independent conversation + project folder + change set.
  Parallel sessions get automatic Git worktree isolation (stored in
  `<project-root>/.claude/worktrees/` by default).
- **Environments**: Local (your machine), Remote (Anthropic cloud — survives
  closing the app), or SSH.
- **Panes**: chat, diff, preview, terminal, file editor, plan, tasks — drag to
  arrange (requires Desktop v1.2581.0+).
- **Permission modes**: Ask permissions, Auto accept edits, Plan mode, Auto
  (research preview), Bypass permissions (enable in Settings → Claude Code). The
  CLI-only `dontAsk` mode is not available.
- **From the CLI**: run `/desktop` in a terminal session to hand it off to the
  Desktop app (subscription auth only, not API key).
- **Dispatch**: a persistent assistant conversation in the Cowork tab (Pro/Max
  only); message it from your phone and it can spawn Cowork work or Code sessions
  on your desktop, with push notifications when done.

### Code tab keyboard shortcuts (macOS; use Ctrl for Cmd on Windows)

| Shortcut | Action |
|---|---|
| `Cmd+/` | Show all shortcuts |
| `Cmd+N` / `Cmd+W` | New / close session |
| `Ctrl+Tab` / `Ctrl+Shift+Tab` | Next / previous session |
| `Esc` | Stop Claude's response |
| `Cmd+Shift+D` / `Cmd+Shift+P` | Toggle diff / preview pane |
| ``Ctrl+` `` | Toggle terminal pane |
| `Cmd+;` | Open a side chat (ask without derailing the session) |
| `Ctrl+O` | Cycle transcript view modes (Normal / Verbose / Summary) |
| `Cmd+Shift+M` / `Cmd+Shift+I` / `Cmd+Shift+E` | Permission mode / model / effort menus |

These apply to the Code tab only; CLI interactive-mode shortcuts (like Shift+Tab)
do not carry over. ⚠️ Unverified: a documented global shortcut list for the
Chat/Cowork tabs — the install article doesn't publish one.

### Known limitations vs the CLI

- **No scripting/automation**: `--print`, output formats, and the Agent SDK are
  CLI-only; Desktop is interactive.
- **Agent teams** (parallel sessions that message each other) are CLI-only; use
  dynamic workflows in Desktop for multi-agent work inside one session.
- **Terminal-dialog commands** (`/permissions`, `/config`, `/agents`, `/doctor`)
  don't work in the Code tab — edit settings files directly or use the CLI.
- **No Linux app.**
- **Third-party model providers** (Bedrock/Vertex/Foundry) require enterprise
  configuration; Desktop talks to Anthropic's API by default.
- Cowork sessions can't be shared, and scheduled tasks need the app open.

### Fable 5 specifics on Desktop

Fable 5 appears in the model dropdown (Chat and Code tabs) on paid plans. In Claude
Code surfaces it always uses extended thinking (`MAX_THINKING_TOKENS=0` has no
effect on it). Inclusion window: June 9–22, 2026 on Pro/Max/Team/seat-based
Enterprise; usage credits required from June 23. Anthropic says standard
subscription access will return "as quickly as we can" when capacity permits.
Note Fable 5 routes a small set of cybersecurity/biology requests to Opus 4.8
(~5% of sessions) — irrelevant for fiction work in practice, but the fallback
model note in a response is that, not a bug.

## Sources

- https://support.claude.com/en/articles/10065433-install-claude-desktop (2026-06-10)
- https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork (2026-06-10)
- https://code.claude.com/docs/en/desktop (2026-06-10)
- https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop (2026-06-10)
- https://www.anthropic.com/news/claude-fable-5-mythos-5 (2026-06-10)
- https://claude.com/product/cowork (2026-06-10)
- https://support.claude.com/en/articles/12138966-release-notes (2026-06-10 — Cowork GA April 9, 2026; Fable 5 June 9, 2026)
- https://support.claude.com/en/articles/12512180-use-skills-in-claude (2026-06-10, via search summary)
- https://modelcontextprotocol.io/docs/develop/connect-local-servers (2026-06-10 — claude_desktop_config.json paths)
- ⚠️ Unverified: press reports (The New Stack) of a doubled 5-hour Cowork usage
  limit June 5 – July 5, 2026 — not confirmed on an Anthropic page; treat as likely
  but check Settings → Usage.
- ⚠️ Unverified: global keyboard shortcuts for Chat/Cowork tabs (no official list found).
