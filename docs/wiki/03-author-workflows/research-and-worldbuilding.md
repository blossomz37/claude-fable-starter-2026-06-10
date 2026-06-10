# Research & Worldbuilding: From Market Maps to World Bibles

> **In plain words:** Claude can do the research legwork that surrounds a book —
> figuring out what readers of your subgenre expect, studying comparable titles,
> digging up period detail, and keeping a living world bible and timeline as you
> draft. This doc shows the workflows, with prompts you can copy. One rule runs
> through all of it: Claude's research is a *draft of the truth* until you verify
> it — treat findings like notes from an enthusiastic intern, not like canon.

## What it is

Author research splits into three jobs, and Claude helps with all of them:

- **Market research** — what does the subgenre promise readers, who are the comp
  titles (comparable books), and where is the gap your book can fill?
- **Topical research** — period detail, technical accuracy, "how long does it
  take to ride from York to Edinburgh," "what does a hospital network breach
  actually look like."
- **Worldbuilding records** — your own invented facts (locations, factions,
  magic rules, chronology), captured as files Claude can read and update so book
  4 doesn't contradict book 1.

The first two pull facts *in* from the world; the third keeps your invented
facts *straight*. Claude Code suits all three because it works in your project
folder: research lands as Markdown files next to your manuscript, and your
world bible is just files Claude reads before drafting — the same idea as
[CLAUDE.md and memory](../01-claude-code-basics/claude-md-and-memory.md),
scaled up.

## Why authors care

- **Write to market without guessing.** A researched trope-and-expectations map
  beats "I think readers like enemies-to-lovers."
- **Comp research in an afternoon, not a month.** Subagents can each take one
  comp title and report back in parallel.
- **Continuity stops leaking.** A world bible Claude updates after every chapter
  catches "wait, was the harbor east or west of the keep?" before readers do.
- **Findings become files.** Research saved as Markdown is reusable in every
  future session — and portable to Obsidian, Notion, or your co-author.

## Getting started

A first win in about ten minutes — a subgenre snapshot:

1. Make a project folder and start Claude Code in it
   (`mkdir ~/Documents/dragon-academy && cd ~/Documents/dragon-academy && claude`).
2. Paste this:

   ```text
   I'm planning a dragon-rider academy fantasy with romance elements.
   Research the current state of this subgenre on the web:
   1. 8-10 recent successful titles closest to that description.
   2. One line each: premise + what readers seem to love about it.
   3. The tropes that appear in most of them (the "expected" set).
   4. Anything all of them do that I'd break at my peril.
   Cite a source URL per claim and flag claims resting on a single
   source. Save the result as research/subgenre-snapshot.md.
   ```

