# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This workspace exists to learn about and test Claude Fable 5 capabilities. It is a documentation/experimentation sandbox, not a software project — there is no build system, no tests, and no application code. It is also not currently a git repository.

## Structure

- `docs/fable-documentation/` — reference material about Claude Fable 5 and Claude Mythos 5 (the Anthropic launch announcement and related notes). Treat these as source-of-truth context when answering questions about Fable 5's capabilities, pricing ($10/$50 per Mtok), safety classifiers (cyber/bio/distillation fallback to Opus 4.8), and availability.

## Working here

- Experiments, test artifacts, and notes created while exploring Fable capabilities should be saved into this workspace with descriptive names so they can be found in later sessions.
- Keep new reference material about Fable/Mythos under `docs/fable-documentation/`.

## Token discipline (applies to every session)

Fable 5 usage burns fast; the main cost is conversation history re-sent every turn.

- **No meta-narration.** No progress recaps, no restating the plan, no "Now I will...".
  Confirm completion of a step in one line.
- **Read surgically.** Read targeted line ranges, not whole files repeatedly. Never
  re-read a file already in context unless it changed.
- **Subagents are token firewalls.** Heavy reading (web research, multi-chapter
  read-throughs) goes to subagents. They return only the fixed short report defined in
  `workspace-agents/DOC_TEMPLATE.md` — never raw research dumps.
- **Match model to step.** Fable-class effort for orchestration, judgment, and final QA;
  cheaper/faster models for mechanical passes (formatting, template fill-in) when the
  environment allows model routing.
- **End sessions at logical boundaries.** After a wave/logical unit, write a handoff to
  `workspace-agents/handoffs/` (dated filename) and stop, rather than continuing a
  bloated session. The next session resumes from the handoff + `PROGRESS.md` only.
- **Files over chat history.** `PROGRESS.md` and handoff files are the durable memory;
  keep them terse and authoritative so fresh sessions can resume cheaply.
- **Do not over-trim.** Never skip self-verification/QA passes to save tokens — trim
  narration, not reasoning.
