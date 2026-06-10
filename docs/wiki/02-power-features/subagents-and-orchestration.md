# Subagents: Let Claude Delegate Work to Copies of Itself

> **In plain words:** A subagent is a fresh copy of Claude that your main Claude
> session hands a task to — like a managing editor assigning chapters to different
> copyeditors. Each copy works in its own clean workspace, then reports back a
> summary. You can run several at once ("review these five chapters in parallel"),
> and you never have to write a single line of configuration to use them.

## What it is

When you chat with Claude Code, everything — your requests, the files it reads,
its replies — accumulates in one conversation. That conversation has a limited
"context window" (working memory). Long sessions fill it up with clutter: search
results, file contents, half-finished tangents.

A **subagent** solves this. Claude spins up a separate copy of itself with a
blank slate, gives it one job ("check chapter 7 for timeline errors"), and lets
it work independently. The subagent reads whatever files it needs, does the
work in its own private context, and returns only the result — a tidy report —
to your main conversation. All the messy intermediate reading stays out of your
session.

The author-world analogy holds up well:

- **You** are the publisher.
- **Your main Claude session** is the managing editor.
- **Subagents** are freelance copyeditors, proofreaders, and beta readers the
  editor hires per task. Each gets a clean brief, works alone, and turns in a
  memo. They don't sit in on your editorial meetings, and they don't see each
  other's work unless someone shows it to them.

Three things make this matter:

1. **Clean context per task.** Each subagent starts fresh, so chapter 12's
   review isn't biased or crowded by chapter 3's.
2. **Parallelism.** Independent subagents can run at the same time. Five
   chapter reviews take roughly as long as one.
3. **Your main session stays uncluttered.** Only summaries come back, so a long
   working session doesn't drown in raw file contents.

## Why authors care

- **Manuscript-scale work fits.** A 100k-word novel won't fit comfortably in one
  conversation, but ten subagents each reading a few chapters handles it.
- **Multiple reader perspectives at once.** One agent reads as a romance reader,
  one as a thriller reader, one tracks the timeline — simultaneously, with no
  cross-contamination between their opinions.
- **Tedious checks become one sentence.** "Use subagents to check every chapter
  against the series bible" replaces an afternoon of copy-paste.
- **No setup required.** You can use subagents purely by asking. Custom
  configured agents are optional polish, not a prerequisite.

## Getting started

You do not need to configure anything. Subagents are built in, and Claude often
uses them on its own. To use them deliberately:

1. Open Claude Code in your manuscript folder (`claude` in Terminal).
2. Ask for parallel delegated work in plain English:

   ```text
   Use subagents to review chapters 1 through 5 in parallel, one agent each.
   Each agent should check its chapter for continuity errors against
   series-bible.md and report back a short list of problems.
   ```

3. Watch the task list: Claude spawns the agents, each works independently, and
   the findings come back as summaries in your conversation.
4. Run `/agents` at any time to see what's running (the **Running** tab) and
   what agent types exist (the **Library** tab).

That's the whole entry point. Everything below is refinement.

## Built-in agent types

Claude Code ships with subagent types it picks between automatically
(verified against the official docs, June 2026):

| Agent | What it's for | Model it uses |
| :-- | :-- | :-- |
| **Explore** | Fast, read-only searching and skimming — "find every scene where Mara appears." Cannot edit files. | Haiku (fast, cheap) |
| **Plan** | Read-only research during plan mode, gathering context before Claude proposes a plan. | Same as your session |
| **general-purpose** | Complex multi-step tasks that need both reading and writing — the default workhorse. | Same as your session |
| statusline-setup | Helper that runs when you use `/statusline`. | Sonnet |
| claude-code-guide | Helper that answers questions about Claude Code itself. | Haiku |

You rarely invoke these by name; Claude routes tasks to them based on what the
task needs. One quirk worth knowing: **Explore and Plan skip your CLAUDE.md
files** to stay fast and cheap. If a project rule must apply during research
("British spellings throughout"), restate it in your request.

## Custom subagents — still no code required

If you keep asking for the same kind of worker — say, a continuity checker with
the same instructions every time — you can save it as a named subagent. The
easiest way is the `/agents` command:

