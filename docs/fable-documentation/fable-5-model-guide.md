# Claude Fable 5: The Model, Explained for Authors

> **In plain words:** Claude Fable 5 is Anthropic's most capable AI model that ordinary
> users can actually get — launched June 9, 2026. It can work on long, multi-step projects
> (think: auditing a whole series bible, or revising a full manuscript pass by pass) with
> far less hand-holding than earlier models. It's included free on paid Claude plans
> through June 22, 2026, and it occasionally hands a request off to a slightly less
> powerful model for safety reasons — which is normal and clearly labeled when it happens.

## What it is

Claude Fable 5 (`claude-fable-5`) is what Anthropic calls a **Mythos-class model made
safe for general use**. Translation: Anthropic built a model so capable that they first
released it only to vetted cybersecurity partners (as "Claude Mythos"). Fable 5 is that
same underlying model, wrapped in safety guardrails so everyone can use it.

A useful analogy: Mythos 5 is the unredacted manuscript; Fable 5 is the published
edition — same book, same voice, but a few specialist appendices (offensive hacking,
dangerous biology) are handled differently for the general reader.

**How it differs from the other Claude models you may know:**

| Model | What it's for | API price (per million tokens, in/out) |
|---|---|---|
| **Fable 5** | The most demanding work; long autonomous projects | $10 / $50 |
| **Opus 4.8** | Anthropic's previous top model; still excellent for complex work | $5 / $25 |
| **Sonnet 4.6** | Best balance of speed and intelligence for everyday drafting | $3 / $15 |
| **Haiku 4.5** | Fastest and cheapest; quick lookups, simple tasks | $1 / $5 |

The headline difference is not "writes prettier sentences" — it's **stamina and
judgment**. Anthropic's phrase is that Fable 5 "works independently for longer than any
prior generally available Claude model, planning across stages and verifying its own
work along the way." For an author, that means: the longer and messier the job (a
30-chapter continuity audit, a full-series timeline reconciliation), the bigger Fable 5's
advantage over Opus, Sonnet, or Haiku. For a single blurb or a quick line edit, you
genuinely may not notice a difference — and the cheaper models remain the sensible
choice there.

**What is Claude Mythos 5?** The same model with some safeguards lifted, restricted to
vetted cybersecurity organizations (via Anthropic's Project Glasswing, with the US
government) and soon select biology researchers. You will not use Mythos 5, and you
don't need it — for the >95% of sessions that never touch a safety classifier, Fable 5's
performance is effectively identical.

## Why authors care

- **Long jobs actually finish.** Fable 5 stays focused across millions of tokens and uses
  its own working notes (file-based memory) to keep improving as it goes. In Anthropic's
  testing, persistent notes helped Fable 5 roughly three times more than they helped
  Opus 4.8. Practical upshot: a "read all 28 chapters, then fix every timeline error"
  task is now realistic in one run.
- **It checks its own work.** Early customers report that at higher effort settings it
  reflects on and validates its output before declaring victory — fewer "done!" responses
  that weren't actually done.
- **Strong document reasoning.** Benchmarks emphasized senior-level document analysis,
  chart/table interpretation, and root-cause reasoning. For you: better answers to "why
  does Act 2 sag?" backed by actual evidence from the manuscript, not vibes.
- **Best-in-class vision.** It reads detailed images precisely (it rebuilt an app from
  screenshots; it extracted exact numbers from scientific figures). For you: cover
  comps, Plottr/Aeon screenshots, handwritten notes, KDP dashboard screenshots.
- **Huge context window.** 1 million tokens — roughly 500,000+ words. A full trilogy
  plus the series bible fits in a single conversation.
- **Free trial window on your existing plan** (through June 22, 2026 — details below).

## Getting started

You need a paid Claude plan (Pro, Max, Team, or seat-based Enterprise). Through
**June 22, 2026**, Fable 5 is included at no extra cost.

**In Claude Desktop (or claude.ai):**

1. Open a new chat.
2. Click the model picker (the model name near the message box).
3. Select **Claude Fable 5**.
4. Ask it something with real scope, e.g. *"Here's my series bible and the first three
   chapters of book 4. Audit the chapters against the bible and list every
   contradiction with chapter and line references."*

**In Claude Code (the terminal app):**

1. Open Terminal (macOS: Cmd+Space, type "Terminal"; Windows: use PowerShell or WSL).
2. Navigate to your manuscript folder: `cd ~/Documents/my-novel`
3. Start Claude Code on Fable 5:
   ```bash
   claude --model claude-fable-5
   ```
4. Or, inside an already-running session, type `/model` and pick Fable 5 from the menu.
5. To make it your default, add this to `~/.zshrc` (macOS) or `~/.bashrc` (Linux):
   ```bash
   export ANTHROPIC_MODEL="claude-fable-5"
   ```

