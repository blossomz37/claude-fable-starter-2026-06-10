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
- ◐ W2-A Drafting & revision — file complete on disk (404 lines); agent died at
  usage limit BEFORE delivering accuracy report → QA must be extra careful
- ◐ W2-B Publishing ops — same (386 lines, no report)
- ◐ W2-C Marketing & launch — file complete (353 lines) + full accuracy report
  received (1 web check: KDP AI-disclosure policy verified; Apr-2026 enforcement
  claim is press-only, flagged in doc)
- ◐ W2-D Research & worldbuilding — file complete on disk (393 lines); no report
- ◐ W2-E Use-case catalog — file complete (317 lines, 97 use cases) + full report
  (EPUB tooling and Vellum automation flagged ⚠️ as workaround-only)
- ☐ Wave 2 orchestrator QA + commit + push (NOT started — usage limit hit
  2026-06-10 ~1pm, resets 1:30pm PT; QA W2-A/B/D with extra scrutiny since
  their self-reports were lost)
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
