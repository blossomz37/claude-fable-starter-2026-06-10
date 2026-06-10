# Publishing Ops: From Finished Draft to Retailer-Ready Files

> **In plain words:** Once the book is written, a second job begins: converting
> files, formatting interiors, writing metadata, checking print specs, and keeping
> ten books' worth of back matter in sync. Claude is very good at this unglamorous
> production work — it can write and run the conversion scripts, sweep for stray
> straight quotes, build your ISBN spreadsheet, and remember the checklist so you
> don't have to. This doc shows how, safely.

## What it is

Publishing operations is everything between "the manuscript is done" and "the book
is live": file conversion (Markdown ⇄ Word ⇄ EPUB), front and back matter, metadata
(categories, keywords, blurb), print checks, and the proofing passes that catch
embarrassments before readers do.

Two ideas make Claude unusually useful here:

1. **Most publishing-ops tasks are mechanical.** "Convert every chapter to one DOCX,"
   "find every scene break that isn't `***`." Mechanical tasks become small scripts
   that run the same way every time — and Claude writes, runs, and maintains those
   scripts for you. You don't need to learn scripting; you need to learn to *ask*.
2. **The rest is judgment, and Claude assists rather than decides.** Which categories
   fit your book, whether the blurb sings — Claude drafts options and checks
   constraints; you choose.

A rule for this whole doc: **deterministic checks become scripts (or
[hooks](../02-power-features/hooks.md)); judgment checks stay as prompts.** A script
counts your em-dashes identically every run; a prompt asks "does this scene break
feel right?" A vibes-based answer to "how many chapters use the wrong header
format" is worse than useless.

## Why authors care

- **One command instead of an afternoon.** Chapter folder → clean EPUB with cover
  and table of contents, repeatably, in seconds.
- **Series consistency without rereading nine books.** A skill updates the "Also by"
  page and back-matter links across the whole series when book 10 launches.
- **Fewer Vellum/Atticus import surprises.** Claude normalizes scene breaks, quotes,
  and headings *before* your formatter sees the file.
- **Real spreadsheets, real Word docs.** Claude Desktop's Cowork tab delivers actual
  `.xlsx` ISBN trackers and `.docx` files with proper styles — see
  [Claude Desktop](../02-power-features/claude-desktop.md).
- **The checklist never forgets.** A release-checklist skill walks the same 30 steps
  for every launch, flagging which ones need *you*.

## Getting started

First win: turn a folder of chapter files into one Word document, with your originals
protected before anything runs.

1. **Install pandoc** — the free, open-source document converter that is still the
   standard tool for Markdown ⇄ DOCX ⇄ EPUB in 2026. On macOS:

   ```bash
   brew install pandoc
   ```

   (Windows: download the installer from pandoc.org. Or just ask Claude Code to
   install it — it will run the right command for your system after you approve.)

2. **Set up a production folder structure.** In Claude Code, inside your book
   project, ask:

   ```text
   Create this folder structure: originals/ (untouchable archive), manuscript/
   (working chapter files), front-matter/, back-matter/, output/ (generated
   files), published/ (final uploaded files, also untouchable). Then add
   permission deny rules so you can never edit or write inside originals/ or
   published/.
   ```

   Claude creates the folders and writes the deny rules into
   `.claude/settings.json` — see
   [Settings & Permissions](../01-claude-code-basics/settings-and-permissions.md)
   for what those rules mean. The convention to internalize: **Claude never touches
   `originals/` or `published/`. Everything Claude generates lands in `output/`,
   and only you promote files into `published/`.**

3. **Copy your chapters in** (to `manuscript/`, originals stay in `originals/`).

4. **Convert.** Ask Claude Code:

   ```text
   Combine all the chapter files in manuscript/ in order into a single DOCX at
   output/MyBook_full_v1.docx using pandoc. Scene breaks are blank lines around
   ***. Show me the command before running it.
   ```

   Claude proposes something like
   `pandoc manuscript/ch*.md -o output/MyBook_full_v1.docx`, you approve, and
   you have a Word file ready for your editor — or for Vellum.

5. **Look at the file** in Word/Pages/LibreOffice. Claude can verify a conversion ran;
   only your eyes verify it looks right.

