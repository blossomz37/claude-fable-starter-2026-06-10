# Marketing & Launch: From Manuscript to Megaphone

> **In plain words:** Claude can turn the book you already wrote into the marketing
> you haven't written yet — blurbs, ads, emails, social posts, launch checklists.
> The trick is order of operations: extract the raw material *from the manuscript
> first*, keep it in one "marketing bible" file, and generate every channel's copy
> from that single source. This doc shows the whole pipeline, with prompts you can
> copy today.

## What it is

Most authors do marketing backwards: open a blank page and try to "write a blurb."
The manuscript already contains your best marketing — the quotable lines, the hook,
the emotional gut-punches, the tropes readers search for. The workflow in this doc
treats marketing as **extraction, then assembly**:

1. **Extract** raw material from the manuscript (a "teaser-extraction pass").
2. **Assemble** foundational copy (blurbs, taglines, personas) into one
   source-of-truth file — a *marketing bible*, the marketing cousin of your story bible.
3. **Generate** channel content (ads, emails, social) *from* that bible, so every
   piece stays consistent with every other piece.
4. **Launch** with a repeatable checklist instead of 3 a.m. panic.

Everything here works in plain conversation with [Claude Code](../01-claude-code-basics/installation-setup.md)
or [Claude Desktop](../02-power-features/claude-desktop.md). Once a step works,
you can package it as a [skill](../02-power-features/skills.md) so you never
re-type the instructions — that's the "next level" thread running through this doc.

## Why authors care

- **Marketing is the part most authors hate.** Offloading the drafting (not the
  judgment) to Claude turns a dreaded week into an afternoon of reviewing options.
- **Consistency sells series.** One marketing bible per book means your Amazon
  blurb, your newsletter, and your ads all describe the same book in the same voice.
- **Launches are checklists, not inspiration.** A launch runbook skill walks the
  same steps every release, so book 4's launch is calmer than book 1's.
- **Volume without burnout.** A launch month needs dozens of assets — subagents
  can draft them in parallel from one brief while you keep writing book 5.

## Getting started

Your first win: a teaser-extraction pass plus a starter marketing bible, in about
15 minutes.

1. Open Claude Code in your book's folder (or point Claude Desktop's Cowork at it).
2. Run the **teaser-extraction pass** — paste this prompt:

   ```
   Read my full manuscript in ./manuscript/. Extract marketing raw material into
   a new file ./marketing/raw-material.md with these sections:
   - QUOTABLE LINES: 20 short lines that work out of context (max 25 words each),
     with chapter references
   - HOOKS: the 5 strongest "what if" / situation hooks in the story
   - TROPES: every recognizable genre trope present (named the way readers name them)
   - EMOTIONAL BEATS: the 8 biggest emotional moments, each summarized in one
     spoiler-free sentence
   - SPOILER LINE: state clearly which plot points must never appear in marketing
   Do not invent anything. Everything must come from the text, with its location noted.
   ```

3. Review the file. Cut anything that misreads the book — this file feeds
   *everything* downstream, so it's worth ten careful minutes here.
4. Now create the marketing bible:

   ```
   Using ./marketing/raw-material.md and the manuscript, draft
   ./marketing/marketing-bible.md with: book metadata (title, series, genre,
   subgenre, heat/violence level, word count), one-sentence logline, 3 taglines,
   a 50-word blurb, a 150-word blurb, a 300-word retailer blurb, 2 reader personas
   (who this reader is, what they read last, what promise they're buying), and
   5 comp titles with one line each on how my book is similar and different.
   Mark every section DRAFT until I approve it.
   ```

5. Edit until each section sounds like *you*. From now on, every marketing prompt
   starts with "Read ./marketing/marketing-bible.md first."

That last sentence is the whole method. One file, always read first, always the
truth. When the blurb changes, change it *there* — everything generated afterward
inherits the fix. Add a line to your [CLAUDE.md](../01-claude-code-basics/claude-md-and-memory.md)
so you never have to say it: *"For any marketing task, read
./marketing/marketing-bible.md before writing anything."*

## Author use cases

### 1. Foundational copy: blurbs, taglines, loglines, personas, comps

Blurbs are the highest-leverage copy you own. Generate variants, then judge:

```
Read ./marketing/marketing-bible.md. Write 3 versions of the 150-word retailer
blurb, each leading with a different element: (a) the hook, (b) the protagonist's
wound, (c) the central relationship. Follow current conventions for my subgenre —
short paragraphs, a question or cliffhanger close, no spoilers past the SPOILER
LINE in raw-material.md. Then tell me which one you'd pick and why.
```

Comp positioning ("for fans of X meets Y") benefits from research first — see
[research-and-worldbuilding.md](./research-and-worldbuilding.md) for genre and
comp research workflows that feed this section of the bible.

