# Fable Starter Kit — Implementation Plan

**Status tracking:** see [PROGRESS.md](PROGRESS.md). **Doc style rules:** see [DOC_TEMPLATE.md](DOC_TEMPLATE.md).
**Last updated:** 2026-06-10

## Mission

Build a robust local wiki (`docs/wiki/`) that serves as an end-to-end educational
starter kit for indie authors using Claude Fable 5 in **Claude Code CLI** and
**Claude Desktop**. Audience is layered: plain-language top layer for non-technical
authors (Carlo's FFA students), plus an "Advanced" section per doc for power users
(Carlo himself).

## Decisions of record (from Carlo, 2026-06-10)

1. **Audience:** Both, layered — every doc leads plain-language, ends with Advanced section.
2. **Balance:** Tooling-heavy. One solid Fable 5 model doc; bulk of wiki covers
   Claude Code CLI + Desktop features (skills, hooks, subagents, MCP, memory, settings).
3. **Use cases:** ALL four areas get deep dives — drafting & revision, publishing ops,
   marketing & launch, research & worldbuilding. "Leave no stone unturned."
4. **Research:** Live web research, verified against current official Anthropic docs.
5. **Agent-facing docs** (this plan, progress, templates) live in `workspace-agents/`.
6. Orchestrator (main session) supervises subagent quality and accuracy; commits per
   logical unit with `Add/Update/Fix [thing]` messages.

## Target wiki structure

```
docs/
  fable-documentation/                  # existing source material + model guide
    Claude_Fable_5_and_Claude_Mythos_5_Anthropic.md   (source, exists)
    fable-about.md                                     (source, exists)
    fable-5-model-guide.md              # W1-A
  wiki/
    README.md                           # wiki home / index / learning path  (W3)
    00-start-here/
      quick-start.md                    # W3
      glossary.md                       # W3
      which-tool-when.md                # W1-G (CLI vs Desktop vs claude.ai)
      managing-usage-and-cost.md        # added 2026-06-10 (token discipline for authors)
    01-claude-code-basics/
      installation-setup.md             # W1-B
      claude-md-and-memory.md           # W1-B
      settings-and-permissions.md       # W1-B
      slash-commands.md                 # W1-B
    02-power-features/
      skills.md                         # W1-C
      hooks.md                          # W1-D
      subagents-and-orchestration.md    # W1-E
      mcp.md                            # W1-F
      claude-desktop.md                 # W1-G
    03-author-workflows/
      drafting-and-revision.md          # W2-A
      publishing-ops.md                 # W2-B
      marketing-and-launch.md           # W2-C
      research-and-worldbuilding.md     # W2-D
    04-reference/
      use-case-catalog.md               # W2-E (master list of author use cases)
```

## Waves

### Wave 1 — Platform & feature research (7 parallel subagents, live web)

Each agent: does live web research against official docs, writes its file(s) directly,
follows DOC_TEMPLATE.md, returns a short accuracy report (sources used, facts it
could not verify) to the orchestrator.

| ID | Slice | Output file(s) |
|----|-------|----------------|
| W1-A | Fable 5 model: capabilities, pricing, effort levels, safety classifiers/fallback, data retention, availability/rollout | `docs/fable-documentation/fable-5-model-guide.md` |
| W1-B | Claude Code basics: install, first run, CLAUDE.md & memory, settings.json, permissions/modes, slash commands | the four `01-claude-code-basics/` files |
| W1-C | Skills system: anatomy, frontmatter, invocation, authoring, where they live, marketplace/plugins | `02-power-features/skills.md` |
| W1-D | Hooks: events, configuration, matchers, exit codes, author-relevant patterns | `02-power-features/hooks.md` |
| W1-E | Subagents & orchestration: Agent tool, custom agents (.claude/agents), background tasks, workflows | `02-power-features/subagents-and-orchestration.md` |
| W1-F | MCP: what it is, connecting servers, scopes, author-relevant servers, building simple ones | `02-power-features/mcp.md` |
| W1-G | Claude Desktop + surface comparison: Desktop features, Cowork, claude.ai/code, mobile; when to use which | `02-power-features/claude-desktop.md`, `00-start-here/which-tool-when.md` |

**Orchestrator QA after Wave 1:** read every doc; verify facts against the repo's
source docs and spot-check claims; verify layering/template compliance; fix or
re-task; commit (`Add wiki: [slice]`).

### Wave 2 — Author workflow deep dives (5 parallel subagents)

These agents read the Wave 1 docs first, then write use-case docs that reference
the feature docs by relative link. They should map use cases to Carlo's existing
skill ecosystem where it exists (see "Carlo's context" below).

| ID | Slice | Output |
|----|-------|--------|
| W2-A | Drafting & revision: novel pipelines, chapter workflows, story bibles/NPE, prose audits, continuity | `03-author-workflows/drafting-and-revision.md` |
| W2-B | Publishing ops: formatting, EPUB/Vellum, metadata, blurbs, file conversion automation | `03-author-workflows/publishing-ops.md` |
| W2-C | Marketing & launch: ad copy, email, social, series marketing, launch checklists | `03-author-workflows/marketing-and-launch.md` |
| W2-D | Research & worldbuilding: genre/market research, comps, timelines, world wikis, deep research | `03-author-workflows/research-and-worldbuilding.md` |
| W2-E | Use-case catalog: master table of author use cases × tool (CLI/Desktop) × feature (skill/hook/subagent/MCP) × difficulty | `04-reference/use-case-catalog.md` |

**Orchestrator QA after Wave 2:** same review pass; check cross-links resolve; commit.

### Wave 3 — Starter-kit assembly (orchestrator-led)

1. `00-start-here/quick-start.md` — author's first 30 minutes, zero to first win.
2. `00-start-here/glossary.md` — every term used anywhere in the wiki, plain language.
3. `wiki/README.md` — wiki home: map of contents + suggested learning path
   (beginner → workflows → power features). Include `managing-usage-and-cost.md`
   early in the learning path.
4. Final QA sweep: link check, terminology consistency vs glossary, no orphan docs.
   Also verify the ⚠️-flagged claims in `managing-usage-and-cost.md` against official
   Anthropic docs (per-turn history resend mechanics, `/cost` command, effort-level
   cost behavior).
5. Final commit + update PROGRESS.md to DONE.

## Token discipline (binding for orchestrator and all subagents)

See the "Token discipline" section of the workspace `CLAUDE.md` — it is binding here.
Operational consequences for this project:

- Wave 2/3 subagents read Wave 1 docs **surgically** (section-targeted), not in full,
  except where the slice genuinely requires a full read.
- Subagent reports follow the cap in DOC_TEMPLATE.md (≤1 page, no raw dumps).
- Orchestrator QA reads produced docs once, in full, per wave — then relies on
  PROGRESS.md notes instead of re-reading.
- One handoff file per session end, dated, in `workspace-agents/handoffs/`.

## Carlo's context (for Wave 2 agents)

Carlo is an author/indie publisher/AI educator (FFA brand, courses on Teachable).
Primary research focus: **NPE (Narrative Physics Engine)** — constraint/tension-based
story development, AI-facing story bibles, "ghost draft" method for subtext.
He already has a large skill ecosystem; workflow docs should mention that skills
like these exist as the natural "next level" (names as installed):
- Drafting: `chapter-production-workflow`, `novel-production-loop`, `npe-worksheet`,
  `story-dossier`, `ghost_draft`, `character-profile-maker`, `scene-brief-creator`
- Revision/QA: `dev-editor-ai`, `grumpy-gus`, `em-dash-tightening`, `ai-ism-helper`,
  `eqbench-js`, `better-pwa-analyst`
- Publishing: `ezpz-m12-formatting`, `vellum-cover-replacement`, `docx-tools`, `pdf-tools`
- Marketing: `ezpz-m0` through `ezpz-m12` suite, `author-pen-bio-generator`
- Research: `genre-research`, `book-analyst`, `book-cover-trends`, `aeon-csv-architect`,
  `deep-research`
Docs should NOT assume the reader has these — present them as "examples of what
becomes possible," with the generic technique explained first.

## Resuming in a new session

1. Read this file and [PROGRESS.md](PROGRESS.md).
2. Pick up at the first wave/item not marked done.
3. Subagent prompts must always include: the output file path(s), instruction to read
   `workspace-agents/DOC_TEMPLATE.md` first, the live-web-research mandate with
   official-source citation, and the requirement to return an accuracy report.
4. Orchestrator never publishes a subagent doc without reading it.

## Source-of-truth URLs for research agents

- https://code.claude.com/docs (Claude Code docs root; subpages for skills, hooks,
  sub-agents, MCP, settings, memory, slash commands)
- https://platform.claude.com/docs (Claude API/platform docs, model overview)
- https://www.anthropic.com/news/claude-fable-5-mythos-5 (Fable 5 launch)
- https://support.claude.com (Desktop/plan/usage help center)
- Repo-local: `docs/fable-documentation/*.md` (launch announcement + email)