## Author use cases

### 1. Markdown → EPUB, repeatably

Pandoc produces valid EPUB3 directly from Markdown, including cover, metadata, and
table of contents. Have Claude create a `metadata.yaml` (title, author, language,
rights, series info) once, then the conversion is one line:

```bash
pandoc metadata.yaml manuscript/ch*.md -o output/MyBook.epub \
  --toc --epub-cover-image=cover.jpg --css=styles/epub.css
```

Ask Claude to wrap that in a script (`scripts/build-epub.sh`) so "rebuild the EPUB"
is one request forever after. Claude can also install and run **EPUBCheck** (the
industry-standard validator) on the output and translate its error messages into
plain English. This whole routine is a natural
[skill](../02-power-features/skills.md) — Carlo's `ezpz-m12-formatting` skill is an
example of exactly this pattern, packaged.

### 2. DOCX work: pandoc for conversion, the docx skill for fidelity

Two different jobs, two tools:

- **Conversion** (Markdown → DOCX for your editor, DOCX → Markdown to bring an
  edited file back): pandoc. Useful flag when ingesting an edited file:
  `--track-changes=accept` (or `reject`/`all`) controls how Word's tracked changes
  are handled.
- **Working *inside* a Word file** where styles, headers, and layout fidelity
  matter (an editor's styled template, a publisher's submission format): Anthropic
  ships document skills for **docx, pdf, xlsx, and pptx** that read and produce
  real Office files — available in Claude Code via the official skills marketplace
  and built into claude.ai/Desktop. See [skills.md](../02-power-features/skills.md)
  for installing them. Locally, skills like Carlo's `docx-tools` and `pdf-tools`
  follow the same pattern: create the file programmatically, then render and
  visually verify the layout.

