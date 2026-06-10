# Wiki Doc Template & Style Guide

Every wiki doc MUST follow this structure and style. The audience is layered:
indie authors first (often non-technical), power users second.

## Required structure

```markdown
# [Plain-English Title]

> **In plain words:** 2–4 sentences. What this is, why an author should care,
> what it lets you do. No jargon — or jargon immediately defined.

## What it is
Plain-language explanation. Analogies to author-world concepts welcome
(story bible, beta reader, editorial assistant, series bible, etc.).

## Why authors care
Concrete author-flavored payoffs. Short bullet list.

## Getting started
Numbered, copy-pasteable steps. Assume macOS first but note Windows where it differs.
The reader should get a first win in minutes.

## Author use cases
3–8 concrete scenarios with enough detail to actually try them.
Where relevant, note "this can be packaged as a skill/hook/subagent" with a link.

## Common pitfalls
Honest list. Include cost/usage notes where relevant.

## Advanced
The power-user layer: full configuration surface, exact file paths, JSON/YAML
examples, edge cases, integration with other features. Technical depth lives
HERE, not above.

## Sources
Bullet list of official URLs consulted, with access date (2026-06-10).
Flag anything you could NOT verify against an official source as
"⚠️ Unverified: ..." — do not silently guess.
```

## Style rules

1. **Plain language above the Advanced line.** Define every technical term on first
   use. An author who has never opened a terminal must be able to follow the top half.
2. **No hype.** No "game-changer", "supercharge", "unleash". State what things do.
3. **Concrete over abstract.** "Claude reads your story bible before drafting chapter 12"
   beats "context-aware generation".
4. **Examples use author scenarios** — manuscripts, chapters, blurbs, series bibles,
   ARC teams — never generic "my_project" or todo apps.
5. **Cross-link** related wiki docs with relative markdown links.
6. **Accuracy over completeness.** If the official docs are ambiguous or you cannot
   verify a detail, say so explicitly in the doc and in your report. Never invent
   flags, file paths, or menu names.
7. **Costs and plans:** when a feature has usage/pricing implications, say so plainly.
8. Length target per doc: roughly 150–350 lines. Substantial, not bloated.
9. Use `claude-fable-5` / "Fable 5" naming consistently; today's date is 2026-06-10.

## Subagent reporting requirement

After writing your file(s), your final message back to the orchestrator must contain:
- File(s) written and approximate line counts
- Official sources actually fetched (URLs)
- A list of claims you could not verify (or "none")
- Anything surprising/newer than expected that the orchestrator should know

Your report is the ONLY thing that enters the orchestrator's context. Keep it under
one page. Do NOT paste doc contents, raw research notes, or fetched page text back
to the orchestrator — write findings into your output file(s) instead.

## Subagent token discipline

- No progress narration in your messages; work silently, report once at the end.
- Read source files surgically (targeted sections), and never re-read a file already
  in your context unless it changed.
- Fetch each external source once; take notes into your draft rather than re-fetching.