On paid plans, Claude Code gives Fable 5 its full 1M-token context window.

## Author use cases

1. **Whole-manuscript continuity audit.** Point Claude Code at your manuscript folder and
   ask Fable 5 to read every chapter, build a timeline, and flag contradictions (eye
   color, travel times, who-knew-what-when). This is exactly the "long-horizon" work
   where Fable 5 outperforms cheaper models. Can be packaged as a skill or subagent.
2. **Series bible reconciliation.** Feed it books 1–3 plus your bible and ask it to
   update the bible to match what's actually on the page — and list every place the
   books disagree with each other.
3. **Deep revision passes with working notes.** Ask it to keep a `revision-notes.md`
   file as it works through chapters. Fable 5 is specifically better at using its own
   notes to improve later output — the file-based memory behavior Anthropic benchmarked.
4. **Structural diagnosis.** "Read the full draft. Where does tension flatten, and what's
   the structural cause?" Its gains in document-based reasoning make these answers more
   evidence-grounded than earlier models.
5. **Visual research and comps.** Drop in screenshots of comp covers, your Aeon Timeline,
   or a photographed notebook page and ask for analysis. Fable 5 is the current
   state-of-the-art on vision tasks.
6. **The big one-shot.** Tasks you'd previously break into ten prompts (outline → draft
   → critique → revise) can often be given as one long brief. Early testers report it
   "one-shots" work that used to take many rounds.
7. **As an advisor to cheaper models** (power users): run your routine pipeline on
   Sonnet/Haiku and have Fable 5 review the plan mid-task. See Advanced.

## Common pitfalls

- **The free window is temporary.** Included on Pro/Max/Team/seat-based-Enterprise only
  **through June 22, 2026**. On **June 23, 2026**, Anthropic removes it from those plans;
  using it after that requires [usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)
  (pay-as-you-go at API rates). Anthropic says it intends to extend the window if
  capacity allows, and to restore Fable 5 to subscriptions "as quickly as we can."
  Status verified 2026-06-10; check Anthropic's announcement page for changes.
- **It burns usage faster.** API pricing is double Opus 4.8 ($10/$50 vs $5/$25 per
  million tokens), and it tends to think longer. ⚠️ Unverified: third-party reporting
  says Fable 5 counts as 2x usage against subscription limits; I could not confirm a
  multiplier on an official support page. Either way: don't use Fable 5 for tasks Sonnet
  handles fine.
- **Expect the occasional model switch — it's fine.** Fable 5 runs safety classifiers on
  every request. If a request looks like offensive cybersecurity, sensitive
  biology/chemistry, or an attempt to extract the model's reasoning, the response is
  handled by **Claude Opus 4.8** instead, and you're told when it happens. The
  safeguards are deliberately tuned broad, so a thriller writer researching how a hacker
  breaches a hospital network, or a sci-fi author asking about engineered plagues, may
  trip them with completely legitimate questions. You still get a high-quality answer
  (Opus 4.8 was the top model until last week); over 95% of sessions never hit a
  fallback at all. In the Claude apps you can toggle this under Settings → Capabilities
  ("Switch models when a message is flagged") — if off, blocked requests pause instead.
- **30-day data retention is mandatory.** All Fable 5 traffic (prompts and outputs) is
  retained for 30 days for safety monitoring — including for API customers who normally
  have zero-data-retention agreements. It is **not used to train Claude**, access is
  logged, and it's deleted after 30 days. If you write under strict NDA or ghostwrite,
  factor this in.
- **Tokenizer note:** Fable 5 uses the newer tokenizer (introduced with Opus 4.7) that
  produces roughly 30% more tokens for the same text — relevant if you're estimating
  API costs from word counts.
- **No "disable thinking" option.** Fable 5 always uses adaptive thinking; you control
  depth with effort (below), not by switching thinking off.

## Advanced

### Model IDs and variants

- Claude API / Vertex AI: `claude-fable-5` (a pinned snapshot — dateless IDs from the
  4.6 generation onward are snapshots, not evergreen pointers)
- AWS Bedrock: `anthropic.claude-fable-5`
- Mythos: `claude-mythos-5` (Glasswing partners only); `claude-mythos-preview` (legacy)
- Claude Code 1M-context variant: `claude-fable-5[1m]` — the `[1m]` suffix is Claude
  Code's convention for selecting the 1M-token context window. ⚠️ Partially verified:
  official docs state Fable 5 has a 1M context window by default on the API and that
  Claude Code on paid plans supports 1M for Fable 5; the literal `[1m]` suffix appears
  in Claude Code itself but I did not find it documented on an official page.

### Specs

- Context window: 1M tokens (default). Max output: 128k tokens per request.
- Adaptive thinking always on; `thinking: {"type": "disabled"}` is rejected.
- Raw chain-of-thought is never returned. `thinking.display` is `"omitted"` (default,
  empty thinking blocks) or `"summarized"` (readable summary).
