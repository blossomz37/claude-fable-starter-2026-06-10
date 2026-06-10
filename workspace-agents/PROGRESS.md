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
- ☑ All NEW items (Carlo's session requests + ideas-01.md topics 1–4) delivered
  in Wave 3 below: adopting-and-sharing-tools.md, usage/cost page in learning
  path, one-folder layout, building-tools coverage, Multimedia category,
  API observability section.

## Wave 3 — Starter-kit assembly — COMPLETE 2026-06-10
- ☑ quick-start.md (264 lines; canonical one-folder layout unifying all four workflow
  trees — `manuscript/` canonical, drafting's `chapters/` noted as alias; no ⚠️ flags)
- ☑ adopting-and-sharing-tools.md (340 lines; three-phase adoption method + PROFILE/
  ADAPTING/CUSTOMIZATIONS conventions + scrub pass + prompt→skill→script→MCP→app
  decision ladder; platform claims verified vs official skills/MCP docs)
- ☑ Multimedia: catalog category 10 (9 rows) + publishing-ops narration subsection +
  marketing imagery subsection. ElevenLabs/Ideogram/OpenAI/Gemini APIs verified
  official; Midjourney ⚠️ workaround-only (no confirmable official API, docs 403'd).
- ☑ managing-usage-and-cost.md: "Advanced: API users" added (Console dashboards,
  OTel env vars + metrics, Admin Usage/Cost API per-key tracking). All three legacy
  ⚠️ claims resolved: history-resend CONFIRMED (+ prompt-caching nuance), /cost FIXED
  (alias of /usage, local estimate), effort-cost CONFIRMED (+ thinking can't be
  disabled on Fable 5). Zero unverified claims remain in the doc.
- ☑ glossary.md (642 lines, 108 entries, A–Z; orchestrator-read in full)
- ☑ wiki/README.md (orchestrator-written: 5-stage learning path with usage/cost at
  step 3, map of contents, how-it-was-built note)
- ☑ Final QA sweep: scripted link check 0 broken (code blocks excluded); all 6 new/
  edited outputs orchestrator-read in full; root README updated (new pages linked,
  "in progress" labels removed); tools page linked from catalog + both READMEs.
  Glossary sweep found 2 real inconsistencies, both fixed: catalog's stale "no EPUB
  tooling documented" ⚠️ row (publishing-ops documents pandoc/EPUBCheck — row
  de-flagged and pointed there) and which-tool-when's overstated "skills carry over"
  bullet (corrected: Code tab + CLI share, chat surfaces keep separate copies).
  Orchestrator fixes during QA: skills.md example link rendered as live broken link
  (backticked); publishing-ops narration section `chapters/` → `manuscript/`.
- ☑ Final commit + push

## Out-of-wave additions
- ☑ `.claude/skills/fable-guide/SKILL.md` (2026-06-10, post-Wave-3, from Carlo's
  `workspace-carlo/ideas/agent-helper.md`) — project skill shipping with the kit:
  warm/authoritative advisor with a routing map over all 20 wiki pages and three
  modes (explain a topic / build a Fable-optimized skill / architect a workspace).
  Linked from root README (tip box) and wiki README. Travels with the repo so
  every starter-kit user gets `/fable-guide`.
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
- 2026-06-10: Wave 3 session. 5 subagents (quick-start, tools, multimedia,
  API-observability, glossary) + orchestrator-written wiki/README.md + root README
  refresh. All outputs orchestrator-read; 4 inconsistencies/breaks found and fixed
  in QA; 0 broken links; all ideas-01.md topics and legacy ⚠️ flags resolved.
  **PROJECT COMPLETE** — wiki is 20 files / 5 sections, all claims verified or
  flagged as of 2026-06-10.
