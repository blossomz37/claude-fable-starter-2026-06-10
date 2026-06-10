# The Claude Fable Starter Kit Wiki

> **In plain words:** This wiki takes a fiction author from "never opened a terminal" to running multi-agent revision pipelines with Claude Fable 5. Every page has a plain-language top half and an **Advanced** section at the bottom — read to the depth you need and stop. Every platform claim was verified against official Anthropic documentation (as of 2026-06-10); anything we could not verify is marked ⚠️.

## The suggested learning path

Follow this order if you're new. Stop at any point — each stage leaves you with something useful.

**Stage 1 — Orient (no installation needed)**
1. [Which tool when](00-start-here/which-tool-when.md) — claude.ai vs mobile vs Desktop vs Claude Code, and which fits each author job.
2. [Quick start](00-start-here/quick-start.md) — your first 30 minutes, including the **one-folder book project** layout the whole wiki builds on.
3. [Managing usage and cost](00-start-here/managing-usage-and-cost.md) — read this *early*. Usage limits are real, and five habits make your plan last dramatically longer.

**Stage 2 — Set up your workshop**
4. [Installation & setup](01-claude-code-basics/installation-setup.md) — terminal basics included, no experience assumed.
5. [CLAUDE.md & memory](01-claude-code-basics/claude-md-and-memory.md) — how Claude remembers your project, voice, and rules.
6. [Settings & permissions](01-claude-code-basics/settings-and-permissions.md) — what Claude may touch, and how to say so once instead of every time.
7. [Slash commands](01-claude-code-basics/slash-commands.md) — the built-in commands you'll actually use.

**Stage 3 — Do real author work** (pick the one matching your next task)
8. [Drafting & revision](03-author-workflows/drafting-and-revision.md) — story bible, chapter pipelines, continuity passes.
9. [Research & worldbuilding](03-author-workflows/research-and-worldbuilding.md) — research notes, world files, fact tracking.
10. [Publishing ops](03-author-workflows/publishing-ops.md) — manuscript to EPUB/print, metadata, retailer prep.
11. [Marketing & launch](03-author-workflows/marketing-and-launch.md) — blurbs, ads, launch plans, imagery.

**Stage 4 — Power features** (when a workflow doc says "this can be packaged as a…")
12. [Skills](02-power-features/skills.md) — turn a repeated prompt into a reusable, shareable command.
13. [Subagents & orchestration](02-power-features/subagents-and-orchestration.md) — parallel helpers that do heavy reading without burning your session.
14. [Hooks](02-power-features/hooks.md) — automatic checks that run without being asked.
15. [MCP](02-power-features/mcp.md) — connect Claude to outside tools and services.
16. [Claude Desktop](02-power-features/claude-desktop.md) — Chat, Cowork, and Code outside the terminal.

**Stage 5 — Go further**
17. [Building, adopting, and sharing author tools](03-author-workflows/adopting-and-sharing-tools.md) — adopt another author's shared tool safely, customize it, share yours back; plus when an idea should become a skill, script, MCP server, or app.
18. [Use-case catalog](04-reference/use-case-catalog.md) — 100+ concrete author use cases in one master table, including the Multimedia category (audiobook narration, cover imagery via APIs).

Stuck on a word? The [Glossary](00-start-here/glossary.md) defines every technical term in the wiki in plain language.

## Map of contents

| Section | Docs |
|---|---|
| **00 — Start here** | [Which tool when](00-start-here/which-tool-when.md) · [Quick start](00-start-here/quick-start.md) · [Managing usage and cost](00-start-here/managing-usage-and-cost.md) · [Glossary](00-start-here/glossary.md) |
| **01 — Claude Code basics** | [Installation & setup](01-claude-code-basics/installation-setup.md) · [CLAUDE.md & memory](01-claude-code-basics/claude-md-and-memory.md) · [Settings & permissions](01-claude-code-basics/settings-and-permissions.md) · [Slash commands](01-claude-code-basics/slash-commands.md) |
| **02 — Power features** | [Skills](02-power-features/skills.md) · [Hooks](02-power-features/hooks.md) · [MCP](02-power-features/mcp.md) · [Subagents & orchestration](02-power-features/subagents-and-orchestration.md) · [Claude Desktop](02-power-features/claude-desktop.md) |
| **03 — Author workflows** | [Drafting & revision](03-author-workflows/drafting-and-revision.md) · [Research & worldbuilding](03-author-workflows/research-and-worldbuilding.md) · [Publishing ops](03-author-workflows/publishing-ops.md) · [Marketing & launch](03-author-workflows/marketing-and-launch.md) · [Building, adopting & sharing tools](03-author-workflows/adopting-and-sharing-tools.md) |
| **04 — Reference** | [Use-case catalog](04-reference/use-case-catalog.md) |

Background on the model itself lives outside the wiki in [the Fable 5 model guide](../fable-documentation/fable-5-model-guide.md) — capabilities, pricing, the June 22 inclusion window, and why it sometimes hands off to Opus 4.8.

## How this wiki was built

The wiki is itself a demonstration of what it teaches: it was researched and written by parallel Claude subagents working from a shared plan and template, with every page QA-read by an orchestrating session and platform claims verified against [code.claude.com/docs](https://code.claude.com/docs), [platform.claude.com/docs](https://platform.claude.com/docs), and [support.claude.com](https://support.claude.com) on 2026-06-10. Claims we could not confirm from an official source are marked ⚠️ in place rather than silently guessed.
