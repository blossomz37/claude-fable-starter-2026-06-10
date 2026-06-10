# Fable Wiki Session Handoff

Date: 2026-06-10
Workspace: `/Users/carlo/Github/claude-fable-starter`
Project: Claude Fable starter kit wiki for indie authors using Claude Code CLI and Claude Desktop

## What this session was doing

The session was building a tooling-heavy, end-to-end local wiki in `docs/wiki/` for indie authors. The reader model is layered: plain-language top half for non-technical authors, Advanced sections for power users.

The orchestrator used subagents for slice-based research and drafting, then planned to perform human-style QA before updating progress and committing each wave.

## Decisions of record

1. Audience is both beginner and advanced, layered in every doc.
2. Coverage is tooling-heavy, not model-only.
3. All four author-workflow areas must get deep dives: drafting and revision, publishing ops, marketing and launch, research and worldbuilding.
4. Research standard is live web verification against official Anthropic/support docs where applicable.
5. `workspace-agents/` holds the agent-facing plan, template, progress, and now this handoff.
6. `README.md` must eventually become the user-facing guide.
7. Remote is `https://github.com/blossomz37/claude-fable-starter-2026-06-10` and work should be pushed at checkpoints.

## Methodology used

### Orchestrator pattern

The main session acted as orchestrator, not bulk writer.

1. Define the target wiki shape in `workspace-agents/IMPLEMENTATION_PLAN.md`.
2. Define a strict doc contract in `workspace-agents/DOC_TEMPLATE.md`.
3. Launch tightly scoped research/drafting subagents per slice.
4. Require each subagent to return an accuracy report with:
   - files written
   - official sources fetched
   - unverified claims
   - anything surprising/newer than expected
5. Do not trust subagent output blindly. Read the produced docs before marking the wave done.
6. Commit per logical unit only after orchestrator QA.

### Doc-writing standard

Every doc should follow the template in `workspace-agents/DOC_TEMPLATE.md`:

- plain-English title
- "In plain words" intro
- What it is
- Why authors care
- Getting started
- Author use cases
- Common pitfalls
- Advanced
- Sources

Style rules that matter:

- plain language above Advanced
- no hype
- author examples, not generic software examples
- cross-link related docs
- if a claim cannot be verified, mark it explicitly

### Research standard

- Prefer official Anthropic / Claude Code / support sources.
- Use repo-local source docs under `docs/fable-documentation/` for Fable launch facts.
- Synthesis docs may rely on already-verified Wave 1 docs, but should say so.
- Never invent commands, settings, paths, or feature names if the docs are unclear.

## Completed work

### Planning artifacts completed

- `workspace-agents/IMPLEMENTATION_PLAN.md`
- `workspace-agents/DOC_TEMPLATE.md`
- `workspace-agents/PROGRESS.md`

### Wave 1 completed and already QA'd

Wave 1 is complete. `workspace-agents/PROGRESS.md` already marks these as done:

- `docs/fable-documentation/fable-5-model-guide.md`
- `docs/wiki/00-start-here/which-tool-when.md`
- `docs/wiki/01-claude-code-basics/installation-setup.md`
- `docs/wiki/01-claude-code-basics/claude-md-and-memory.md`
- `docs/wiki/01-claude-code-basics/settings-and-permissions.md`
- `docs/wiki/01-claude-code-basics/slash-commands.md`
- `docs/wiki/02-power-features/skills.md`
- `docs/wiki/02-power-features/hooks.md`
- `docs/wiki/02-power-features/subagents-and-orchestration.md`
- `docs/wiki/02-power-features/mcp.md`
- `docs/wiki/02-power-features/claude-desktop.md`

Wave 1 findings surfaced in progress notes:

- slash commands have largely merged into skills
- hook surface is larger than expected, around 31 events
- Desktop is a three-tab Chat/Cowork/Code app
- Tool Search defers MCP tools by default
- the Fable 5 inclusion window remained June 9–22 as of the last verified check that day

### Wave 2 draft outputs now exist, but orchestrator QA is still pending

These files are present in the repo and appear to be the outputs of the interrupted subagent run:

- `docs/wiki/03-author-workflows/drafting-and-revision.md` — 404 lines
- `docs/wiki/03-author-workflows/publishing-ops.md` — 386 lines
- `docs/wiki/03-author-workflows/marketing-and-launch.md` — 353 lines
- `docs/wiki/03-author-workflows/research-and-worldbuilding.md` — 393 lines
- `docs/wiki/04-reference/use-case-catalog.md` — 317 lines

Important: `workspace-agents/PROGRESS.md` still shows all Wave 2 items as not started. That is stale relative to the file tree. The next session should not restart Wave 2 drafting from scratch; it should do orchestrator QA on the files that already landed, then update progress.

### Verified subagent outputs captured in the session history

Two Wave 2 slices were explicitly reported back in the session log:

1. `marketing-and-launch.md`
   - completed to spec
   - one live KDP AI-disclosure verification performed
   - soft/unverified claim about April 2026 KDP enforcement was flagged, not asserted as fact

