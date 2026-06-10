# Which Claude Should I Open? A Decision Guide for Authors

> **In plain words:** Claude comes in four flavors — the website, the phone app, the
> Desktop app, and Claude Code. They share one account, one subscription, and mostly
> one brain. The difference is *what they can touch*: your manuscript files, your
> folders, your automations. This page tells you which door to walk through for each
> kind of author job.

## What it is

A "surface" is just the place you talk to Claude. Same Claude, different reach:

| Surface | Best at | Can it touch your files? | Automation features |
|---|---|---|---|
| **claude.ai (web)** | Quick chats, Projects, Artifacts, research with connectors | Only files you upload by hand | Skills, connectors (MCP), scheduled none |
| **Mobile app** | Ideas on the couch, voice brainstorming, reading drafts back | Uploads only; can *send tasks* to your desktop via Dispatch (Pro/Max) | Same chats/Projects as web |
| **Claude Desktop** | Everything web does **plus** hands-off file work (Cowork) and Claude Code in a window (Code tab) | Yes — folders you approve (Cowork), project folders (Code tab) | Cowork scheduled tasks, skills, connectors, desktop extensions, computer use |
| **Claude Code CLI** | Drafting pipelines inside a book project; scripting and repeatable automation | Yes — full read/write in your project folder | Skills, hooks, subagents, agent teams, `--print` scripting, cron-style jobs |

Think of it like your writing life: the **phone** is the notebook in your pocket,
the **website** is a café meeting with your editor, **Desktop** is the office with
an assistant who can actually open the filing cabinet, and the **CLI** is the
production floor where books get manufactured.

## Why authors care

- Picking the right surface saves rework: a brainstorm that should have been a
  Project, or a folder cleanup you did by hand because you didn't know Cowork existed.
- One paid plan (Pro/Max) covers all four — usage is shared, so heavy agentic work
  in one surface draws from the same pool.
- Your setup carries over more than you'd think: skills, MCP connectors, and (between
  Desktop's Code tab and the CLI) even your `CLAUDE.md` and settings are shared.

## Getting started

1. **Already have a paid plan?** Install [Claude Desktop](../02-power-features/claude-desktop.md)
   first — it's the superset surface for desk work (Chat + Cowork + Code tabs).
2. **Want drafting pipelines?** Set up Claude Code via
   [installation-setup](../01-claude-code-basics/installation-setup.md). If terminals
   put you off, skip the CLI and use the Code tab inside Desktop — same engine.
3. Put the mobile app on your phone for capture-anywhere brainstorming.
4. Then route each job using the flows below.

## Author use cases

Decision flows for the jobs that come up most:

