# Claude Fable Starter Kit for Indie Authors

**An end-to-end educational wiki for fiction writers using Claude Fable 5 in Claude Code and Claude Desktop.**

Claude Fable 5 launched on June 9, 2026 — Anthropic's most capable generally available model, built for long, multi-step autonomous work. For an indie author, that means things like *"read all 28 chapters and fix every timeline error"* are now one request, not one afternoon. This repository is a self-contained starter kit that takes you from "never opened a terminal" to running multi-agent revision pipelines, with every claim verified against official Anthropic documentation (as of 2026-06-10).

> [!NOTE]
> **Who this is for.** Every page is written in two layers: a plain-language top half for authors who may be entirely non-technical, and an **Advanced** section at the bottom for power users who want the full configuration surface. Read to the depth you need and stop.

---

## 🚀 Start here

| If you are… | Read this first |
|---|---|
| Brand new to all of this | [Which Claude should I open?](docs/wiki/00-start-here/which-tool-when.md) — the four Claude surfaces and which fits each author job |
| Ready to install | [Installation & setup](docs/wiki/01-claude-code-basics/installation-setup.md) — terminal basics included, no experience assumed |
| Wondering what Fable 5 actually is | [The Fable 5 model guide](docs/fable-documentation/fable-5-model-guide.md) — capabilities, pricing, the June 22 inclusion deadline, and why it sometimes switches to Opus 4.8 |

**The suggested learning path:** which-tool-when → installation → CLAUDE.md & memory → settings & permissions → slash commands → then pick the power feature or workflow that matches your next real task.

---

## 📚 The wiki

### 00 — Start here
| Doc | What you'll learn |
|---|---|
| [Which tool when](docs/wiki/00-start-here/which-tool-when.md) | claude.ai vs mobile vs Desktop vs Claude Code CLI — decision flows for common author jobs |

### 01 — Claude Code basics
| Doc | What you'll learn |
|---|---|
| [Installation & setup](docs/wiki/01-claude-code-basics/installation-setup.md) | Installing on Mac/Windows, your first session, choosing models, how to stop things |
| [CLAUDE.md & memory](docs/wiki/01-claude-code-basics/claude-md-and-memory.md) | Teaching Claude your voice rules and series facts — permanently |
| [Settings & permissions](docs/wiki/01-claude-code-basics/settings-and-permissions.md) | Protecting your manuscript with rules Claude cannot talk its way past |
| [Slash commands](docs/wiki/01-claude-code-basics/slash-commands.md) | The ~10 commands you'll actually use, and the keyboard survival kit |

### 02 — Power features
| Doc | What you'll learn |
|---|---|
| [Skills](docs/wiki/02-power-features/skills.md) | Package your blurb formula or revision checklist so Claude follows it every time |
| [Hooks](docs/wiki/02-power-features/hooks.md) | Automatic guardrails: block edits to `originals/`, auto-backup every chapter, log word counts |
| [Subagents & orchestration](docs/wiki/02-power-features/subagents-and-orchestration.md) | Delegate to parallel copies of Claude — five chapter reviews in the time of one |
| [MCP](docs/wiki/02-power-features/mcp.md) | Connect Claude to Notion, Obsidian, spreadsheets, and your story bible |
| [Claude Desktop](docs/wiki/02-power-features/claude-desktop.md) | The Chat / Cowork / Code three-tab app — Claude Code without a terminal |

### 03 — Author workflows *(in progress)*
| Doc | What you'll learn |
|---|---|
| Drafting & revision | Story-bible-driven chapter pipelines, multi-pass audits, voice preservation |
| Publishing ops | Format conversion, metadata, proofing passes, release checklists |
| Marketing & launch | Manuscript-fed copy generation, blurb tournaments, launch runbooks |
| Research & worldbuilding | Genre research fan-outs, world wikis, timeline extraction |

### 04 — Reference *(in progress)*
| Doc | What you'll learn |
|---|---|
| Use-case catalog | The master table: every author use case × best surface × best mechanism × difficulty |

### Fable 5 documentation
| Doc | What it is |
|---|---|
| [Fable 5 model guide](docs/fable-documentation/fable-5-model-guide.md) | The wiki's comprehensive model reference, written for authors |
| [Launch announcement](docs/fable-documentation/Claude_Fable_5_and_Claude_Mythos_5_Anthropic.md) | Archived copy of Anthropic's June 9, 2026 announcement |
| [Launch email](docs/fable-documentation/fable-about.md) | Archived copy of the Claude Team launch email |

---

## ⏰ Time-sensitive: the Fable 5 inclusion window

Fable 5 is included **at no extra cost** on Pro, Max, Team, and seat-based Enterprise plans **through June 22, 2026**. From June 23 it requires usage credits until Anthropic restores standard access. If you're reading this during the window: try the big stuff now — a whole-manuscript continuity audit is the perfect test drive. Details in the [model guide](docs/fable-documentation/fable-5-model-guide.md).

---

## 🔍 How this wiki was built (and why you can trust it)

This kit was produced by a supervised multi-agent workflow — itself a demonstration of the orchestration techniques the wiki teaches:

1. **Parallel research agents** each owned one slice (skills, hooks, subagents, MCP, Desktop…) and verified every claim against live official sources — [code.claude.com/docs](https://code.claude.com/docs), [platform.claude.com/docs](https://platform.claude.com/docs), [support.claude.com](https://support.claude.com), and Anthropic announcements.
2. **An orchestrator session** reviewed every page in full for accuracy, consistency, and template compliance before it was committed.
3. **Anything that couldn't be verified against an official source is flagged inline** with ⚠️ rather than stated as fact. Every page ends with a dated Sources list.

The orchestration artifacts are public in [`workspace-agents/`](workspace-agents/) — the [implementation plan](workspace-agents/IMPLEMENTATION_PLAN.md), the [doc template & style guide](workspace-agents/DOC_TEMPLATE.md) every agent followed, and the [progress tracker](workspace-agents/PROGRESS.md). If you're learning multi-agent orchestration, that folder is a worked example.

> [!WARNING]
> Claude Code moves fast. Everything here was verified on **2026-06-10**; commands, settings, and feature names can change. Each page's Sources section tells you exactly where to re-check.

---

## 🗂 Repository map

```
docs/
├── fable-documentation/     # The model: guide + archived launch materials
└── wiki/
    ├── 00-start-here/       # Orientation and decision guides
    ├── 01-claude-code-basics/   # Install, memory, permissions, commands
    ├── 02-power-features/   # Skills, hooks, subagents, MCP, Desktop
    ├── 03-author-workflows/ # Drafting, publishing, marketing, research
    └── 04-reference/        # Use-case catalog
workspace-agents/            # How this wiki was built: plan, template, tracker
CLAUDE.md                    # Instructions for Claude Code sessions in this repo
```