- Supported at launch: effort, task budgets (beta header `task-budgets-2026-03-13`),
  memory tool, code execution, programmatic tool calling, context editing / tool-result
  clearing (beta header `context-management-2025-06-27`), compaction, vision.
- Knowledge: trained on data through January 2026 (per Anthropic support).

### Effort levels

Fable 5 supports `low` / `medium` / `high` (default) / `xhigh` / `max` via
`output_config.effort`. Anthropic's guidance for Fable 5 specifically: start at `high`,
use `xhigh` for the most capability-sensitive work, and step down to `medium`/`low` for
routine tasks — lower effort on Fable 5 "still performs well and often exceeds `xhigh`
performance on prior models." At `high`/`xhigh`, set a large `max_tokens` (it caps
thinking + response combined). In Claude Code, "ultracode" in the effort menu is
`xhigh` plus standing permission for multi-agent workflows — not a separate API level.

### Refusals, fallback, and billing (API)

On the API, blocked requests are **not** automatically rerouted (unlike the consumer
apps). The Messages API returns HTTP 200 with `stop_reason: "refusal"` plus which
classifier fired; you are not billed for requests refused before output. Three retry
paths:

- **Server-side fallback** (beta): pass the `fallbacks` parameter and the API retries on
  Opus 4.8 for you (Claude API and Claude Platform on AWS).
- **Client-side**: SDK middleware (TypeScript, Python, Go, Java, C#) retries on any platform.
- **Manual**: roll your own; **fallback credit** refunds the prompt-cache cost of the
  model switch so you don't pay it twice.

In Claude Managed Agents, fallback is built in.

### Advisor strategy and Managed Agents

- **Advisor tool** (public beta, header `advisor-tool-2026-03-01`): a fast, cheap worker
  model (e.g., Sonnet 4.6) calls Fable 5 mid-task to check its plan and evaluate its
  work — near-Fable quality at mostly worker-model token rates. For an author pipeline:
  Haiku/Sonnet drafts chapter summaries; Fable 5 advises on the revision plan.
- **Claude Managed Agents** (public beta): Anthropic's hosted harness for long-running
  agentic work (webhooks, multi-agent orchestration, sandboxes). Fable 5 works with it
  out of the box.

### Admin and data terms (API)

- Fable 5 and Mythos 5 are designated **Covered Models**: 30-day retention is required
  on all surfaces (first- and third-party); zero-data-retention agreements do not apply
  to them. Data is used only to detect/prevent serious misuse, never for training;
  human access is logged; deletion after 30 days in almost all cases.
- Per Anthropic's launch email: **Console admins must accept updated terms in the Claude
  Console before the organization can use the model.** ⚠️ Partially verified: stated in
  Anthropic's official launch email (archived in this repo) but I did not find it
  restated on a public docs/support page.

### Migration

To move existing API workloads from Opus 4.8 (or earlier) to Fable 5, Claude Code's
`claude-api` skill automates model names, prompts, and settings:

```
/claude-api migrate
```

Anthropic's migration guide:
`platform.claude.com/docs/en/about-claude/models/migration-guide`.

### Related repo docs

- [Anthropic launch announcement (archived copy)](./Claude_Fable_5_and_Claude_Mythos_5_Anthropic.md)
- [Anthropic launch email (archived copy)](./fable-about.md)

## Sources

All accessed 2026-06-10:

- https://www.anthropic.com/news/claude-fable-5-mythos-5 — launch post: pricing,
  rollout timeline, classifiers, retention, Mythos 5, availability
- https://platform.claude.com/docs/en/about-claude/models/overview — model IDs, specs,
  pricing for Fable 5 / Opus 4.8 / Sonnet 4.6 / Haiku 4.5, tokenizer note
- https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  — API behavior: refusals, fallback, billing, adaptive thinking, supported features,
  Covered Models designation
- https://platform.claude.com/docs/en/build-with-claude/effort — effort levels and
  Fable 5 recommendations; ultracode note
- https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5
  — automatic model switching in Claude apps/Code, settings toggle
- https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models
  — 30-day retention details and privacy protections
- https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
  — 1M context for Fable 5 in Claude Code on paid plans
- https://support.claude.com/en/articles/11940350-claude-code-model-configuration —
  selecting Fable 5 in Claude Code (`/model`, `--model`, `ANTHROPIC_MODEL`)
- Anthropic launch email, June 9, 2026 (archived in this repo as `fable-about.md`) —
  advisor strategy, Managed Agents, Console admin terms acceptance, `/claude-api migrate`
- ⚠️ Unverified: subscription "2x usage" multiplier for Fable 5 (third-party reporting
  only, e.g. BleepingComputer); the literal `[1m]` suffix on an official page; Console
  admin terms acceptance on a public support page (email-only so far).