**"Draft chapter 14 of my book project."**
→ **Claude Code** (CLI or Desktop's Code tab). It reads your story bible, dossier,
and previous chapters from the project folder before writing, and saves the draft
as a real file. Web/mobile would make you re-upload context every time.

**"Brainstorm series titles on the couch."**
→ **Mobile or web.** No file access needed; voice input on mobile is great for this.
Save keepers into a Project so they're there when you're back at your desk.

**"Organize my manuscript folder — five years of drafts — without typing commands."**
→ **Desktop, Cowork tab.** Point it at the folder, state the outcome ("sort by book,
rename consistently, flag duplicates, delete nothing"), approve the plan. No
terminal involved. Details in [claude-desktop.md](../02-power-features/claude-desktop.md).

**"Run my chapter pipeline with hooks, skills, and QA gates."**
→ **Claude Code CLI.** Hooks (automatic checks that fire at fixed points), agent
teams, and scripted `--print` runs are CLI-only. The Desktop Code tab runs skills
and most workflows, but the deterministic-automation layer lives in the terminal.

**"Iterate on my back-cover blurb until it sings."**
→ **Web or Desktop Chat tab**, using an Artifact. Versioned side-panel document,
fast to compare drafts, easy to copy out.

**"Keep a living workspace for one book — synopsis, agent feedback, comp research."**
→ **Projects** (web, mobile, or Desktop Chat). Upload the stable context once;
every chat in the Project knows it.

**"Build my ARC-team spreadsheet from these notes."**
→ **Desktop, Cowork.** It produces a real .xlsx with working formulas saved to disk.

**"Research chat that can see my Notion/Google Drive notes."**
→ **Web or Desktop Chat with connectors** (MCP). Same connectors work in Code
sessions too if your pipeline needs them.

**"Fix something while I'm out — start the job from my phone."**
→ **Mobile → Dispatch → Desktop** (Pro/Max). Message a task from the phone app;
your desktop at home runs it in Cowork or spawns a Code session, then pings you.

**"Long revision job I want running while my laptop is closed."**
→ **Claude Code cloud session** (start from the Code tab choosing "Remote", from
claude.ai/code, or the iOS app). Cloud sessions keep running when the app closes —
local Cowork tasks don't.

## Common pitfalls

- **Don't draft long manuscripts in plain web chat.** Without a project folder or
  Project knowledge, Claude forgets your canon between sessions and you'll paste
  context forever.
- **Cowork ≠ Code.** Cowork is for general file work (organizing, documents,
  spreadsheets); Code is for project-folder pipelines with version control. Cowork
  actually runs on the same agentic architecture as Claude Code — but the Code
  surfaces add Git, diffs, hooks, and CLAUDE.md discipline.
- **Usage is shared and agentic work is expensive.** Cowork tasks and long Code
  sessions burn allocation much faster than chat. Fable 5 is included on paid plans
  only through June 22, 2026; after that it needs usage credits.
- **Local tasks need the lid open.** Cowork tasks and local Code sessions stop if
  the app closes or the machine sleeps. Use cloud Code sessions for fire-and-forget.
- **Mobile can't do file work itself.** It can only *delegate* to a desktop that's
  awake, signed in, and has Dispatch set up.

## Advanced

The honest overlaps — capabilities that exist on more than one surface:

| Capability | Web | Mobile | Desktop (Chat/Cowork) | Desktop (Code tab) | Code CLI |
|---|---|---|---|---|---|
| Projects & Artifacts | ✅ | ✅ | ✅ | — | — |
| Skills | ✅ (Settings → Capabilities) | partial | ✅ | ✅ (shared with CLI) | ✅ |
| MCP / connectors | ✅ remote connectors | — | ✅ + local extensions (.mcpb) + `claude_desktop_config.json` | ✅ (reads Desktop config **and** `~/.claude.json` / `.mcp.json`) | ✅ (`.mcp.json`, `~/.claude.json`; does *not* read Desktop's config — import with `claude mcp add-from-claude-desktop`) |
| CLAUDE.md project memory | — | — | — | ✅ shared | ✅ shared |
| Hooks | — | — | — | ✅ (via settings files) | ✅ |
| Agent teams | — | — | — | — | ✅ |
| Scheduled/recurring tasks | — | — | ✅ Cowork `/schedule` | ✅ scheduled tasks | ✅ cron/scripting |
| Scripting (`--print`, SDK) | — | — | — | — | ✅ |
| Cloud sessions | view at claude.ai/code | ✅ monitor/start | — | ✅ "Remote" environment | ✅ |
| Computer use (screen control) | — | — | ✅ Cowork (paid) | ✅ research preview, Pro/Max | limited (macOS via /mcp) |

Notes for power users:

- **Skills are two ecosystems converging:** claude.ai/Desktop chat skills (managed
  under Customize → Skills, installable from the in-app directory) and Claude Code
  skills (folders in `~/.claude/skills` or project `.claude/skills`). The Code tab
  uses the Code ecosystem. Don't assume a chat-installed skill exists in your CLI,
  or vice versa.
- **Two sessions, one project:** you can run the CLI and Desktop Code tab
  simultaneously on the same project; they share config and CLAUDE.md but keep
  separate session histories. `/desktop` in the CLI hands the current session to
  the app.
- **Surface-by-feature config paths:** Desktop chat MCP →
  `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) /
  `%APPDATA%\Claude\claude_desktop_config.json` (Windows); Code (both forms) →
  `~/.claude.json`, `~/.claude/settings.json`, project `.mcp.json`.
- **Linux:** CLI only — there is no Desktop app for Linux.

Deep dives: [Claude Desktop](../02-power-features/claude-desktop.md) ·
[Claude Code installation & setup](../01-claude-code-basics/installation-setup.md)

## Sources

- https://code.claude.com/docs/en/desktop (2026-06-10 — tabs, Code tab vs CLI feature
  comparison, shared config, Dispatch, cloud sessions, computer use)
- https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork (2026-06-10)
- https://claude.com/product/cowork (2026-06-10)
- https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork (2026-06-10, via search summary — mobile Dispatch)
- https://support.claude.com/en/articles/12512180-use-skills-in-claude (2026-06-10, via search summary)
- https://www.anthropic.com/news/claude-fable-5-mythos-5 (2026-06-10 — Fable 5 plan
  inclusion through June 22, 2026)
- https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them (2026-06-10, via search summary — Artifacts on Free + paid)
- ⚠️ Unverified: exact extent of skills support in the mobile app ("partial" above is a
  conservative judgment, not an official matrix).