Tip: ask Claude to use a `--reference-doc=template.docx` with pandoc so generated
Word files inherit your (or your editor's) styles instead of pandoc's defaults.

### 3. Vellum-adjacent: Claude prepares, Vellum formats

Vellum remains Mac-only and proprietary (no Windows version exists or is announced;
Atticus and Lacuna are the usual cross-platform alternatives). Claude doesn't
replace your formatter — it makes the input clean so the import doesn't fight you:

```text
Prepare output/MyBook_for_vellum.docx from manuscript/: chapter titles as
Heading 1, no other heading levels, scene breaks normalized to a single ***
paragraph, no tabs or double spaces, no manual page breaks, smart quotes
throughout. Report everything you changed.
```

Vellum's importer keys on heading styles for chapter detection, so this
normalization is most of the battle. The same prep works for Atticus.
(Carlo's `vellum-cover-replacement` skill is an example of automating one
narrow Vellum-adjacent chore.)

### 4. Front and back matter, generated and maintained

Front matter (title page, copyright page, dedication) and back matter ("Also by,"
newsletter signup, review ask) are templates with variables — ideal skill material.
The high-value version is **series back-matter maintenance**: when book 10 launches,
books 1–9 all need updated "Also by" pages and a link to the new book. As a skill:

```text
/backmatter-update --new-book "Book 10 Title" --asin B0XXXXXXXX
```

The skill loops over each earlier book's back-matter source file, inserts the new
title and link in series order, rebuilds each EPUB, and produces a diff report for
your review. What used to be an evening of error-prone copy-paste becomes ten
minutes of checking diffs. (You still re-upload to KDP yourself — uploads are a
human step.)

### 5. Cleanup passes: quotes, dashes, scene breaks

Classic pre-format sweeps, all deterministic, all scriptable:

- **Smart-quote pass:** convert straight quotes/apostrophes to curly. The trap is
  apostrophes at word starts (*'Tis*, *'em*, decade abbreviations like *'90s*)
  curling the wrong way — ask Claude to script the conversion *and list every
  leading-apostrophe case for manual review* rather than guessing.
- **Em-dash and ellipsis normalization:** `--` → `—`, `. . .` vs `…` made
  consistent. (Reducing em-dash *overuse* is a judgment-plus-counting job — Carlo's
  `em-dash-tightening` skill shows the full version: classify, count, reduce to a
  target density with versioned output.)
- **Scene-break normalization:** find every variant (`***`, `* * *`, `#`, blank
  lines, `~`) and unify to one form. Script reports each occurrence with line
  numbers; you approve the rewrite.

Run these as scripts with a diff you review — never as freehand "fix my whole
manuscript" prompts (see pitfalls).

### 6. KDP metadata: categories, keywords, blurb HTML

- **Research:** "Search current Amazon categories for slow-burn fantasy romance;
  give me 10 candidate categories and 7 keyword strings under 50 characters each,
  with reasoning." Claude's web search gets you a strong draft; final picks are
  judgment (and rankings shift — verify in your KDP dashboard). Current limits:
  **3 categories and 7 keywords per format** (each format gets its own slots).
- **Blurb formatting:** KDP descriptions allow limited HTML — `<br>`, `<p>`, `<b>`,
  `<em>`, `<i>`, `<u>`, `<h4>`–`<h6>`, and `<ol>`/`<ul>` lists — with a **4,000
  character limit that includes the tags** (verified against KDP help, 2026-06-10).
  `<h1>`–`<h3>`, links, images, and CSS are not supported. Ask Claude to convert
  your blurb to KDP-safe HTML *and report the character count including tags*.
  Paste the HTML directly into the description field, not via the rich-text toolbar.
- **Series consistency:** keep a `series-metadata.yaml` (series name spelling,
  reading order, pen name, tagline, keywords) and have Claude audit every book's
  metadata against it: "Check books 1–9 metadata files against
  series-metadata.yaml and list every mismatch."

### 7. Print-ready checks and the ISBN spreadsheet

- **Page-count estimate:** Claude can compute a *rough* estimate from word count
  (commonly ~250–300 words per page at a 5×8 or 5.5×8.5 trim with ordinary
  settings) — good enough for cost and spine ballparks, **not** a substitute for
  the real count from your formatted PDF. From an actual page count, spine width
  is deterministic (KDP: pages × per-page paper thickness; their cover calculator
  is the source of truth).
- **Widow/orphan-prone constructions:** true widows/orphans only exist after
  typesetting, but Claude can flag the *risk patterns* in source — one-word
  paragraph endings, single-sentence paragraphs at section ends, very long
  unbroken paragraphs — so you fix them before formatting instead of nudging
  text in Vellum.
- **ISBN tracker:** in Claude Desktop's Cowork tab: "Build an Excel workbook
  tracking my ISBNs: one row per ISBN with title, format, imprint, assignment
  date, status; a formula flagging unassigned ISBNs; one sheet per pen name."
  Cowork writes a real `.xlsx` with working formulas to your folder — see
  [Claude Desktop](../02-power-features/claude-desktop.md).

### 8. Proofing passes (not revision)

Proofing is the last sweep before upload — distinct from
[drafting and revision](drafting-and-revision.md). Split it cleanly:

- **Deterministic audits (scripts):** duplicated words ("the the"), straight
  quotes after the smart-quote pass, double spaces, inconsistent chapter headers,
  scene-break variants, unclosed quotation marks. Run as a `format-check` script
  (see Advanced) — same results every run, zero tokens after the script exists.
- **Judgment sweeps (prompts/subagents):** real typo hunting needs reading.
  Dispatch parallel [subagents](../02-power-features/subagents-and-orchestration.md):
  "One subagent per chapter: list likely typos, homophone errors (peak/pique),
  and dropped words — report file, line, quote, suggested fix. Change nothing."
  You apply fixes from the report. Token-heavy — reserve for the final pass.
- **Dialogue punctuation audit** sits between: a script finds `."` vs `,"`
  patterns around dialogue tags; deciding whether *"she said"* is a tag or an
  action beat takes judgment. Script finds candidates; Claude reads only those.

### 9. Cover-adjacent text ops

Claude doesn't design covers, but every word *on or near* the cover is text ops:

- **Cover copy:** front-cover tagline options, back-cover print blurb (shorter
  than the KDP description), hardcover flap copy.
- **Spine text check:** KDP requires **at least 79 pages** for spine text, with
  0.0625" clearance each side. Ask Claude: "My book is 212 pages on cream paper —
  what's the spine width per KDP's formula, and does 'THE SALT ROADS — K. MERCER'
  plausibly fit at 7pt+?" Claude does the arithmetic; your cover designer confirms
  visually.
- **A+ Content:** Amazon's image-and-text product-page modules. Claude drafts the
  module copy (headlines, alt text, series cross-sell blocks) in your brand voice;
  pair with the image specs from KDP's A+ help page.

## Common pitfalls

- **Never bulk-edit prose without a diff.** "Fix all the quotes in my manuscript"
  as a freehand edit invites silent text changes. The safe shape: script makes the
  change, Claude shows the diff, you approve. For judgment passes, have Claude
  write a *report* and apply fixes selectively.
- **Claude can't see the rendered book.** It verifies that pandoc ran, not that
  the EPUB looks right on a Kindle. Always open output in Kindle Previewer /
  Apple Books before upload. (The docx/pdf skills mitigate this by rendering pages
  to images — but final human review stands.)
- **Pandoc is a converter, not a typesetter.** Its EPUBs are clean and valid; its
  print PDFs are not Vellum/Atticus-grade interiors. Pandoc for ebook and
  interchange; a dedicated formatter for print interiors.
- **KDP strips what it doesn't support.** Links, `<h2>`, emojis, and review quotes
  in descriptions get stripped or rejected. Retailer rules drift and third-party
  guides contradict each other — check the current KDP help page when it matters.
- **Smart-quote scripts mangle leading apostrophes.** *'90s*, *'em*, *'Tis*.
  Demand the exceptions report.
- **Token cost:** scripted checks are free after creation; subagent typo sweeps
  across a 100k-word manuscript are among the most expensive things in this wiki.
  Run them once, late, on purpose.
- **Permission rules ≠ backups.** Deny rules stop Claude's editing tools; keep
  Time Machine/git/Dropbox running regardless. Versioning convention: never
  overwrite — `MyBook_full_v1.docx`, `_v2`, dated EPUB builds in `output/`, and
  `originals/` as the never-edited archive.

## Advanced

### A worked publishing-prep pipeline

```text
my-book/
├── .claude/
│   ├── settings.json          # deny rules: originals/, published/
│   ├── hooks/protect.sh       # PreToolUse belt-and-suspenders block
│   └── skills/
│       ├── release-checklist/SKILL.md
│       └── backmatter-update/SKILL.md
├── originals/                 # untouched final draft — Claude never writes here
├── manuscript/                # working chapter files (ch01.md ...)
├── front-matter/  back-matter/
├── metadata.yaml              # pandoc/EPUB metadata
├── series-metadata.yaml       # cross-book consistency source of truth
├── scripts/
│   ├── build-epub.sh  build-docx.sh
│   └── format-check.sh
├── output/                    # everything generated lands here, versioned
└── published/                 # what actually went to retailers — Claude never writes here
```

Protection is layered, per [hooks.md](../02-power-features/hooks.md) and
[settings-and-permissions.md](../01-claude-code-basics/settings-and-permissions.md):
deny rules (`"Edit(originals/**)"`, `"Edit(published/**)"`, `"Write(originals/**)"`,
`"Write(published/**)"`) catch the file tools; a `PreToolUse` hook matching
`Edit|Write|Bash` catches shell-based writes the rules might miss.

### The format-check script (concept)

One script, exit code 0/1, run on demand or wired as a hook before builds:

```bash
# scripts/format-check.sh — report-only, never modifies
# 1. scene breaks: anything matching break-ish patterns that isn't exactly "***"
# 2. straight quotes: lines containing " or ' after the smart-quote pass
# 3. doubles: "  " double spaces, repeated words ("\b(\w+) \1\b")
# 4. chapter headers: every file starts with "# Chapter N" pattern, N sequential
# 5. em-dash hygiene: " — " spaced dashes vs "—" per house style; count + density
# 6. dialogue candidates: ," and ." adjacent to closing quotes, for the judgment pass
# Output: file:line:issue, summary table, exit 1 if any blockers
```

Ask Claude to write it against *your* house style, then freeze it. Wire it as a
`PreToolUse` hook on your build script or just make `build-epub.sh` call it first
and refuse to build on blockers — deterministic enforcement, zero tokens.

### The release-checklist skill

A `release-checklist` skill (see [skills.md](../02-power-features/skills.md) for
anatomy) with `disable-model-invocation: true` so it runs only when *you* type
`/release-checklist`. The body is your launch list with each item tagged:

- `[AUTO]` — Claude does it: run format-check, build EPUB, run EPUBCheck, verify
  metadata against `series-metadata.yaml`, character-count the blurb HTML,
  regenerate back matter, page-count estimate.
- `[CHECK]` — Claude verifies and reports: links in back matter resolve (it can
  fetch them), ISBN assigned in the tracker, cover file present at expected specs.
- `[HUMAN]` — flagged, never attempted: visual proof in Kindle Previewer, order
  the physical proof copy, price decision, category final picks, the actual
  KDP upload, pressing **Publish**.

This is the honest division of labor: the **repetitive ~20% gets automated; the
judgment ~80% gets a checklist with your name on it.** The win isn't that Claude
publishes the book — it's that nothing mechanical is ever forgotten or done
inconsistently, and your attention is spent only where attention matters.

### MCP and Desktop hand-offs

- Keep the ISBN tracker or launch calendar in Notion/Airtable and let Claude Code
  read/update it via [MCP](../02-power-features/mcp.md) instead of a local file.
- Use Claude Code for the script-and-files pipeline; use Desktop/Cowork when the
  deliverable is itself an Office file (ISBN `.xlsx`, a styled submission `.docx`).
  Same skills and CLAUDE.md apply in the Desktop Code tab.

### Audiobook narration drafts via the ElevenLabs API

Claude can't speak, but it can run the pipeline around a text-to-speech service.
ElevenLabs has a real, official API (text-to-speech, plus sound effects and music),
so a `narrate-chapter` skill is the same shape as the EPUB pipeline above: a script
reads `manuscript/ch-NN.md`, strips formatting, splits at scene breaks, sends each
piece to the API, and writes `audio/ch-NN.mp3` — with Claude handling the
pre-processing judgment calls (expanding abbreviations, marking pronunciations,
flagging dialogue-heavy passages to re-listen to). Three cautions: the API is
**billed per character**, so price one chapter before a whole novel; keep your API
key in an environment variable, never in the skill file; and check your audiobook
retailer's current policy on AI narration before producing — this makes *drafts and
proofs*, the publish decision is yours. More multimedia rows (narrator auditions,
trailer audio):
[use-case-catalog.md → Multimedia](../04-reference/use-case-catalog.md#10-multimedia-audio--image-generation).

## Sources

- https://pandoc.org/epub.html — official pandoc EPUB guide: command syntax,
  metadata blocks, `--css`, `--epub-cover-image`, image embedding (accessed 2026-06-10)
- https://kdp.amazon.com/en_US/help/topic/G201189630 — KDP "Write a Book
  Description": 4,000-char limit including tags, supported HTML table
  (`<br> <p> <b> <em> <i> <u> <h4>–<h6> <ol> <ul> <li>`), prohibited content
  (accessed 2026-06-10)
- https://kdp.amazon.com/en_US/help/topic/G201953020 — KDP "Create a Paperback
  Cover": spine width formula, spine-text clearance (accessed 2026-06-10, via search
  summary)
- https://elevenlabs.io/docs — official ElevenLabs API docs: text-to-speech,
  sound effects, music APIs (accessed 2026-06-10)
- https://github.com/anthropics/skills — Anthropic's document skills
  (docx/pdf/xlsx/pptx) referenced via [skills.md](../02-power-features/skills.md)
  (accessed 2026-06-10)
- KDP limits (3 categories / 7 keywords per format) and Vellum's Mac-only status
  (macOS 13+, no Windows version announced) — corroborated across multiple current
  third-party sources (Kindlepreneur, Reedsy, 2026 guides) via web search 2026-06-10.
  ⚠️ Unverified directly on a single official page: the 3-category limit and the
  79-page spine-text minimum come from KDP help content surfaced through search
  summaries, not a direct fetch — both are stable, widely-documented KDP rules, but
  confirm in your KDP dashboard at upload time.
- ⚠️ Unverified: words-per-page estimates (~250–300 at common trim sizes) are
  industry rules of thumb, not a KDP spec — always confirm with the formatted PDF.
