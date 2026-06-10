# Glossary: Every Technical Term in This Wiki, in Plain Language

> **In plain words:** Every technical term used anywhere in this wiki, defined for
> an author who has never opened a terminal. Each entry says what the thing is in
> 1–3 sentences, often with an author-world analogy, and links to the wiki page
> that covers it in depth. Skim it once now; come back whenever a doc uses a word
> you don't recognize.

This is a reference page, not a tutorial — entries are alphabetical, grouped by
letter. Terms in **bold** inside a definition usually have their own entry.

---

## Symbols

**⚠️ (warning flag)** — This wiki's honesty convention. In a doc's Sources section,
"⚠️ Unverified:" marks a claim the author could not confirm against an official
source; in tables (like the [use-case catalog](../04-reference/use-case-catalog.md)),
⚠️ marks a use case that depends on something unverified. Treat flagged items as
"probably right, check before relying on it."

**@-mention / @-import** — Typing `@` in Claude Code pulls a specific file into the
conversation (`look at @chapters/ch07.md`), and an `@path/to/file` line inside a
CLAUDE.md file imports that file automatically every session — how a story bible
gets loaded without re-pasting. See
[CLAUDE.md and memory](../01-claude-code-basics/claude-md-and-memory.md).

## A

**acceptEdits** — A permission mode where Claude applies file edits without asking
each time, inside your project folder. Use it after you've agreed on a list of line
edits and don't want twenty confirmation prompts. See
[Settings and permissions](../01-claude-code-basics/settings-and-permissions.md).

**ADAPTING.md** — This wiki's convention for shared author tools: a self-onboarding
interview file. A new user tells their Claude "read ADAPTING.md and onboard me,"
and it asks them the questions needed to configure the tool. See
[Adopting and sharing tools](../03-author-workflows/adopting-and-sharing-tools.md).

**Aeon Timeline** — A commercial timeline app popular with novelists. Claude can
extract your draft's chronology into a CSV file that Aeon imports directly. See
[Research and worldbuilding](../03-author-workflows/research-and-worldbuilding.md).

**Agent SDK** — A programmer's library (Python and TypeScript) that exposes Claude
Code's agent machinery so developers can build their own apps on it. Power-user
territory; most authors never need it. See
[Subagents and orchestration](../02-power-features/subagents-and-orchestration.md).

**Agent teams** — An experimental Claude Code feature: multiple coordinated sessions
with a shared task list that message each other, managed by a lead agent. CLI-only.
See [Subagents and orchestration](../02-power-features/subagents-and-orchestration.md).

**AI-facing dossier** — A story bible reorganized for a reader with no intuition:
explicit, structured, ruthless about what must never be contradicted. The form of
story bible Claude drafts best from. See
[Drafting and revision](../03-author-workflows/drafting-and-revision.md).

**API (Application Programming Interface)** — The pay-per-use doorway programs use
to talk to Claude directly, as an alternative to a subscription. API users pay per
**token** instead of having plan limits. See
[Managing usage and cost](managing-usage-and-cost.md).

**API key** — A long secret code that proves to a service (Claude's API, ElevenLabs,
Airtable) that a request comes from your account. Treat it like a signed blank
check: keep it in environment variables, never in files you share or commit. See
[MCP](../02-power-features/mcp.md).

**ARC team (Advance Reader Copy team)** — The readers who get your book early in
exchange for honest reviews. Their tracking spreadsheets and email sequences are
classic Claude jobs. See
[Marketing and launch](../03-author-workflows/marketing-and-launch.md).

**Artifact** — A versioned side-panel document in claude.ai and Claude Desktop chat.
Ideal for iterating short copy — blurbs, taglines, bios — because versions stack
and you can flip between them. See
[Claude Desktop](../02-power-features/claude-desktop.md).

**Auto memory** — Notes Claude writes for itself as it works with you: corrections
you made, preferences it noticed, how your project is laid out. On by default,
stored per project, fully readable and editable via `/memory`. See
[CLAUDE.md and memory](../01-claude-code-basics/claude-md-and-memory.md).