1. Run `/agents`, go to the **Library** tab, choose **Create new agent**.
2. Pick **Personal** (available in all your projects) or project scope.
3. Choose **Generate with Claude** and describe the agent in plain English:
   "A continuity checker that compares a chapter against series-bible.md and
   reports contradictions in character details, timeline, and setting."
4. Pick its tools (read-only is a good default for reviewers), a model, and a
   color, then save.

From then on, Claude delegates to it automatically whenever a task matches its
description, or you can summon it directly: type `@` and pick the agent, or say
"use the continuity-checker subagent on chapter 9."

Under the hood, each custom agent is just a small Markdown file in
`.claude/agents/` (this project) or `~/.claude/agents/` (all your projects) —
details in [Advanced](#advanced).

## Author use cases

1. **Per-chapter continuity sweep.** "Spawn one subagent per chapter in
   `manuscript/`. Each checks its chapter against `series-bible.md` for
   character eye color, ages, timeline, and geography. Compile all findings
   into `reports/continuity.md`." Worth saving as a custom agent if you do it
   every draft.
2. **Multi-lens critique.** "Read chapter 14 with three subagents in parallel:
   one as a devoted romance reader judging the emotional beats, one as a
   thriller reader judging pacing and stakes, one purely tracking the timeline.
   Give me each report separately." Because each agent has a clean context, the
   thriller reader's complaints can't bleed into the romance reader's verdict.
3. **Research fan-out across comp titles.** "Use one subagent per comp title —
   *Fourth Wing*, *Iron Flame*, *A Court of Thorns and Roses* — to research its
   blurb structure, tropes, and review themes on the web, then synthesize a
   positioning memo." This is the classic fan-out/fan-in pattern, and the kind
   of breadth-first research Anthropic's own engineering team found multi-agent
   setups excel at. See also
   [Research & worldbuilding](../03-author-workflows/research-and-worldbuilding.md).
4. **Isolate noisy bulk work.** "Use a subagent to run the prose-audit script
   across all 40 chapters and report only the flagged passages." The thousands
   of lines of raw output stay in the subagent's context; you see one summary.
5. **Blurb tournament.** "Three subagents each draft a blurb from a different
   angle — character-first, stakes-first, voice-first — then a fourth agent
   compares them against the top 10 blurbs in my subgenre and picks a winner."
6. **Overnight or walk-away work.** Dispatch long jobs as background sessions
   with `claude agents` and check back later — see
   [Background and long-running work](#background-and-long-running-work).

Recurring versions of 1–3 can be packaged as custom agents (above) or paired
with [skills](skills.md) and [hooks](hooks.md) for fully repeatable pipelines.

## Background and long-running work

Subagents themselves can run in the **foreground** (you wait) or **background**
(you keep working while they run). Claude decides, but you can say "run this in
the background" or press **Ctrl+B** to background a running task. `/tasks`
lists everything running in the background of the current session. One caveat:
background subagents can't ask you permission questions — anything that would
prompt is auto-denied, so grant permissions up front for background work.

For bigger jobs, Claude Code has layers above subagents (all verified current,
June 2026):

- **Background sessions / agent view** (`claude agents`, research preview):
  dispatch whole independent sessions — "format the paperback interior,"
  "draft the newsletter" — and monitor them all on one screen. They keep
  running even after you close the terminal.
- **Background shell commands**: a single long-running command (a compile, a
  batch export) can run without blocking the conversation.
- **Routines**: scheduled sessions that run in Anthropic's cloud on a timer —
  a nightly word-count report, for instance.
- **Agent teams** (experimental, off by default): multiple coordinated sessions
  with a shared task list that message each other, managed by a lead agent.
- **Cloud scale**: this layered local orchestration mirrors Anthropic's hosted
  **Managed Agents** platform, and Fable 5 (`claude-fable-5`, released June
  2026) was built for exactly this — Anthropic describes it running in a
  harness like Claude Code or Managed Agents "for days at a time: planning
  across stages, delegating to sub-agents, and checking its own work."

## Common pitfalls

- **Tokens multiply — fast.** Anthropic's own engineering data: an agent uses
  roughly **4× the tokens of a chat**, and multi-agent systems about **15×**.
  A five-agent fan-out is real usage against your plan limits. Worth it for
  breadth-first jobs (reviewing many chapters, researching many comps); wasteful
  for a quick question about one scene. When in doubt, just ask in the main
  conversation.
- **Subagents don't share memory.** Agent A's discoveries are invisible to
  agent B. If agents must build on each other's work, have them write findings
  to files (a `reports/` folder works well) and tell the next agent to read
  them.
- **Results still come back to your context.** Ten subagents each returning a
  detailed report can fill your main conversation anyway. Ask for short
  summaries, or have agents write full reports to files and return one line.
- **Subagents can't spawn subagents.** No infinite nesting. Chains must be
  coordinated from the main conversation.
- **Don't fan out interdependent work.** If chapter 12's revision depends on
  what changes in chapter 11, parallel agents will step on each other. Parallel
  is for independent tasks; sequential chains are for dependent ones.
- **Edited an agent file by hand?** Agent files added or changed directly on
  disk load at session start — restart the session. Agents created via
  `/agents` take effect immediately.
- **Latency.** A subagent starts cold and re-gathers context. For quick
  back-and-forth iteration, the main conversation is faster.

## Advanced

### Agent file anatomy

Custom subagents are Markdown files with YAML frontmatter. Locations, in
priority order when names collide: managed (organization) settings → `--agents`
CLI flag (session-only JSON) → `.claude/agents/` (project; check into git) →
`~/.claude/agents/` (personal) → plugin `agents/` directories. Both project and
user directories are scanned recursively, so `agents/review/romance-reader.md`
is fine; identity comes from the `name` field, not the filename.

```markdown
---
name: continuity-checker
description: Checks manuscript chapters against the series bible for contradictions. Use proactively after any chapter is drafted or revised.
tools: Read, Grep, Glob
model: haiku
---

You are a continuity editor for a multi-book fiction series.
Compare the chapter you are given against series-bible.md.
Report contradictions in character details, timeline, geography,
and established magic/tech rules. Cite chapter line and bible entry
for each finding. Return a concise numbered list; do not rewrite prose.
```

The body is the subagent's entire system prompt — it does *not* get the normal
Claude Code system prompt. It *does* get your CLAUDE.md hierarchy and a git
status snapshot (built-in Explore and Plan are the only types that skip those).

**Frontmatter fields** (verified against official docs, 2026-06-10; only
`name` and `description` are required):

| Field | Purpose |
| :-- | :-- |
| `name` | Unique id, lowercase-and-hyphens |
| `description` | When Claude should delegate to it. Add "use proactively" to encourage auto-delegation |
| `tools` | Allowlist of tools (inherits all if omitted) |
| `disallowedTools` | Denylist, applied before `tools` |
| `model` | `sonnet`, `opus`, `haiku`, `fable`, a full model ID, or `inherit` (default) |
| `permissionMode` | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan` |
| `maxTurns` | Cap on agentic turns |
| `skills` | [Skills](skills.md) preloaded in full at startup |
| `mcpServers` | [MCP servers](mcp.md) scoped to this agent (inline or by name) |
| `hooks` | [Hooks](hooks.md) active only while this agent runs |
| `memory` | Persistent memory dir: `user`, `project`, or `local` — the agent accumulates learnings across sessions |
| `background` | `true` = always run as a background task |
| `effort` | `low` … `max` reasoning effort override (model-dependent) |
| `isolation` | `worktree` = work in a temporary git worktree, not your live checkout |
| `color` | UI color: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan` |
| `initialPrompt` | Auto-submitted first turn when run as the main session via `--agent` |

**Tool restriction** is the practical safety lever: give reviewers
`tools: Read, Grep, Glob` and they physically cannot rewrite your manuscript.
**Model selection per agent** is the cost lever: route bulk search to `haiku`,
keep prose judgment on `fable` or your session model. To block an agent type
entirely, add `"Agent(Explore)"`-style rules to `permissions.deny` in
[settings](../01-claude-code-basics/settings-and-permissions.md). (The Agent
tool was named Task before v2.1.63; old `Task(...)` rules still work.)

### Invocation escalation

Natural language ("use the continuity-checker on chapter 9") → `@`-mention
(`@agent-continuity-checker`, guarantees that agent runs) → `claude --agent
continuity-checker` (the whole session *becomes* that agent — its prompt, tools,
and model replace the defaults), or set `"agent": "continuity-checker"` in
`.claude/settings.json` to make that the project default.

### Orchestrator patterns

- **Fan-out / fan-in:** spawn N parallel agents on independent slices, then
  synthesize. Best for breadth-first work; this is the orchestrator–worker
  design from Anthropic's multi-agent research system, where an Opus lead with
  Sonnet workers outperformed a single agent by 90.2% on research evals.
- **Pipeline:** chain agents sequentially — "use the line-edit agent on chapter
  3, then the continuity-checker on the result." Each returns to the main
  conversation, which briefs the next.
- **Adversarial verification:** one agent produces (a blurb, a plot fix), a
  second agent with a skeptic prompt attacks it ("find every way this blurb
  misrepresents the book"). For bigger versions — dozens of agents
  cross-checking each other — Claude Code's **dynamic workflows** (`/workflows`)
  run scripted multi-agent passes with built-in cross-verification.
- **Shared state via files:** since agents share no memory, the filesystem is
  the bulletin board. A common shape: every fan-out agent writes
  `reports/ch-NN.md`; the fan-in agent globs and reads `reports/*.md`. The
  `memory` frontmatter field adds per-agent persistent knowledge across
  sessions (`~/.claude/agent-memory/<name>/` for user scope).
- **Forks:** `/fork draft three alternate endings from where we are` spawns a
  subagent that *inherits* your full conversation instead of starting fresh —
  for side quests that need everything you've discussed so far.
- **Resuming:** general-purpose and custom subagents return an agent ID and can
  be resumed with full prior context ("continue that review and now check the
  epilogue"). Explore and Plan are one-shot.

### The Claude Agent SDK, in one paragraph

Everything above also exists as a library. The **Claude Agent SDK** (Python and
TypeScript) exposes Claude Code's agent loop, tools, and subagent system
programmatically — you can define agents in code, restrict their tools, wire
hooks, and ship the result as your own application (a manuscript-audit web tool,
a publisher pipeline). Note that from June 15, 2026, SDK and `claude -p` usage
on subscription plans draws from a separate monthly Agent SDK credit. Start at
the official overview: <https://code.claude.com/docs/en/agent-sdk/overview>.
For hosted production agents without running your own infrastructure, the same
concepts graduate to Anthropic's Managed Agents platform
(<https://platform.claude.com/docs/en/managed-agents/overview>).

## Sources

- https://code.claude.com/docs/en/sub-agents — built-in types, file locations, full frontmatter table, `/agents`, invocation, forks, memory, examples (accessed 2026-06-10)
- https://code.claude.com/docs/en/agents — "Run agents in parallel": subagents vs agent view vs agent teams vs dynamic workflows vs worktrees, `/tasks`, `/workflows`, routines (accessed 2026-06-10)
- https://code.claude.com/docs/en/agent-view — background sessions, `claude agents`, research-preview status, supervisor process (accessed 2026-06-10)
- https://code.claude.com/docs/en/agent-sdk/overview — Agent SDK languages, capabilities, SDK credit change, Managed Agents comparison (accessed 2026-06-10)
- https://www.anthropic.com/engineering/multi-agent-research-system — orchestrator-worker pattern, ~4×/~15× token multipliers, 90.2% eval result, when multi-agent helps vs hurts (accessed 2026-06-10)
- Fable 5 + Managed Agents framing ("can work for days… delegating to sub-agents") — Anthropic's Fable 5 announcement materials via https://www.anthropic.com/claude/fable and June 2026 coverage (accessed 2026-06-10)
- ⚠️ Unverified: none of the feature claims above are unverified; exact subscription rate-limit impact of parallel fan-outs varies by plan and was not quantified beyond the official "multiplies token usage" warning and the engineering-blog multipliers.