2. `use-case-catalog.md`
   - 97 distinct use cases across 9 categories
   - synthesis doc built from already-verified Wave 1 docs
   - EPUB/Vellum automation limitations were flagged honestly as workarounds/unverified areas

The three other Wave 2 files exist locally but do not have copied accuracy reports in the preserved session excerpt. Treat them as present but not yet orchestrator-approved.

## Promised but not yet implemented

There is one explicit promised addition that is not yet in the plan structure or file tree:

- `docs/wiki/03-author-workflows/adopting-and-sharing-tools.md`

Why it exists:

The user asked how Fable should decompose shared author tools and repos so they can be customized and re-shared cleanly. The session answered with a three-phase method:

1. intake interrogation
2. cleanup and layer separation
3. portability re-architecture

That answer should be turned into a real wiki doc with copy-paste prompts and should also feed the use-case catalog.

Core method from that answer:

- separate a tool into engine, conventions, and personal layer
- interrogate the repo instead of trying to understand it manually
- move user-specific assumptions into `PROFILE.md`
- ship an `ADAPTING.md` interview so a new user's Claude can configure the tool for them
- maintain `CUSTOMIZATIONS.md` so upstream updates can be re-applied cleanly

## Where to jump back in

Do not resume by launching more research agents immediately.

The correct re-entry point is:

1. Read `workspace-agents/IMPLEMENTATION_PLAN.md`.
2. Read `workspace-agents/PROGRESS.md`.
3. Read this handoff.
4. Read all five Wave 2 output docs that already exist.
5. Perform Wave 2 orchestrator QA before making new promises or launching new subagents.

## Exact next actions

### Next action block A: Wave 2 QA

1. Read all five Wave 2 files in full.
2. Verify template compliance against `DOC_TEMPLATE.md`.
3. Check cross-links between the four `03-author-workflows` docs and `04-reference/use-case-catalog.md`.
4. Spot-check any official-source claims where the docs make concrete assertions.
5. Confirm the two explicitly flagged limitations remain clearly labeled:
   - EPUB generation/validation
   - Vellum automation
6. Decide whether each file is:
   - pass as-is
   - needs small orchestrator edits
   - needs re-tasking

### Next action block B: progress and commit hygiene

If Wave 2 passes QA:

1. Update `workspace-agents/PROGRESS.md` to mark W2-A through W2-E done.
2. Mark Wave 2 orchestrator QA + commit done.
3. Commit with a message in the existing style, for example:
   - `Add wiki: Wave 2 author workflows and use-case catalog`
4. Push to the configured GitHub remote.

### Next action block C: Wave 3 assembly

After Wave 2 is committed:

1. Create `docs/wiki/00-start-here/quick-start.md`
2. Create `docs/wiki/00-start-here/glossary.md`
3. Create `docs/wiki/README.md`
4. Create `docs/wiki/03-author-workflows/adopting-and-sharing-tools.md`
5. Update `docs/wiki/04-reference/use-case-catalog.md` if the new adopting/sharing doc adds use cases worth cataloging
6. Make `README.md` the user-facing guide as requested in progress notes
7. Run a final QA sweep for links, consistency, and orphaned terminology

## QA checklist for the next session

- Are the Wave 2 docs still clearly layered for beginners first, power users second?
- Do they explain generic technique first and only then mention Carlo's existing skills as examples?
- Are any feature claims relying on stale June 2026 assumptions that should be re-checked?
- Does the use-case catalog still align with the current feature docs?
- Does the new `adopting-and-sharing-tools.md` fill the exact gap the user identified?
- Does `README.md` now orient end users rather than serving as a minimal repo note?

## Repo-state note

At the time this handoff was written, the working tree appeared clean and the Wave 2 output files were already present on disk. That strongly suggests the interruption happened after subagent writes landed but before orchestrator review, progress update, and checkpoint commit.

## Minimal resume script

If you want the shortest reliable restart path, use this sequence:

1. Read `workspace-agents/IMPLEMENTATION_PLAN.md`
2. Read `workspace-agents/PROGRESS.md`
3. Read `workspace-agents/handoffs/2026-06-10-fable-wiki-session-handoff.md`
4. Read the five existing Wave 2 docs
5. QA Wave 2
6. Update progress
7. Commit and push
8. Build Wave 3, including `adopting-and-sharing-tools.md`
9. Turn `README.md` into the user-facing entry point

## Files to read first next time

- `workspace-agents/IMPLEMENTATION_PLAN.md`
- `workspace-agents/DOC_TEMPLATE.md`
- `workspace-agents/PROGRESS.md`
- `docs/wiki/03-author-workflows/drafting-and-revision.md`
- `docs/wiki/03-author-workflows/publishing-ops.md`
- `docs/wiki/03-author-workflows/marketing-and-launch.md`
- `docs/wiki/03-author-workflows/research-and-worldbuilding.md`
- `docs/wiki/04-reference/use-case-catalog.md`