## B

**Background session** — A whole independent Claude Code session you dispatch and
monitor from one screen ("format the paperback interior") that keeps running after
you close the terminal. See
[Subagents and orchestration](../02-power-features/subagents-and-orchestration.md).

**bypassPermissions ("yolo mode")** — The permission mode with no approval prompts
at all. The docs are blunt: only use it in isolated environments where Claude can't
cause damage — almost no author needs it. See
[Settings and permissions](../01-claude-code-basics/settings-and-permissions.md).

## C

**Checkpoint** — See **Rewind**.

**claude.ai** — Claude in a browser tab: chat, Projects, Artifacts, connectors. It
never touches your hard drive directly — you upload and download files by hand.
See [Which tool, when](which-tool-when.md).

**Claude Code** — Anthropic's "agentic" assistant that works directly with the files
on your computer — your manuscript, story bible, blurbs — instead of making you
copy-paste into a chat box. Runs in the terminal (the full version), in Claude
Desktop's Code tab, in code editors, and on the web. See
[Quick start](quick-start.md) and
[Installation and setup](../01-claude-code-basics/installation-setup.md).

**Claude Desktop** — The installed Claude app for Mac and Windows. Everything the
website does, plus three tabs: **Chat** (conversation), **Cowork** (hands-off file
work in folders you approve), and **Code** (Claude Code without a terminal). See
[Claude Desktop](../02-power-features/claude-desktop.md).

**CLAUDE.md** — A plain text file in your book folder that Claude Code reads at the
start of every session — the note you leave on the assistant's desk: voice rules,
series facts, file layout, standing orders. The AI-facing page of your story bible.
A `CLAUDE.local.md` variant holds personal notes not shared with collaborators. See
[CLAUDE.md and memory](../01-claude-code-basics/claude-md-and-memory.md).

**CLI (command-line interface)** — A program you operate by typing commands instead
of clicking — Claude Code's original and most fully featured form. See
[Installation and setup](../01-claude-code-basics/installation-setup.md).

**Cloud session** — A Claude Code session that runs on Anthropic's servers instead
of your machine, so it keeps working after you close the laptop. Start one from the
Code tab ("Remote"), claude.ai/code, or the iOS app. See
[Which tool, when](which-tool-when.md).

**Code tab** — Claude Code inside Claude Desktop: same engine as the CLI, shares
your CLAUDE.md and settings, but with windows, visible diffs, and no terminal. See
[Claude Desktop](../02-power-features/claude-desktop.md).

**Comp title (comparable title)** — A published book similar to yours, used to
position your book in the market ("for fans of X meets Y"). Comp research is a
flagship subagent job. See
[Research and worldbuilding](../03-author-workflows/research-and-worldbuilding.md).

**Compaction** — What Claude Code does when the **context window** fills up: it
summarizes the conversation so far and continues from the summary. Details can blur
in the summary — which is why rules that matter belong in CLAUDE.md (re-read from
disk afterward), not in chat. `/compact` triggers it deliberately, with focus
instructions. See
[CLAUDE.md and memory](../01-claude-code-basics/claude-md-and-memory.md).

**Connector** — The claude.ai / Claude Desktop name for an **MCP** connection to
another service (Notion, Google Drive, Slack), set up with a click instead of a
command. See [MCP](../02-power-features/mcp.md).

**Console (Anthropic Console)** — The web dashboard for API accounts: usage and
cost pages, API keys, spend limits. Where the authoritative bill lives if you pay
per token. See [Managing usage and cost](managing-usage-and-cost.md).

**Context window** — Claude's working memory during a session, with a hard size
limit — a desk that only holds so many pages. Your messages, the chapters it reads,
and its own replies all pile onto that desk (roughly 200,000 tokens — about 150,000
words — on standard models; 1 million on Fable 5). When it fills, **compaction**
kicks in. See
[CLAUDE.md and memory](../01-claude-code-basics/claude-md-and-memory.md).