3. Read the file it writes. Spot-check two or three claims yourself (open the
   books' store pages). Note the two habits baked into the prompt — **ask for
   sources** and **flag single-source claims**. Make them reflexes.

## Author use cases

### 1. The three-phase genre research pattern

The reliable shape for full market research is three phases, each feeding the
next. Run them as three separate prompts (or sessions) so each output gets your
review before it feeds forward.

**Phase 1 — define the subgenre envelope.** Start from seed titles, not
labels. "Romantasy" is too broad; *the cluster of books readers buy together*
is the real genre.

```text
Seed titles: [3-5 books that feel like the book I want to write].
Research what these have in common and what cluster of books readers
buy alongside them (also-boughts, "readers also enjoyed" lists,
shared subgenre tags on store pages and Goodreads). Define the
envelope: what must a book in this cluster deliver? Output
research/01-envelope.md with the cluster list and shared DNA, cited.
```

**Phase 2 — map reader expectations.** Go deep on what readers expect, love,
and punish:

```text
Using research/01-envelope.md, build a market report: core tropes
(near-mandatory), common tropes (expected), fresh tropes (recent
breakout differentiators); reader expectations for heat level, pacing,
POV, ending type, length; what reviews praise and complain about most
across the cluster; positioning gaps readers are asking to have
filled. Cite sources; flag single-source claims.
Save as research/02-market-report.md.
```

**Phase 3 — convert findings into a writing style guide.** The step most
people skip: turn market facts into *drafting rules* Claude follows later.

```text
From research/02-market-report.md, write a style guide for drafting
this book: voice and tense norms for the cluster, chapter length and
pacing expectations, trope checklist (using / subverting / skipping),
content expectations, and 10 concrete prose-level dos and don'ts.
Save as research/03-style-guide.md.
```

Reference that style guide from your CLAUDE.md (`@research/03-style-guide.md`)
and every drafting session inherits it. This whole pipeline can be packaged as
a [skill](../02-power-features/skills.md) — Carlo's installed `genre-research`
skill is exactly this three-phase pattern, formalized.

### 2. Comp-title analysis with subagent fan-out

Comp research is "breadth-first" — many independent titles, same questions —
which is precisely what [subagents](../02-power-features/subagents-and-orchestration.md)
are for. One agent per comp, in parallel:

```text
Use subagents, one per comp title, for: Fourth Wing, Divine Rivals,
and Powerless. Each agent researches its title on the web and writes
research/comps/<title>.md covering:
1. Blurb structure: hook, what's promised, what's withheld, final line type
2. Trope list, and which tropes the marketing leads with
3. Review mining: the exact phrases readers use when praising it, and
   the top 3 complaints in critical reviews
4. Where it sits in the cluster — what it does that neighbors don't
Cite sources per claim. When all agents finish, read every comps file and
write research/positioning-memo.md: shared promises across comps, the
reader language I should echo in my own blurb, and the gaps none of them
fill that my premise could.
```

The review-mining step matters most: readers' own words ("slow-burn done
right," "the found family made me cry") are blurb and ad copy you can't invent.
Packaged versions exist as skills (`book-analyst` for per-title deep dives,
`book-cover-trends` for the visual side) — but the plain prompt above needs
nothing installed. Cost note: multi-agent fan-out uses roughly 15× the tokens
of a simple chat — worth it for five comps, overkill for one.

### 3. Topical research for fiction

Period detail and technical accuracy respond well to role-framed prompts:

```text
I'm writing an 1890s Boston scene where a character is treated for a
laudanum overdose at home. Research: what would a physician of that
decade actually do, what equipment and language would they use, and
what would the family be doing in the room? Distinguish clearly
between well-documented facts and your inference. Cite sources.
Save to research/topics/1890s-overdose-treatment.md.
```

Two notes specific to this kind of research:

- **Sensory texture beats encyclopedia facts.** Ask explicitly: "what would
  the scene smell, sound, and feel like?" — that's what makes research visible
  on the page.
- **Deep technical questions may switch models — that's fine.** Fable 5 runs
  safety classifiers on every request; detailed cybersecurity or
  biology/chemistry questions (your hacker thriller, your engineered-plague
  sci-fi) can trip them even when entirely legitimate. The answer is then
  handled by Opus 4.8 instead, clearly labeled. Expected, harmless, still a
  strong answer — see the
  [Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md).

### 4. A worldbuilding wiki that maintains itself

Your world bible should be linked Markdown files in the project, not one giant
document:

```text
world/
├── INDEX.md            # one-line summary + link per entry
├── locations/          # one file per place
├── factions/           # one file per faction, with goals + relationships
├── people/             # recurring characters
├── rules/              # magic/tech systems — costs, limits, exceptions
└── timeline.md         # dated events (see use case 5)
```

Bootstrap it from an existing draft in one prompt:

```text
Read every chapter in manuscript/. Build a world bible under world/
using the structure above: one file per location, faction, and named
character, each recording only facts established ON THE PAGE, with a
chapter citation for each fact. Link entries to each other with
relative Markdown links. Write world/INDEX.md last.
```

Then keep it current with an updater step after each chapter — a prompt
("update world/ with any new facts from chapter 14, cite the chapter") or,
better, a small skill (`/bible-update chapter-14`) so the procedure is
identical every time; a [hook](../02-power-features/hooks.md) can nudge you
whenever a chapter file changes. Because the wiki is plain Markdown with
links, **Obsidian is its natural home**: open the project folder as a vault
and you get a clickable graph of your world for free, while Claude keeps
editing the same files (vault-aware search options in
[mcp.md](../02-power-features/mcp.md)).

### 5. Timelines, travel time, and date math

Chronology errors are the most common continuity bug, and the most mechanical
to catch. Extract a timeline from the draft:

```text
Read manuscript/ in order. Extract every dated or relatively-dated event
("three days later") into world/timeline.csv with columns:
Title, Start Date, Duration, Participants, Location, Chapter.
Where the text gives only relative time, compute the date from the
nearest anchor and mark the cell with an asterisk. Then list every
chronological impossibility you found: overlapping presences,
travel times that don't work, characters aging inconsistently.
```

That CSV is import-ready for **Aeon Timeline** (File → Import CSV or TSV; Title
and Start Date are the only mandatory columns) — your drafted chronology
becomes a visual timeline in one import. The `aeon-csv-architect` skill is the
packaged version. For travel-time checks, give Claude the rules once
("horseback ≈ 30-40 miles/day on roads; map distances are in
world/locations/distances.md") and ask it to audit every journey against them.

### 6. Long-horizon deep research with Fable 5

For big questions — "map the entire cozy-fantasy market since 2023" or "every
documented detail of the 1900 Galveston hurricane relevant to a survivor POV" —
Fable 5's stamina changes what's feasible: it can plan a multi-stage research
run, delegate to subagents, keep working notes, and check its own output along
the way. What makes long runs *trustworthy* is **adversarial verification** —
a second agent whose only job is to attack the first one's claims:

```text
Stage 1: research [question] across multiple independent sources and
write research/report-draft.md with an inline citation for every claim.
Stage 2: spawn a skeptic subagent. Its only job: try to knock down the
draft. Check each citation actually supports the claim, hunt for
contradicting sources, and flag anything resting on one source or on
no source. It writes research/verification.md.
Stage 3: revise the draft using the verification file. Mark surviving
single-source claims as "unconfirmed." Final output: research/report.md.
```

This is the fan-out/verify/synthesize shape (full orchestration prompt in
[Advanced](#advanced)); Carlo's `deep-research` skill packages it. Long runs
are real token usage — see the cost notes in
[subagents-and-orchestration.md](../02-power-features/subagents-and-orchestration.md).

## Common pitfalls

- **Hallucination is the occupational hazard.** Claude can produce confident,
  specific, wrong facts — invented book titles, false period details,
  misremembered review quotes. Web-grounded research with citations is much
  safer than answers from memory, but a citation can still be misread. Always
  ask for sources; always spot-check what matters.
- **Distrust single-source claims.** Make "flag anything resting on one source"
  a standard line in research prompts. One blog post is a lead, not a fact.
- **The verify-before-canon rule.** Nothing moves from `research/` into your
  world bible, style guide, or manuscript until *you* have checked it.
  Research files are drafts of the truth; canon files are commitments.
- **Keep research and canon physically separate.** `research/` (what the world
  says — cited, provisional) vs `world/` (what *your* story says — established,
  chapter-cited). If they mix, unverified findings leak into drafting context
  and Claude treats them as true.
- **Review mining has a selection bias.** One-star reviews overrepresent angry
  readers; five-star reviews overrepresent superfans. Mine both, and weight
  recurring complaints over loud one-offs.
- **Market research goes stale.** Date every research file and put an "as of"
  in the header; an 18-month-old trope map can mislead a launch today.
- **Cost.** Multi-agent fan-outs multiply token usage (~15× a normal chat per
  Anthropic's engineering data), and Fable 5 burns usage faster than Sonnet.
  Fan out for genuine breadth; a single question needs a single conversation.

## Advanced

### A worked research project layout

```text
my-novel/
├── CLAUDE.md                    # imports 03-style-guide.md; states the
│                                #   verify-before-canon rule explicitly
├── manuscript/
├── world/                       # CANON — established, chapter-cited
│   ├── INDEX.md
│   ├── locations/ factions/ people/ rules/
│   └── timeline.csv
└── research/                    # PROVISIONAL — cited, dated, unverified
    ├── 01-envelope.md
    ├── 02-market-report.md
    ├── 03-style-guide.md        # promoted to canon-adjacent once reviewed
    ├── comps/                   # one file per comp title
    ├── topics/                  # one file per factual question
    └── sources/                 # source notes (format below)
```

### Source-notes format

One file per substantial source keeps citations auditable:

```markdown
# Source: "The State of Romantasy 2026" — Publishers Weekly
- URL: https://...
- Accessed: 2026-06-10
- Type: trade press (secondary)
- Reliability: high for sales data, medium for trend predictions
## Claims used
- [C1] Subgenre grew 40% YoY in print → used in 02-market-report.md §2
- [C2] "Readers report fatigue with..." → SINGLE SOURCE, unconfirmed
```

The `[C1]` IDs let a verification agent trace any report claim back to its
source mechanically.

### A deep-research orchestration prompt

The full fan-out/verify/synthesize template, for a long Fable 5 run:

```text
Research project: [question]. Work in research/.
PLAN: Break the question into 3-6 independent sub-questions; write
research/PLAN.md and keep it updated as you work.
FAN-OUT: One subagent per sub-question. Each searches the web across
multiple independent sources, writes research/findings/<topic>.md with
an inline URL citation per claim, plus a source note per major source
in research/sources/. Agents share nothing except these files.
VERIFY: A skeptic subagent reads all findings. For each claim: does
the cited source actually say this? Does any source contradict it? Is
it single-sourced? Output research/verification.md labeling every
claim CONFIRMED / SINGLE-SOURCE / CONTRADICTED / UNSUPPORTED.
SYNTHESIZE: Write research/report.md from confirmed material, with an
"Unconfirmed leads" section for single-source items and a "Disputed"
section where sources disagree. Every claim keeps its citation.
Nothing from this report enters world/ — that promotion is mine.
```

Save it as a project skill with `arguments: [question]` and the whole pipeline
becomes `/deep-research "..."` — see [skills.md](../02-power-features/skills.md).

### MCP connections for research vaults

If your research and worldbuilding live outside the project folder, connect
them instead of copying — full setup in [mcp.md](../02-power-features/mcp.md):

- **Obsidian vault:** simplest route — point Claude Code at the vault folder
  directly (`/add-dir ~/Vaults/worldbuilding`) or via the filesystem MCP
  server, since a vault is just Markdown. For vault-aware operations (search
  by tag, append to a note), use the community Local REST API plugin +
  Obsidian MCP server route described in mcp.md.
- **Notion story bible:** `claude mcp add --transport http notion
  https://mcp.notion.com/mcp`, authenticate via `/mcp`, then "fetch the
  faction page from my story bible before drafting this scene." Claude can
  also write research summaries back to Notion pages.
- A custom research subagent can scope these servers to itself via its
  `mcpServers` frontmatter field, keeping connector overhead out of your
  drafting sessions.

### Custom research agents worth defining

Two `.claude/agents/` definitions that earn their keep (file format in
[subagents-and-orchestration.md](../02-power-features/subagents-and-orchestration.md)):
**comp-researcher** (web research tools only, encoding use case 2's four
questions so every comp gets identical treatment) and **claim-skeptic**
(read-only plus web search; prompt: "You verify, you never generate. For each
claim, find the cited source and judge whether it supports the claim. Hunt for
contradictions. You succeed by finding errors."). Keeping the skeptic a
*separate agent* matters: a fresh context has no investment in the draft
being right.

## Sources

- Repo wiki docs synthesized: [subagents-and-orchestration.md](../02-power-features/subagents-and-orchestration.md),
  [mcp.md](../02-power-features/mcp.md), [skills.md](../02-power-features/skills.md),
  [hooks.md](../02-power-features/hooks.md),
  [claude-md-and-memory.md](../01-claude-code-basics/claude-md-and-memory.md),
  [fable-5-model-guide.md](../../fable-documentation/fable-5-model-guide.md) —
  all themselves verified against official docs 2026-06-10.
- https://help.timeline.app/article/235-importing-csv-files — Aeon Timeline 3
  CSV import: File → Import CSV or TSV, Title + Start Date mandatory, column
  mapping (accessed 2026-06-10).
- https://www.anthropic.com/engineering/multi-agent-research-system — fan-out
  research pattern and ~15× token multiplier for multi-agent systems (accessed
  2026-06-10, via subagents doc).
- Fable 5 safety-classifier fallback to Opus 4.8 for cybersecurity/biology
  queries: see sources in the [Fable 5 model guide](../../fable-documentation/fable-5-model-guide.md)
  (Anthropic launch post + support article, accessed 2026-06-10).
- ⚠️ Unverified: the three-phase genre research pattern, research/ folder
  conventions, source-notes format, and prompt templates are craft synthesis
  (drawing on Carlo's `genre-research`, `book-analyst`, `aeon-csv-architect`,
  and `deep-research` skill ecosystem), not claims from official documentation.
- ⚠️ Unverified: horseback travel rate (~30-40 miles/day) is a common
  historical-fiction rule of thumb presented as an *example* of giving Claude
  rules to audit against, not as a researched fact.
