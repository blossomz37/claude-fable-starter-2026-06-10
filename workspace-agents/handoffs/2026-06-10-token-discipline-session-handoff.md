# Token Discipline Session Handoff

Date: 2026-06-10 (second session this date; follows `2026-06-10-fable-wiki-session-handoff.md`)
Workspace: `/Users/carlo/Github/claude-fable-starter`

## What this session did

Hardened token-burn mitigation into the workspace after Carlo asked how to make
Fable 5 usage last. No wiki-wave work was performed; Wave 2 remains next.

## Changes (committed `60a69cb`, pushed)

1. **New wiki page:** `docs/wiki/00-start-here/managing-usage-and-cost.md` —
   author-facing token economics (per-turn history resend is the real cost), five
   habits, "write to a file saves tokens" myth debunked. Contains ⚠️-flagged claims
   pending live verification in Wave 3 QA.
2. **`CLAUDE.md`:** new binding "Token discipline" section (no meta-narration,
   surgical reads, subagent firewalls, model routing, end-at-boundaries handoffs,
   don't over-trim reasoning).
3. **`workspace-agents/DOC_TEMPLATE.md`:** subagent report hard-capped at ≤1 page,
   no raw dumps; subagent token-discipline rules added (silent work, fetch once).
4. **`workspace-agents/IMPLEMENTATION_PLAN.md`:** new page added to wiki structure;
   Wave 3 must include it in learning path and verify its ⚠️ claims; binding
   token-discipline section for orchestrator + subagents.
5. **`workspace-agents/PROGRESS.md`:** out-of-wave additions logged; session log entry.
6. Prior session's handoff file was untracked — now committed.
7. Repo memory note created (`/memories/repo/conventions.md`) with workspace conventions.

## Decisions of record

1. Token discipline is binding for orchestrator and all subagents (CLAUDE.md is the
   canonical statement; plan and template reference/operationalize it).
2. Wave 3 final QA must live-verify the ⚠️ claims in managing-usage-and-cost.md
   (history-resend mechanics, `/cost` command, effort-level cost behavior).
3. `workspace-carlo/` stays untracked (chat history appears intentionally gitignored).

## Next session should

1. Resume **Wave 2** per `IMPLEMENTATION_PLAN.md` (W2-A through W2-E subagents),
   now under the new subagent report cap and token-discipline rules.
2. Read only: this handoff + `PROGRESS.md` + plan sections needed per slice.
