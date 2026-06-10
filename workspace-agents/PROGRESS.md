# Progress Tracker

Legend: ☐ not started · ◐ in progress · ☑ done (orchestrator-reviewed) 

## Wave 1 — Platform & feature research
- ☑ W1-A Fable 5 model guide
- ☑ W1-B Claude Code basics (4 files)
- ☑ W1-C Skills
- ☑ W1-D Hooks
- ☑ W1-E Subagents & orchestration
- ☑ W1-F MCP
- ☑ W1-G Desktop + which-tool-when
- ☑ Wave 1 orchestrator QA + commit (all 10 docs read in full; passed)

## Wave 2 — Author workflow deep dives
- ☑ W2-A Drafting & revision (404 lines; lost report compensated by orchestrator
  spot-checks — all platform claims verified against Wave 1 docs)
- ☑ W2-B Publishing ops (386 lines; external KDP/Vellum claims already ⚠️-flagged
  in-doc; pandoc/EPUBCheck claims sound)
- ☑ W2-C Marketing & launch (353 lines + full accuracy report)
- ☑ W2-D Research & worldbuilding (393 lines; `arguments:` frontmatter and
  classifier-fallback claims verified against Wave 1 docs)
- ☑ W2-E Use-case catalog (317 lines; catalog format deviates from DOC_TEMPLATE
  required structure — acceptable for a 04-reference master-table doc per plan spec)
- ☑ Wave 2 orchestrator QA + commit + push (2026-06-10, second resume session):
  all 5 docs read in full once; scripted cross-link check — zero broken links;
  spot-checked W2-A/B/D platform claims against QA'd Wave 1 docs (memory field,
  prompt-type Stop hooks, FileChanged, arguments frontmatter,
  disable-model-invocation, 1M context, 4×/15× multipliers, pricing/free window,
  Opus 4.8 classifier fallback) — all confirmed. No fixes needed; PASS.
- ☐ NEW (from Carlo, this session): add
  docs/wiki/03-author-workflows/adopting-and-sharing-tools.md in Wave 3 —
  intake → cleanup → re-architect method for adopting shared author tools
  (three-layer model: engine/conventions/personal; PROFILE.md extraction;
  ADAPTING.md self-onboarding prompt; delta log; scrub-before-reshare).
  Content drafted in conversation 2026-06-10 — see session handoff in
  workspace-agents/handoffs/ if context lost.
- ☐ NEW: add a usage/cost-management page or section (Carlo hit session limits
  mid-wave; wiki should teach mitigation: cheaper models for subagents,
  /usage, /clear, /compact, batch sizing, model-per-agent).
- ☐ NEW (from Carlo's ideas-01.md, logged 2026-06-10): four topics for Wave 3 —
  1. **One-folder end-to-end project**: quick-start.md should establish ONE
     canonical book-project folder layout and show how each workflow doc's
     structure (drafting's bible/, publishing's output/, marketing/, research/,
     world/) slots into it as subfolders. Today each deep dive shows its own
     separate layout; nothing unifies them.
  2. **Authors building custom tools/apps** (vibecoding: Electron apps, web
     components, author utilities): essentially uncovered (only a one-line
     `mcpb` mention in mcp.md). Fold into the planned
     adopting-and-sharing-tools.md → retitle scope to "building, adopting, and
     sharing author tools."
  3. **Audio & image generation via third-party APIs** (ElevenLabs narration,
     Midjourney/Ideogram covers): zero current coverage. Add a new use-case-
     catalog category (Multimedia) + a short section in publishing-ops or
     marketing Advanced. Honesty flags required: Midjourney has no official
     API (⚠️ workaround-only, like the Vellum rows); ElevenLabs does.
  4. **API observability/cost management**: managing-usage-and-cost.md covers
     plan usage + `/cost` only. Add an "Advanced: API users" section (Console
     usage dashboards, Claude Code OpenTelemetry support, per-key tracking) —
     verify against official docs during the Wave 3 ⚠️-claims sweep already
     scheduled for that page.

## Wave 3 — Starter-kit assembly
- ☐ quick-start.md
- ☐ glossary.md
- ☐ wiki/README.md (home + learning path)
- ☐ Final QA sweep (links, terminology; verify ⚠️ claims in managing-usage-and-cost.md)
- ☐ Final commit

## Out-of-wave additions
- ☑ 00-start-here/managing-usage-and-cost.md (token discipline for authors) — written
  by orchestrator 2026-06-10; ⚠️ flags pending live verification in Wave 3 QA.
- ☑ Token discipline hardened into CLAUDE.md, IMPLEMENTATION_PLAN.md, DOC_TEMPLATE.md
  (subagent report cap + silent-work rules).

## Session log
- 2026-06-10: Plan created, Wave 1 launched.
- 2026-06-10: Wave 1 complete (10 docs, all QA'd and passed). Key findings agents
  surfaced: slash commands merged into skills; ~31 hook events now; Desktop is
  Chat/Cowork/Code three-tab app; Tool Search defers MCP tools by default;
  Fable 5 inclusion window June 9–22 confirmed unchanged as of today.
- 2026-06-10: User added: README.md must become the user-facing guide; remote is
  https://github.com/blossomz37/claude-fable-starter-2026-06-10 — push at checkpoints.
- 2026-06-10: Token-burn mitigation session. Added managing-usage-and-cost.md wiki
  page; hardened token discipline into CLAUDE.md, plan, and doc template. Key rule:
  subagent reports ≤1 page, no raw dumps; sessions end at wave boundaries with handoffs.
- 2026-06-10: Wave 2 QA session. All 5 docs PASS (full reads, scripted link check,
  spot-checks vs Wave 1 docs replacing the lost W2-A/B/D reports). Wave 2 complete.
  Next: Wave 3 (includes the two NEW items above).