*Packaged version:* this whole layer is one skill in a mature setup — Carlo's
`ezpz-m1-foundational-copy` skill does exactly this from an intake file. See
[Advanced](#advanced) for how the modules chain.

### 2. Channel content: ads, email, social — from the one bible

**Ad copy.** Each platform has its own conventions — Meta ads lean on emotional
hooks and visuals, Amazon ads on tight genre-and-promise text, BookBub on deal
framing and comp authors. Speak to Claude in those *general* terms and let it
draft within them:

```
Read ./marketing/marketing-bible.md. Draft 5 short ad-copy variants aimed at
cold readers of my subgenre: 2 leading with trope, 2 with emotional stakes,
1 with a comp-author angle. Keep each under 150 characters so they survive
truncation anywhere. Plain text, no hashtags, no emojis unless I ask.
```

One honest note: **character limits, ad formats, and platform policies change
constantly.** Don't let Claude (or this doc) assert a current limit from memory —
when a number matters, check the platform's own help pages that day, or have
Claude do a web search and cite the page.

**Email sequences.** Three sequences cover most indie careers — welcome (new
subscriber → knows you), launch (announce → last call), cross-sell (finished
book A → buys book B):

```
Read ./marketing/marketing-bible.md. Draft a 4-email launch sequence:
(1) cover + preorder announce, (2) excerpt teaser using a QUOTABLE LINE,
(3) launch-day email, (4) last-call with early reader quotes [PLACEHOLDER].
My voice rules are in CLAUDE.md — match them. Subject lines: give me 3 options
per email. Output one markdown file per email in ./marketing/email/launch/.
```

**Social content.** Ask for *structures*, not finished posts: hooks (the first
line that stops the scroll), captions, and carousel outlines (slide-by-slide
text for a multi-image post). Generate ten, post two — that ratio is normal.

```
Read ./marketing/marketing-bible.md and raw-material.md. Give me: 10 scroll-
stopping hook lines built from my QUOTABLE LINES, 5 caption drafts pairing a
hook with a one-line trope promise and soft CTA, and 2 carousel outlines
(6 slides each): one "tropes in this book", one "meet the protagonist".
```

**Voice consistency is a settings problem, not a prompting problem.** Put your
voice rules — banned words, sentence rhythm, "never sound like a press release",
emoji policy — in CLAUDE.md or in the style section of a marketing skill, once.
Then every channel inherits them. See [skills.md](../02-power-features/skills.md)
for how a skill carries style rules with it.

### 3. Series-level marketing

Series sell backlist; market the *shelf*, not just the new spine:

- **Reading-order page:** "Read all five book files' opening chapters and the
  series bible. Draft a reading-order page for my website: publication order,
  chronological order if different, one-line spoiler-free pitch per book."
- **Box-set copy:** a box set is a new product needing its own blurb — prompt for
  one that sells the *arc* ("five books, one slow-burn betrayal") rather than
  summarizing each volume.
- **Cross-book hooks:** "For each book, write the back-matter paragraph that
  hooks the reader into the *next* book without spoiling it."
- **Author-brand bios, pen-name aware:** "Write my bio in 25 / 50 / 150 words for
  pen name Vera Holt — romance voice, no mention of my thriller pen name. Keep a
  bios section per pen name in the marketing bible." If you run multiple pen
  names, keep one marketing-bible *folder per pen name* so voices never bleed.

*Packaged versions:* `ezpz-m8-series-marketing` and `author-pen-bio-generator`
are existing skills that formalize exactly these jobs.

### 4. Launch checklists and ARC management

A launch is ~40 small tasks in a fixed order. Capture them once as a
**launch-runbook skill** — a checklist Claude walks *with* you, asking for each
input as it's needed, writing each deliverable to the right folder, and tracking
what's done in a `launch-status.md` file. Build it by telling Claude:

```
Create a skill called launch-runbook. It walks me through my book launch in
phases: T-60 days (cover, blurb final, preorder up), T-30 (ARC team, email 1),
T-7 (ads drafted, social scheduled-for-review), launch day, T+7 (review nudge,
cross-sell email). At each step it checks ./marketing/launch-status.md, tells
me the next 3 actions, drafts whatever copy that step needs, and updates the
status file when I confirm a step is done.
```

**ARC teams** (Advance Reader Copy teams — the readers who get the book early in
exchange for honest reviews) are spreadsheet work, which makes them a great
[Claude Desktop / Cowork](../02-power-features/claude-desktop.md) job: "Build me
an ARC tracker spreadsheet: name, email, format sent, date sent, review posted
(Y/N), follow-up date, with a formula flagging anyone 14+ days overdue." Then
draft the three standard ARC emails (invitation, delivery, review-day reminder)
from the marketing bible — and send them yourself, from your own mailer.

### 5. Orchestration: tournaments and parallel channels

Two patterns from [subagents-and-orchestration.md](../02-power-features/subagents-and-orchestration.md)
map perfectly onto marketing:

**The blurb tournament.** Drafting and judging are different jobs; separate them:

```
Run a blurb tournament. Launch 3 subagents in parallel; each reads
./marketing/marketing-bible.md and drafts a 150-word blurb from a different
angle: trope-forward, character-wound-forward, plot-hook-forward. Then a 4th
judge subagent — who must NOT see which agent wrote which — scores all three
against current conventions for my subgenre and recommends one, with reasons.
Show me all three plus the judge's memo. I make the final call.
```

**Per-channel parallel generation.** Once the bible is approved, the channels
don't depend on each other — fan them out: "Launch 3 subagents from
./marketing/marketing-bible.md: one drafts the launch email sequence, one the
ad-copy variants, one the social hook bank. Each writes to its own folder under
./marketing/. Compile a summary of what was produced." Because every agent reads
the same bible, the outputs agree with each other. You review once, at the end.

## Common pitfalls

- **AI copy still needs human taste — and testing.** Claude drafts plausible ad
  copy; it cannot know what *converts* for your book. Treat every variant as a
  hypothesis. Run small tests, keep winners, feed results back into the bible
  ("trope-forward hooks outperform character hooks for this book").
- **Never auto-post.** No hook, hooks-based automation, or scheduled task should
  publish outward-facing content without a human reading it first. Generate to
  files; you press every publish button. (This is also why the prompts above say
  "scheduled-for-review", not "scheduled".)
- **Skipping the extraction pass.** Blurbs written from memory of your own book
  drift generic. The raw-material file is the difference between "a romance about
  second chances" and the actual line from chapter 22 that makes readers click.
- **Stale platform "facts."** Ad character limits, image specs, and content
  policies change quarter to quarter. Anything platform-specific in your skills
  should say "verify current specs on the platform's help page" rather than
  hard-coding numbers.
- **Disclosure norms exist — know the current ones.** As of June 2026, Amazon KDP
  requires disclosing AI-*generated* book content (text, images, translations)
  during publishing, while AI-*assisted* work (brainstorming, editing your own
  writing) does not require disclosure; enforcement has tightened. Marketing copy
  itself isn't what that checkbox covers, but ad platforms and retailers each have
  their own evolving AI rules — check the current policy pages before launch, and
  see [publishing-ops.md](./publishing-ops.md) for the publishing side.
- **Cost/usage:** parallel subagents and Cowork sessions consume usage much faster
  than chat. Run tournaments on the copy that matters (blurbs, launch emails), not
  on every caption.
- **Voice homogenization.** If your newsletter starts sounding like everyone
  else's, your voice rules are too thin. Add real examples of your own posts to
  CLAUDE.md or the skill's style section — examples beat adjectives.

## Advanced

### The modular marketing pipeline

The end-state of everything above is a **numbered suite of skill modules**, each
reading the outputs of earlier modules and writing files the later ones consume:

```
m0 intake          → book metadata + author voice + platform config → marketing plan
m1 foundational    → blurbs, taglines, loglines, personas, keywords
m2 teaser extract  → quotable lines, hooks, visual prompts from manuscript
m3 social          → reels scripts, threads, carousels
m4 email           → welcome / launch / cross-sell sequences
m5 ad copy         → per-platform paid ad variants
m6 website         → bios, book/series pages, SEO copy
m7 engagement      → reader magnets, ARC/street-team materials
m8 series          → box-set copy, reading orders, cross-book hooks
...                → trailers, covers, formatting (m10–m12)
```

This is a real, working example: **Carlo's `ezpz-m0` through `ezpz-m12` suite**
(plus an `ezpz-marketing-consultant` skill that checks which files exist in the
workspace and recommends the next runnable module). The architecture lessons
transfer even if you build your own from scratch:

- **Numbered modules with file contracts.** Each skill declares which files it
  needs (m4 requires m0's intake + m1's blurbs) and which it produces. The
  filesystem *is* the pipeline state — no module holds anything only in chat.
- **Intake first, always.** m0 captures metadata, voice, and platform choices
  *once*; every later module reads it instead of re-asking. This is the
  source-of-truth principle from [Getting started](#getting-started), formalized.
- **A consultant/router on top.** A small skill that inspects the folder,
  diagnoses what's missing ("you have a bible but no teaser file — run m2 next"),
  and routes. Cheap to build, removes all "what do I do next?" friction.

### Build a 3-module starter yourself

You don't need thirteen modules. Three cover 80% of a launch. Tell Claude Code:

```
Create three skills in ~/.claude/skills/:

1. market-m0-intake — interviews me for book metadata, genre, heat level, comps,
   and voice rules (asks for 3 sample paragraphs of my own marketing writing),
   then writes ./marketing/intake.md. Refuses to run if the file already exists
   unless I say "refresh".

2. market-m1-foundation — requires ./marketing/intake.md and a manuscript path.
   Runs the teaser-extraction pass to ./marketing/raw-material.md, then drafts
   ./marketing/marketing-bible.md (loglines, taglines, 3 blurb lengths, personas,
   comp positioning). Marks all sections DRAFT; a second run in "revise" mode
   applies my edits.

3. market-m2-channels — requires the approved marketing-bible.md. Asks which
   channel (email / ads / social), then generates that channel's assets into
   ./marketing/<channel>/, following the voice rules from intake.md. Never
   schedules or posts anything.
```

Each skill's `SKILL.md` should begin with a **preconditions block** ("if
./marketing/intake.md does not exist, stop and tell the user to run
market-m0-intake") — that's what makes modules composable instead of fragile.
See [skills.md](../02-power-features/skills.md) for SKILL.md anatomy and
frontmatter, and [hooks.md](../02-power-features/hooks.md) if you later want a
hard guarantee (e.g., a hook that blocks any tool call resembling "post" or
"send" during marketing sessions).

### Judge agents with real criteria

The blurb tournament improves sharply when the judge has a rubric file. Keep
`./marketing/genre-conventions.md` (built via [genre research](./research-and-worldbuilding.md))
listing what working blurbs in your subgenre actually do — opening-line patterns,
trope-naming norms, length, close style. Define the judge as a custom subagent
(`.claude/agents/blurb-judge.md`) whose system prompt says: *score only against
./marketing/genre-conventions.md; never reward 'beautiful writing' that violates
genre signaling.* Anatomy of custom agent files:
[subagents-and-orchestration.md](../02-power-features/subagents-and-orchestration.md).

### Connecting outward (carefully)

[MCP servers](../02-power-features/mcp.md) can connect Claude to your mailing-list
provider, Canva, Notion, or spreadsheets — useful for *reading* campaign stats
into the bible or *drafting* a design brief. Keep the never-auto-post rule:
connect read/draft capabilities freely, and leave the send/publish action in
human hands, enforced by [permissions](../01-claude-code-basics/settings-and-permissions.md)
(deny or always-ask on any send-class tool).

### Cover concepts and ad imagery via image APIs

Claude doesn't draw, but it can drive image APIs the way it drives the marketing
pipeline: prompt-craft from the marketing bible, batch generation, file naming per
platform, and a contact sheet for your judgment pass. Two verified entry points:
the **Ideogram API** (its documented strength is legible text *inside* images —
titles and taglines on ad cards; it also publishes a hosted MCP server, so you can
connect it like any [MCP](../02-power-features/mcp.md) and skip scripting entirely)
and the **OpenAI Images API** (gpt-image models, generation plus edits) for
character art and scene imagery. Both bill separately from Claude, per image.
⚠️ Midjourney has no broadly available official public API — Discord/web only, and
unofficial proxy APIs risk your account — so treat Midjourney jobs as manual with
Claude doing the prompt-writing. These are *concept and ad* images; a retail cover
still goes through a human designer or your own typography pass. Full row list:
[use-case-catalog.md → Multimedia](../04-reference/use-case-catalog.md#10-multimedia-audio--image-generation).

## Sources

- Repo wiki docs cross-referenced: `skills.md`, `subagents-and-orchestration.md`,
  `mcp.md`, `claude-desktop.md`, `hooks.md`, `settings-and-permissions.md`,
  `claude-md-and-memory.md` (read 2026-06-10).
- Amazon KDP Content Guidelines (AI-generated vs AI-assisted disclosure):
  https://kdp.amazon.com/en_US/help/topic/G200672390 (accessed 2026-06-10).
- Carlo's `ezpz-m0`–`ezpz-m12` skill suite (installed locally) — used as the
  worked example of a modular marketing pipeline.
- https://developer.ideogram.ai/ — official Ideogram API docs: generation, remix,
  text rendering, hosted MCP server (accessed 2026-06-10).
- https://developers.openai.com/api/docs/guides/image-generation — official OpenAI
  Images API guide: gpt-image models, generation and edits (accessed 2026-06-10).
- ⚠️ Midjourney: no official public API confirmed as of 2026-06-10 — its official
  docs site returned HTTP 403 to our fetch; web search corroborates Discord/web-only
  access, with unconfirmed third-party claims of a restricted enterprise API.
- ⚠️ By design, this doc avoids platform-specific numbers (ad character limits,
  image specs, pricing) because they change frequently; readers are directed to
  current platform help pages. No such numbers are asserted here.
- ⚠️ Unverified: third-party reports of KDP AI-disclosure enforcement tightening
  in April 2026 come from secondary sources, not an Amazon announcement; the doc
  states it softly ("enforcement has tightened").
