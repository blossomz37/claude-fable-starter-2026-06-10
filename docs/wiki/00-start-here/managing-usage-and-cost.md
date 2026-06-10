# Managing Usage and Cost (Making Fable 5 Last)

> **In plain words:** Fable 5 is the most capable Claude model — and the most expensive
> ($10/$50 per million tokens in/out). Long working sessions burn through usage limits
> surprisingly fast, and most of that burn is invisible: it's the conversation history
> being re-sent on every turn, not the words you see on screen. This page explains where
> the tokens actually go and gives you habits that cut usage substantially without
> dumbing down the model.

## What it is

Every message you send to Claude costs **tokens** (chunks of text, roughly ¾ of a word
each). Two kinds matter:

- **Input tokens** — everything Claude has to *read* before answering: your message,
  plus the entire conversation so far, plus every file it has opened in the session.
- **Output tokens** — everything Claude *writes* back.

The non-obvious part: **the whole conversation is re-sent as input on every single
turn.** Turn 40 of a session re-reads turns 1–39. A long session is like a beta reader
who re-reads the entire manuscript-so-far before reacting to each new paragraph — the
re-reading is where the time (tokens) goes, not the reactions.

This is why usage "burns out super fast" in long agentic sessions even when the visible
answers are short: cost per turn keeps climbing as history accumulates. (Anthropic's
docs confirm the mechanics: each turn's input "contains all previous conversation
history plus the current user message," growing linearly. One softener: Claude Code
automatically uses *prompt caching*, which discounts re-sent repeated content — so
history isn't re-billed at full price every turn, but a long session still costs more
per message than a short one.)

## Why authors care

- **Usage limits are real.** On Pro/Max plans, heavy Fable 5 sessions can exhaust your
  allowance mid-task — often right in the middle of a long revision pass.
- **The fix is workflow, not sacrifice.** The habits below mostly *improve* output
  quality too (shorter, cleaner context = fewer confused answers).
- **Cheaper models exist for cheap steps.** Sonnet-class models cost roughly a third of
  Fable 5 and are fine for routine drafting-to-template work
  (see [the model guide](../../fable-documentation/fable-5-model-guide.md)).

## Getting started

The five highest-impact habits, in order:

1. **End sessions early; hand off instead of pushing through.** When a session has done
   one big unit of work, ask Claude to write a one-page handoff file (what's done, what's
   next, key decisions), then start a *fresh* session that reads only that file. Two
   short sessions cost far less than one long one, because each turn in a long session
   re-pays for all the history before it.
2. **Use subagents as token firewalls.** Have a subagent do the heavy reading (research,
   a 20-chapter read-through) in its *own* context, and return only a short report. The
   bulk never enters your main conversation, so you never pay for it again.
   See [Subagents & orchestration](../02-power-features/subagents-and-orchestration.md).
3. **Match the model to the step.** Fable 5 for judgment-heavy, long-horizon work
   (continuity audits, orchestration, final QA). Sonnet or Haiku for mechanical steps
   (reformatting, file conversion, first-pass summaries).
4. **Point at files; don't paste them.** Attaching or referencing a file lets Claude read
   just the parts it needs. Pasting a full manuscript into the chat box locks it into
   the history forever — you re-pay for it every turn afterward.
5. **Cut the meta-chatter.** Tell Claude: *"No progress narration, no recaps, no
   restating the plan — confirm completion in one line."* This trims output tokens and
   keeps the chat readable. (Note: redirecting output into a doc instead of the chat
   window does **not** by itself save tokens — Claude pays the same to write either way.
   The saving comes from writing *less*, wherever it lands.)

## Author use cases

1. **Manuscript-wide continuity audit, on a budget.** Orchestrator (Fable 5) defines the
   audit; one subagent per act reads chapters and returns a findings table; orchestrator
   merges and verifies. You pay Fable prices only for the thin orchestration layer.
2. **Series bible refresh.** Instead of one marathon session, run one session per book
   that appends to a shared `CONTINUITY_NOTES.md`, then one short final session that
   reconciles the file. File-based memory is exactly where Fable 5 shines
   (see [CLAUDE.md & memory](../01-claude-code-basics/claude-md-and-memory.md)).
3. **Chapter drafting pipeline.** Plan and final QA on Fable 5; the repetition/style/
   line-edit passes on a cheaper model via subagents. Same pipeline, ~half the spend.
4. **Research sprint.** A research subagent fetches and digests ten craft articles and
   returns a one-page brief. Your main session never carries ten articles in history.

## Common pitfalls

- **"Write it to a file to save tokens."** A common myth. Output costs the same in chat
  or in a file. Files help for *other* reasons (persistence, handoffs, not re-pasting),
  which indirectly save input tokens later — but the act of writing is not cheaper.
- **Letting a session live all day.** The longest sessions are the most expensive *per
  message*, and quality degrades too. End and hand off.
- **Re-reading files Claude already has.** Watch for repeated full-file reads; say
  "you've already read that file — don't re-read it."
- **Over-trimming.** Don't instruct Fable 5 to skip its self-checking and verification —
  that judgment is the main thing you're paying Fable prices for. Trim *narration*, not
  *reasoning*.
- **Using Fable 5 for everything.** For a single blurb or quick line edit you may notice
  no quality difference from Sonnet at a third of the cost.

## Advanced

**Standing instructions.** Put token discipline in `CLAUDE.md` (or workspace agent rules)
so it applies to every session automatically rather than being re-typed:

```markdown
## Token discipline
- No progress narration or recaps; confirm completion in one line.
- Read files surgically (targeted sections); never re-read files already in context.
- Heavy reading/research goes to subagents that return ≤1-page reports.
- End sessions at logical boundaries with a handoff file in workspace-agents/handoffs/.
```

**Subagent return contracts.** The single biggest lever in orchestrated workflows is
capping what subagents send back. Require a fixed short report format (files written,
sources used, unverified claims, surprises) — never "tell me everything you found."

**Model routing per step.** In Claude Code, `/model` switches models mid-session; in
scripted pipelines, route by step: `claude-fable-5` for plan/QA steps, a Sonnet-class
model for mechanical passes.

**Effort settings.** Thinking tokens are billed as output tokens, and higher effort
levels spend more of them. Use `/effort` to lower the level for intermediate passes and
keep high effort for final QA. Note: extended thinking cannot be *disabled* on Fable 5 —
it always thinks; effort level is the dial you actually have.

**Context window ≠ free.** Fable 5's 1M-token window means a trilogy *fits*; it does not
mean carrying a trilogy in every turn is wise. Load big corpora into a subagent or
query them with targeted reads.

**Watch the meter.** In Claude Code, `/usage` shows session token usage and an estimated
dollar cost, plus — on Pro/Max/Team plans — usage bars against your plan limits and a
breakdown by skill, subagent, plugin, and MCP server (press `d`/`w` to toggle 24-hour vs
7-day views). `/cost` and `/stats` are aliases for the same screen. The dollar figure is
a local estimate; for authoritative billing, API users should check the Console Usage
page. Check after a representative session to find your own hot spots.

## Advanced: API users

If you pay per-token through the Claude API (instead of a Pro/Max subscription), you
get harder numbers and better tooling. Everything below is for Console/API accounts.

**Console dashboards.** The Claude Console has dedicated **Usage** and **Cost** pages
([platform.claude.com/usage](https://platform.claude.com/usage)) — this is the
authoritative bill, unlike the local estimate in `/usage`. When you first authenticate
Claude Code with a Console account, a workspace named "Claude Code" is created
automatically, giving you centralized cost tracking for all Claude Code usage in your
organization (you can't create API keys in it; it exists for tracking). You can also
set workspace spend limits to cap total spend.

**OpenTelemetry monitoring.** Claude Code can export usage metrics to any
OpenTelemetry (OTel) backend — useful if you run scripted pipelines (say, a nightly
chapter-audit job) and want a dashboard of what they cost. Minimal setup:

```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp      # or: prometheus, console, none
export OTEL_LOGS_EXPORTER=otlp        # or: console, none
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

Exported metrics include `claude_code.token.usage` (tokens), `claude_code.cost.usage`
(estimated USD per session), `claude_code.session.count`, and
`claude_code.lines_of_code.count`. Metrics carry attributes like `user.id`,
`session.id`, and the model — and per-request attribution by skill, subagent, plugin,
and MCP server — so you can see *which* pipeline step burns the tokens. You can attach
your own labels (e.g. per project or per pen name) via `OTEL_RESOURCE_ATTRIBUTES`.

**Per-API-key usage tracking.** If you give each project (or each pipeline) its own API
key, you can break down usage by key. Two routes:

- The Console Usage page supports filtering and grouping similar to the API below.
- The **Usage & Cost Admin API** (`/v1/organizations/usage_report/messages`) returns
  token counts filterable/groupable by API key (`api_key_ids[]`), workspace, model, and
  service tier; the companion `/v1/organizations/cost_report` endpoint returns USD costs
  (daily buckets, groupable by workspace). Both require an **Admin API key**
  (`sk-ant-admin...`) and an organization — the Admin API is not available on
  individual accounts.

For per-user Claude Code cost breakdowns specifically, Anthropic points at the Claude
Code Analytics API rather than fanning out one API key per user.

## Sources

- Repo-local: [`fable-5-model-guide.md`](../../fable-documentation/fable-5-model-guide.md)
  (pricing, context window, effort levels, model comparison) — verified 2026-06-10.
- Repo-local: [`Claude_Fable_5_and_Claude_Mythos_5_Anthropic.md`](../../fable-documentation/Claude_Fable_5_and_Claude_Mythos_5_Anthropic.md)
  (launch facts) — verified 2026-06-10.
- [Manage costs effectively](https://code.claude.com/docs/en/costs) — `/usage` command
  behavior, local-estimate caveat, prompt caching/auto-compaction, effort and thinking
  billed as output tokens, Fable 5 always-on extended thinking, Claude Code workspace,
  spend limits — accessed 2026-06-10.
- [Commands reference](https://code.claude.com/docs/en/commands) — `/cost` and `/stats`
  as aliases of `/usage`; `/effort` levels — accessed 2026-06-10.
- [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  — per-turn history resend ("Input phase: contains all previous conversation history
  plus the current user message"), linear growth, thinking blocks stripped from later
  turns — accessed 2026-06-10.
- [Monitoring (OpenTelemetry)](https://code.claude.com/docs/en/monitoring-usage) —
  telemetry env vars, exported metrics and attributes — accessed 2026-06-10.
- [Usage and Cost API](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api)
  — Console Usage/Cost pages, Admin API endpoints, per-API-key filtering, Admin key
  requirement — accessed 2026-06-10.