**Cowork** — Claude Desktop's hands-off tab for multi-step file work: point it at a
folder, state the outcome ("sort by book, rename consistently, delete nothing"),
approve its plan. Produces real Word docs, spreadsheets with working formulas, and
organized folders. See [Claude Desktop](../02-power-features/claude-desktop.md).

**CSV (comma-separated values)** — The simplest spreadsheet file format: plain text,
one row per line. The interchange format for timelines (Aeon Timeline imports CSVs)
and royalty exports. See
[Research and worldbuilding](../03-author-workflows/research-and-worldbuilding.md).

**CUSTOMIZATIONS.md** — This wiki's convention for adopted tools: a dated log of
every change you made versus the original, so when the original author ships an
update you can re-apply your changes cleanly. See
[Adopting and sharing tools](../03-author-workflows/adopting-and-sharing-tools.md).

## D

**Deny rule** — A written permission rule that makes something impossible, not just
discouraged — `"Edit(originals/**)"` means Claude *cannot* edit that folder, no
matter what. The lock, where CLAUDE.md is the polite request. See
[Settings and permissions](../01-claude-code-basics/settings-and-permissions.md).

**Deterministic** — "Always happens, exactly the same way." A script or **hook** is
deterministic; an instruction Claude reads and interprets is not. This wiki's rule:
deterministic checks become scripts or hooks, judgment checks stay as prompts. See
[Hooks](../02-power-features/hooks.md).

**Diff** — A before-and-after view of a proposed file change, shown so you can
approve or decline it. Reviewing diffs instead of trusting bulk edits is a core
safety habit here. See [Publishing ops](../03-author-workflows/publishing-ops.md).

**Dispatch** — A Claude feature (Pro/Max): message a task from the phone app and
your desktop at home runs it — in Cowork or a Code session — then pings you. See
[Claude Desktop](../02-power-features/claude-desktop.md).

**DOCX** — Microsoft Word's file format — what editors and many submission systems
expect. **Pandoc** converts Markdown ⇄ DOCX; Anthropic's document skills work
*inside* Word files when style fidelity matters. See
[Publishing ops](../03-author-workflows/publishing-ops.md).

## E

**Effort level** — A dial for how hard a model thinks before answering
(`low` → `max`), set with `/effort`. Thinking is billed as output tokens, so lower
effort on routine passes saves usage; on Fable 5 thinking can't be switched off —
effort is the only dial. See [Managing usage and cost](managing-usage-and-cost.md)
and the [Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

**ElevenLabs** — A text-to-speech service with an official API. Claude can run a
pipeline that turns chapter files into audio narration drafts — billed per
character, separately from Claude. See
[Publishing ops](../03-author-workflows/publishing-ops.md).

**Engine / conventions / personal (the three layers)** — This wiki's model of any
shared author tool: the **engine** (generic logic anyone could use), the
**conventions** (genre and workflow defaults a user might swap), and the
**personal** layer (pen names, paths, voice — things that are *you*). Tools break
when they travel because the personal layer is welded to the engine. See
[Adopting and sharing tools](../03-author-workflows/adopting-and-sharing-tools.md).

**EPUB** — The standard ebook file format that retailers like KDP accept. Pandoc
builds valid EPUBs straight from Markdown chapters. See
[Publishing ops](../03-author-workflows/publishing-ops.md).

**EPUBCheck** — The industry-standard validator that checks an EPUB file for errors
before you upload it. Claude can install it, run it, and translate its error
messages into plain English. See
[Publishing ops](../03-author-workflows/publishing-ops.md).

**Extended thinking** — A model's ability to reason privately before answering.
Fable 5 always thinks (it can't be disabled); you control depth with the **effort
level**. Thinking tokens count as output tokens on your bill. See the
[Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

## F

**Fable 5 (`claude-fable-5`)** — Anthropic's most capable generally available model
(launched June 9, 2026): built for long autonomous jobs like whole-manuscript
audits, with a 1M-token context window. The most expensive model ($10/$50 per
million tokens in/out on the API); included free on paid plans only through
June 22, 2026, then usage credits. Never the default — you select it deliberately.
See the [Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

**Fan-out / fan-in** — The orchestration pattern: spawn several **subagents** in
parallel on independent slices (one per chapter, one per comp title), then one
agent synthesizes their reports. Best for breadth-first work; expensive (~15× chat
tokens). See
[Subagents and orchestration](../02-power-features/subagents-and-orchestration.md).

**Fork** — `/fork` spawns a subagent that *inherits* your full conversation instead
of starting blank — for side quests ("draft three alternate endings from here")
that need everything discussed so far. See
[Subagents and orchestration](../02-power-features/subagents-and-orchestration.md).

**Frontmatter** — The metadata block between `---` markers at the top of a file
(written in **YAML**). In a skill it holds the name and trigger description; in
subagent files it sets tools and models; in rules files it scopes which files a
rule applies to. See [Skills](../02-power-features/skills.md).

## G

**Ghost draft** — Documenting the *implied but never stated* layer of a story —
off-page history, what characters know but won't say, the power dynamics under
polite dialogue — so the AI can write scenes *around* subtext instead of announcing
it. The biggest single lever for show-don't-tell. See
[Drafting and revision](../03-author-workflows/drafting-and-revision.md).

**Git** — A version-control system: it keeps a full history of every change to the
files in a folder, like Track Changes for an entire project. Useful background for
authors mainly as backup and sharing infrastructure; beware that anything ever
*committed* to git history stays retrievable even after deletion. See
[Adopting and sharing tools](../03-author-workflows/adopting-and-sharing-tools.md).

**GitHub** — The most popular website for hosting git **repositories** — where
authors share tools, skills, and starter kits with each other. See
[Adopting and sharing tools](../03-author-workflows/adopting-and-sharing-tools.md).

**Glob pattern** — Wildcard path matching used in permission rules and frontmatter:
`*` matches anything in a name, `**` matches whole folder trees — so
`Edit(originals/**)` covers everything inside `originals/`. See
[Settings and permissions](../01-claude-code-basics/settings-and-permissions.md).

## H

**Haiku** — The fastest, cheapest Claude model ($1/$5 per million tokens). The right
brain for bulk mechanical work — searching, counting, first-pass summaries — routed
via cheap subagents. See the
[Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

**Hallucination** — When an AI produces confident, specific, *wrong* facts —
invented book titles, false period details, misremembered quotes. The occupational
hazard of research; the antidote is citations plus your own spot-checks. See
[Research and worldbuilding](../03-author-workflows/research-and-worldbuilding.md).

**Hook** — A small rule that runs automatically at a fixed moment ("every time
Claude edits a file, make a backup first"). Unlike CLAUDE.md instructions, a hook
is enforced by the app itself — it fires every single time, no exceptions. The
copyeditor who checks every page without being asked. See
[Hooks](../02-power-features/hooks.md).

## I

**Ideogram** — An image-generation service whose documented strength is legible
text *inside* images (titles and taglines on ad cards). It has an official API and
a hosted MCP server, so Claude can drive it. Bills separately from Claude. See
[Marketing and launch](../03-author-workflows/marketing-and-launch.md).

**ISBN** — The unique identifier assigned to each edition and format of a published
book. Tracking which ISBN went to which title/format is classic spreadsheet work
for Cowork. See [Publishing ops](../03-author-workflows/publishing-ops.md).

## J

**JSON** — A strict text format for structured data, used by Claude Code's settings
and hook configuration files. Unforgiving: one stray comma breaks the whole file —
which is why this wiki suggests letting Claude write the JSON and you review it.
See [Hooks](../02-power-features/hooks.md).

**jq** — A small free command-line tool that reads JSON — the one extra install
most hook scripts in this wiki need (`brew install jq` on macOS). See
[Hooks](../02-power-features/hooks.md).

## K

**KDP (Kindle Direct Publishing)** — Amazon's self-publishing platform. The wiki
covers its metadata limits (categories, keywords), description HTML rules, spine
specs, and AI-disclosure policy — always verify current numbers in your own KDP
dashboard. See [Publishing ops](../03-author-workflows/publishing-ops.md).

## M

**Managed Agents** — Anthropic's hosted platform for long-running production agents
without running your own infrastructure. The cloud-scale cousin of the local
orchestration in this wiki; most authors only need to know it exists. See
[Subagents and orchestration](../02-power-features/subagents-and-orchestration.md).

**Markdown** — Plain text with simple symbols for formatting (`#` for headings,
`**bold**`). The native format of this whole wiki's workflows: chapters, bibles,
CLAUDE.md, and skills are all Markdown — readable in any text editor, in Obsidian,
and by Claude. See [Quick start](quick-start.md).

**Marketing bible** — This wiki's convention: one source-of-truth file
(`marketing/marketing-bible.md`) holding your approved blurbs, taglines, personas,
and comps. Every channel's copy is generated *from* it, so everything stays
consistent. The marketing cousin of your story bible. See
[Marketing and launch](../03-author-workflows/marketing-and-launch.md).

**MCP (Model Context Protocol)** — An open standard — think USB-C for AI apps —
that lets Claude connect to your other tools and accounts: Notion, Obsidian, Slack,
spreadsheets. You give Claude a key to specific rooms instead of copy-pasting
between apps. See [MCP](../02-power-features/mcp.md).

**MCP server** — One MCP connection — the key to one room. One server for Notion,
one for your file system, one for Slack. Each can offer Claude tools (actions),
resources (readable data), and prompts (templates). See
[MCP](../02-power-features/mcp.md).

**.mcpb (MCP Bundle / desktop extension)** — A one-click installable package that
adds a local MCP server to Claude Desktop, installed under Settings → Extensions.
(Older `.dxt` files are the same format under its legacy name.) See
[MCP](../02-power-features/mcp.md).

**Metadata** — Data *about* the book rather than the book itself: title, author,
series, categories, keywords, blurb. Lives in your retailer dashboard and, for
builds, in a `metadata.yaml` file pandoc reads when generating EPUBs. See
[Publishing ops](../03-author-workflows/publishing-ops.md).

**Model** — The "brain" answering you. The current family: **Fable 5** (most
capable, most expensive), **Opus 4.8**, **Sonnet 4.6**, **Haiku 4.5** (fastest,
cheapest). Switch with `/model`; match the model to the step. See
[Installation and setup](../01-claude-code-basics/installation-setup.md) and the
[Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

**Mythos 5** — The same underlying model as Fable 5 with some safeguards lifted,
restricted to vetted cybersecurity organizations and select researchers. You won't
use it and don't need it. See the
[Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

## N

**NPE (Narrative Physics Engine)** — Carlo's story-development method: modeling a
story through constraints, tension axes, and narrative "gravity" (all metaphorical)
instead of plot summaries. Functions like a story bible, but AI-facing — constraints
steer an AI better than summaries. See
[Drafting and revision](../03-author-workflows/drafting-and-revision.md).

## O

**OAuth** — The browser sign-in flow ("Continue with Notion…") used when connecting
services. Safer than API keys: Claude never sees your password, and you can revoke
access from the service's side. See [MCP](../02-power-features/mcp.md).

**Obsidian** — A free notes app built on folders of Markdown files. The natural
home for a worldbuilding wiki: open your project folder as a vault and you get a
clickable graph of your world while Claude keeps editing the same files. See
[Research and worldbuilding](../03-author-workflows/research-and-worldbuilding.md).

**One-folder book project** — This wiki's canonical layout: one folder per book
holding `manuscript/`, `bible/`, `marketing/`, `output/`, and the rest, so every
workflow guide slots in without restructuring. (The drafting guide's worked example
calls the chapters folder `chapters/` — same folder, same job as `manuscript/`.)
See [Quick start](quick-start.md).

**OpenTelemetry (OTel)** — A monitoring standard Claude Code can export usage
metrics to, so API users running scripted pipelines (a nightly chapter-audit job)
can see exactly what each step costs on a dashboard. See
[Managing usage and cost](managing-usage-and-cost.md).

**Opus 4.8** — Anthropic's previous top model, still excellent for complex work
($5/$25 per million tokens) — and the model Fable 5 quietly hands flagged requests
to (see **safety classifiers**). See the
[Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

**Orchestration / orchestrator** — Running a multi-agent workflow: a main session
(the managing editor) plans, delegates slices to subagents (freelance editors),
and merges their reports. See
[Subagents and orchestration](../02-power-features/subagents-and-orchestration.md).

**originals/ and published/** — The two write-protected folders in the canonical
layout: `originals/` is your untouchable pre-AI archive, `published/` is what
actually shipped. The convention: Claude never writes in either; everything it
generates lands in `output/`, and only you promote files. Enforced with deny rules
plus hooks. See [Quick start](quick-start.md) and
[Publishing ops](../03-author-workflows/publishing-ops.md).

## P

**Pandoc** — The free, open-source document converter that is still the standard
tool for Markdown ⇄ DOCX ⇄ EPUB. A converter, not a typesetter: clean ebooks and
interchange files, not print-grade interiors. See
[Publishing ops](../03-author-workflows/publishing-ops.md).

**Permission mode** — Claude Code's overall posture toward asking first, cycled
with `Shift+Tab`: `default` (asks), `acceptEdits` (auto-approves edits), `plan`
(read-only), `bypassPermissions` (never asks — dangerous). See
[Settings and permissions](../01-claude-code-basics/settings-and-permissions.md).

**Permission rules** — Written allow/ask/deny lists in settings files, for decisions
made once and enforced forever ("never edit `originals/`"). Enforced by the app
itself — Claude cannot talk its way past a **deny rule**. See
[Settings and permissions](../01-claude-code-basics/settings-and-permissions.md).

**Plan mode** — The read-only permission mode: Claude can read and discuss your
whole book while being physically unable to change a word. One keystroke
(`Shift+Tab`, or `/plan`) gives you a beta reader who can see everything and touch
nothing. See
[Settings and permissions](../01-claude-code-basics/settings-and-permissions.md).

**Plan tiers (Free / Pro / Max / Team / Enterprise)** — Claude's subscription
levels. Claude Code, Cowork, and the Code tab require a paid plan (or an API
account); the free plan is chat-only. Usage is shared across all surfaces on one
plan. See [Installation and setup](../01-claude-code-basics/installation-setup.md)
and [Which tool, when](which-tool-when.md).

**Plugin** — A package that bundles skills, hooks, agents, and MCP config together
for one-command installation (`/plugin install …`), optionally published through a
marketplace. The step up from sharing a repo. See
[Skills](../02-power-features/skills.md).

**PreToolUse / PostToolUse** — The two hook moments you'll use most: *before* a
tool call (can block it — manuscript protection) and *after* it succeeds (reacts —
automatic backups, word-count logging). See
[Hooks](../02-power-features/hooks.md).

**PROFILE.md** — This wiki's convention for shared tools: one plain file holding
every user-specific value — pen name, genre, folder paths, voice notes — so the
rest of the tool stays generic. One file to edit when the tool changes hands. See
[Adopting and sharing tools](../03-author-workflows/adopting-and-sharing-tools.md).

**Progressive disclosure** — Why skills are cheap: Claude always sees a one-line
description of every installed skill (a table of contents), but the full
instructions load only when actually needed. See
[Skills](../02-power-features/skills.md).

**Prompt** — Simply what you type to Claude — a request in plain English. The
bottom rung of this wiki's tool ladder: most ideas should stay prompts before
becoming skills, scripts, or servers. See
[Adopting and sharing tools](../03-author-workflows/adopting-and-sharing-tools.md).

**Prompt caching** — An automatic discount: repeated content re-sent every turn
(conversation history) is billed at a reduced rate. It softens, but doesn't
eliminate, the cost of long sessions. See
[Managing usage and cost](managing-usage-and-cost.md).

**Prompt injection** — A security risk: untrusted content Claude reads (a web page,
an email) containing hidden instructions ("ignore previous instructions and…").
Be most careful with MCP servers that both read untrusted content *and* can take
actions. See [MCP](../02-power-features/mcp.md).

**Project (claude.ai / Desktop)** — A persistent workspace in chat: upload your
series bible and notes once, and every conversation inside the Project already
knows them. The fastest first win for series Q&A. See
[Claude Desktop](../02-power-features/claude-desktop.md) and
[Which tool, when](which-tool-when.md).

## R

**Repository (repo)** — A project folder tracked by **git**, often hosted on
GitHub. How author tools, cohort starter kits, and shared setups travel between
people. See
[Adopting and sharing tools](../03-author-workflows/adopting-and-sharing-tools.md).

**Rewind (`/rewind`, aliases `/checkpoint`, `/undo`)** — Claude Code's undo button:
restore files and conversation to an earlier checkpoint when an edit pass goes
wrong. See [Slash commands](../01-claude-code-basics/slash-commands.md).

**Routine** — A scheduled session that runs in Anthropic's cloud on a timer — a
nightly word-count report, for instance — even with your laptop off. See
[Subagents and orchestration](../02-power-features/subagents-and-orchestration.md).

## S

**Safety classifiers** — Checks Fable 5 runs on every request. If a request looks
like offensive cybersecurity or sensitive biology/chemistry (your hacker thriller,
your engineered-plague sci-fi), the answer is handled by **Opus 4.8** instead —
clearly labeled, expected, harmless, and still a strong answer. Over 95% of
sessions never hit it. See the
[Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

**Session** — One continuous conversation with Claude in one folder — one sitting
with an assistant. Each starts with a blank conversational memory (memory files
reload automatically); quit and it's saved, resume with `claude -c` or `/resume`.
Shorter sessions are cheaper *and* sharper. See
[Installation and setup](../01-claude-code-basics/installation-setup.md).

**Settings files (`settings.json`)** — Small JSON files holding permission rules,
hooks, model defaults, and other configuration: `~/.claude/settings.json` (all your
projects), `.claude/settings.json` (this project, shareable), and
`.claude/settings.local.json` (this project, just you). You mostly never edit them
by hand — `/permissions` and `/config` do it for you. See
[Settings and permissions](../01-claude-code-basics/settings-and-permissions.md).

**Skill** — A reusable instruction packet: a folder with a `SKILL.md` file that
Claude loads only when needed — the laminated procedure card in a drawer ("here's
exactly how I write blurbs"). Triggered automatically when relevant, or by typing
`/skill-name`. See [Skills](../02-power-features/skills.md).

**Slash command** — A message starting with `/` that operates the app itself rather
than talking to Claude — `/model`, `/clear`, `/usage`. The menu also includes your
own skills; in Claude Code, custom commands have merged into skills. See
[Slash commands](../01-claude-code-basics/slash-commands.md).

**Sonnet** — The middle Claude model: best balance of speed and intelligence for
everyday drafting work, at roughly a third of Fable 5's price. The default on Pro
plans. See the
[Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

**Story bible / series bible** — Your record of canon: characters, timeline, world
rules, who-knows-what. In this wiki it lives as files in `bible/` (and a shared
`series-bible/` one level up for a series), loaded via CLAUDE.md so Claude reads it
before drafting. See
[Drafting and revision](../03-author-workflows/drafting-and-revision.md).

**Subagent** — A fresh copy of Claude that your main session hands a task to — a
freelance copyeditor hired per job. It works in its own clean **context window**
and returns only a summary, so heavy reading never clutters (or re-bills) your main
conversation. Several can run in parallel. See
[Subagents and orchestration](../02-power-features/subagents-and-orchestration.md).

**Surface** — This wiki's word for *where* you talk to Claude: the website, the
phone app, Claude Desktop, or Claude Code. Same Claude, different reach into your
files. See [Which tool, when](which-tool-when.md).

## T

**Terminal** — The text-based command window on your computer (Terminal on macOS,
PowerShell on Windows): you type a request, press Enter, text comes back. That's
all it is — and it's where the CLI form of Claude Code lives. See
[Installation and setup](../01-claude-code-basics/installation-setup.md).

**Token** — The unit AI usage is measured in: a chunk of text, roughly ¾ of a word.
**Input tokens** are everything Claude must read before answering (including the
whole conversation so far, re-sent every turn); **output tokens** are everything it
writes back, including its private thinking. See
[Managing usage and cost](managing-usage-and-cost.md).

**Tool (Claude's tools)** — The named actions Claude Code can take: `Read`, `Edit`,
`Write`, `Bash` (shell commands), `WebFetch`, and MCP tools. Permission rules are
written against these names — `Edit(originals/**)`, `Bash(rm *)`. See
[Settings and permissions](../01-claude-code-basics/settings-and-permissions.md).

**Tool Search** — Claude Code's trick for connecting many MCP servers without
draining the context window: only tool *names* load at startup, full definitions
load on demand. See [MCP](../02-power-features/mcp.md).

## U

**Usage credits** — Pay-as-you-go top-ups (at API rates) for things a subscription
no longer includes — notably Fable 5 on paid plans after June 22, 2026. See the
[Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

**Usage limits** — The cap on how much Claude you can use per period on a
subscription plan, shared across every surface. Long agentic sessions burn through
them fastest; `/usage` shows where you stand. See
[Managing usage and cost](managing-usage-and-cost.md).

## V

**Vellum** — A Mac-only book-formatting app many indies use for print and ebook
interiors. Claude doesn't replace it — it cleans the input (heading styles, scene
breaks, smart quotes) so Vellum's import doesn't fight you. Atticus is the usual
cross-platform alternative. See
[Publishing ops](../03-author-workflows/publishing-ops.md).

**Vision** — A model's ability to read images. Fable 5's is best-in-class: cover
comps, Plottr/Aeon screenshots, handwritten notebook pages, KDP dashboard
screenshots. See the
[Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

**Voice firewall** — This wiki's name for the CLAUDE.md section that protects your
prose voice: "my fragments and comma splices are deliberate — keep them; do not
homogenize." Applied to every session forever, so edit passes preserve you. See
[Drafting and revision](../03-author-workflows/drafting-and-revision.md).

## W

**world/ vs research/** — The wiki's canon discipline: `research/` holds what the
world says (cited, dated, *provisional*), `world/` holds what your story says
(established, chapter-cited, *canon*). Nothing moves from research to canon until
you have verified it. See
[Research and worldbuilding](../03-author-workflows/research-and-worldbuilding.md).

**Worktree** — A temporary parallel copy of a git project that lets an agent or a
second session work without touching your live files. Used automatically for
parallel Code-tab sessions; available to subagents via `isolation: worktree`. See
[Subagents and orchestration](../02-power-features/subagents-and-orchestration.md).

## Y

**YAML** — A human-friendly format for structured settings, written as
`key: value` lines. Where you meet it here: skill and subagent **frontmatter**,
and `metadata.yaml` for ebook builds. See [Skills](../02-power-features/skills.md).

---

## Sources

- Definitions are derived from the wiki docs themselves (the 18 pages under
  `docs/wiki/` and the model guide in `docs/fable-documentation/`), each of which
  carries its own official-source citations. Accessed 2026-06-10.
- Where a term's external facts were not stated in the wiki, it is defined
  generically here without asserting specifics.
