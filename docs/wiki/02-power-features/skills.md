# Skills: Teach Claude Your Procedures Once

> **In plain words:** A skill is a reusable instruction packet — a folder with a
> `SKILL.md` file inside — that Claude loads only when it's needed. Think of it as
> handing your assistant a laminated procedure card: "Here's exactly how I write
> blurbs." Write it once, and Claude follows it every time, in every project,
> without you re-pasting the instructions.

## What it is

If you've ever pasted the same blurb checklist, style guide, or revision procedure
into chat for the tenth time, skills are the fix. A skill is a small folder
containing a `SKILL.md` file (a plain text file with instructions), plus any
supporting material — templates, examples, even scripts.

Claude sees a one-line description of every installed skill at all times, like a
table of contents. The full instructions load only when the skill is actually
relevant. That's called **progressive disclosure**, and it means you can install
dozens of skills without cluttering Claude's working memory (its "context").

How skills differ from the other ways of teaching Claude:

| Feature | What it's for | Author analogy |
| :--- | :--- | :--- |
| **CLAUDE.md memory** | Facts always in play ("my genre is cozy mystery, never use em-dashes") | The sticky note on the monitor |
| **Skill** | A procedure loaded on demand ("here's my 9-step blurb process") | The laminated procedure card in a drawer |
| **Slash command** | A skill you trigger by typing `/name` — in Claude Code, custom commands have been merged into skills; both create `/name` | The button you press |
| **Subagent** | A separate assistant with its own working memory for big delegated jobs | The freelance editor you hand a chapter to |

The official rule of thumb from Anthropic's docs: create a skill "when you keep
pasting the same instructions, checklist, or multi-step procedure into chat, or
when a section of CLAUDE.md has grown into a procedure rather than a fact."
Unlike CLAUDE.md content, a skill's body costs almost nothing until it's used.

Skills follow the [Agent Skills open standard](https://agentskills.io) (published
December 2025), so the same skill folder works across Claude Code, claude.ai, the
API, and a growing list of non-Anthropic tools.

## Why authors care

- **Stop re-explaining your craft.** Your blurb formula, synopsis structure, and
  comma-splice rules live in files, not in your memory of what you typed last week.
- **Consistency across a series.** A "series-bible-updater" skill applies the same
  procedure to book 1 and book 7.
- **Share your process.** A skill folder is just files — zip it for your co-author,
  commit it to your project, or publish it as a plugin for your students.
- **Cheap until used.** Each installed skill costs roughly 100 tokens of overhead
  (about a sentence); the full instructions load only when triggered.
- **Two trigger modes.** Claude can invoke a skill automatically when your request
  matches its description, or you can fire it deliberately by typing `/skill-name`.

## Getting started

This builds a working **blurb-writer** skill in about five minutes. macOS shown;
on Windows, the personal skills folder is `C:\Users\<you>\.claude\skills\`.

1. **Create the skill folder.** Open Terminal and run:

   ```bash
   mkdir -p ~/.claude/skills/blurb-writer
   ```

   `~/.claude/skills/` is your *personal* skills folder — skills here work in
   every project. (A `.claude/skills/` folder inside a manuscript project works
   only for that project.)

2. **Create the SKILL.md file.** Save the following as
   `~/.claude/skills/blurb-writer/SKILL.md` (any text editor works — or just ask
   Claude Code to create it for you):

   ```yaml
   ---
   name: blurb-writer
   description: Writes back-cover blurbs for novels following a hook-stakes-twist structure. Use when the user asks for a blurb, back-cover copy, Amazon book description, or jacket copy.
   ---

   # Blurb Writer

   Write a back-cover blurb using this structure:

   1. **Hook line** — one sentence, the protagonist's ordinary world cracked open.
   2. **Escalation paragraph** — 2-3 sentences raising stakes. Name the
      protagonist; never name the antagonist.
   3. **Twist-tease** — one sentence implying the impossible choice. No spoilers
      past the 40% mark of the book.
   4. **Tagline** — italicized, under 12 words.

   Rules:
   - 150-200 words total.
   - Present tense, third person.
   - End on a question or an ultimatum, never a summary.
   - Match the genre's voice: ask which genre if it isn't obvious from context.
   - Produce 2 variants and label them A and B.
   ```

   The part between the `---` markers is **YAML frontmatter** — metadata.
   The `description` is the trigger: Claude reads it to decide when to load the
   skill. Everything below is what Claude actually follows once it loads.

3. **Test it.** Start Claude Code (`claude`) and try both invocation paths:
   - **Automatic:** type "I need back-cover copy for my space-opera romance" —
     the request matches the description, so Claude loads the skill.
   - **Explicit:** type `/blurb-writer` (the folder name becomes the command).

4. **Iterate.** Edit the file and test again — Claude Code watches skill folders,
   so changes to `SKILL.md` take effect in the current session without restarting.
   If the skill didn't fire automatically, add the words you actually said to the
   `description` (see [Common pitfalls](#common-pitfalls)).

## Author use cases

1. **Style-guide enforcement.** Put your house style (banned words, dialogue-tag
   rules, comma policy) in a `style-guide` skill. Add `user-invocable: false` so
   it's background knowledge Claude applies when editing, not a command you type.
2. **Synopsis generator.** A `synopsis` skill encoding your agent-submission
   format: 1-page and 2-page variants, present tense, spoilers required, named
   characters capped at five. Bundle a `template.md` Claude fills in.
3. **Query-letter formatter.** Frontmatter `arguments: [title, wordcount, genre]`
   lets you run `/query-letter "Saltwater Crown" 92000 fantasy` and get a properly
   structured letter with personalization slots left blank.
4. **Series-bible updater.** After drafting a chapter: `/bible-update chapter-12`.
   The skill instructs Claude to extract new characters, settings, and timeline
   facts and append them to your bible files. Pair with a hook for automatic
   nudges — see [hooks.md](hooks.md).
5. **ProWritingAid-style audit.** A `prose-audit` skill bundling scripts that
   count adverbs, filter words, and sentence-length distribution, plus
   instructions for turning the numbers into a revision plan. Scripts run without
   their code ever entering context — only the output does.
6. **Chapter audit before "done".** A `chapter-audit` checklist skill: POV slips,
   continuity against the bible, scene-goal check, echo words. Set
   `disable-model-invocation: true` so it runs only when *you* decide a chapter
   is ready, never mid-draft.
7. **ARC/launch packet.** One skill that produces the back-matter page, ARC team
   email, and three social captions from a finished manuscript, using bundled
   example files so the voice stays consistent book to book.

For heavyweight multi-chapter workflows, a [subagent](subagents-and-orchestration.md)
may fit better; skills can also *run inside* subagents (see Advanced).

## Common pitfalls

- **Vague descriptions don't trigger.** `description: Helps with books` will
  never fire. State *what it does* and *when to use it*, in third person, with
  the words you'd naturally say: "...Use when the user asks for a blurb, back-cover
  copy, or Amazon book description."
- **The body loads into context and stays there.** Once invoked, the skill's text
  remains for the rest of the session and costs tokens on every turn. Keep
  `SKILL.md` lean (official guidance: under 500 lines; move reference material to
  separate files in the folder).
- **Skills don't sync across surfaces.** A skill in `~/.claude/skills/` exists
  only on that computer. claude.ai uploads, API uploads, and Claude Code folders
  are three separate copies you maintain separately (verified current as of
  2026-06-10).
- **Treat third-party skills like software.** A skill can instruct Claude to run
  code and use tools. Anthropic's docs say to audit skills from unknown sources
  before installing — check for odd network calls or instructions that don't
  match the stated purpose. Project skills checked into a shared repo can grant
  themselves tool permissions once you trust the workspace, so review them first.
- **Too many skills shrinks descriptions.** With a large library, Claude Code
  trims descriptions to fit a budget, which can strip your trigger words. Run
  `/doctor` to check; least-used skills lose their text first.
- **Cost note:** skills don't cost anything extra to install; they spend your
  normal token usage when invoked. A skill that injects a whole manuscript via a
  shell command can be expensive — inject only what the task needs.

## Advanced

### Where skills live (Claude Code, June 2026)

| Location | Path | Applies to |
| :--- | :--- | :--- |
| Enterprise | managed settings (admin-deployed) | whole organization |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | all your projects |
| Project | `.claude/skills/<skill-name>/SKILL.md` | that project only |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | wherever the plugin is enabled |

Name conflicts: enterprise overrides personal, personal overrides project. Plugin
skills are namespaced (`/plugin-name:skill-name`) so they can't conflict. Legacy
`.claude/commands/*.md` files still work and accept the same frontmatter; if a
command and a skill share a name, the skill wins. Project skills are also
discovered from parent directories up to the repo root and on demand from nested
`.claude/skills/` folders (monorepo support), and from directories added with
`--add-dir` / `/add-dir`. Live change detection covers `SKILL.md` edits
mid-session; a brand-new top-level skills directory requires a restart.

### Skill anatomy

```text
chapter-audit/
├── SKILL.md           # required entry point
├── checklist.md       # reference, loaded only if needed
├── examples/
│   └── sample-report.md
└── scripts/
    └── echo_words.py  # executed via bash; code never enters context
```

Reference supporting files *from* `SKILL.md` ("For the full checklist, see
`[checklist.md](checklist.md)`") and keep references one level deep — Claude may
only preview deeply nested files. Three loading levels: frontmatter metadata
(~100 tokens, always loaded), `SKILL.md` body (loads on trigger), bundled files
(load or execute only as needed).

### Frontmatter reference (Claude Code)

All fields optional; only `description` is recommended. Verified against
code.claude.com docs, 2026-06-10:

| Field | What it does |
| :--- | :--- |
| `name` | Display name in listings; defaults to the directory name. The *command* name comes from the directory name, not this field (except a plugin-root `SKILL.md`). |
| `description` | The trigger. Combined `description` + `when_to_use` text is truncated at 1,536 characters in the listing — put the key use case first. |
| `when_to_use` | Extra trigger context (phrases, example requests), appended to the description. |
| `argument-hint` | Autocomplete hint, e.g. `[chapter-file] [format]`. |
| `arguments` | Named positional args for `$name` substitution, e.g. `arguments: [title, genre]`. |
| `disable-model-invocation` | `true` = only you can invoke it (`/name`). Use for side-effect workflows: commits, publishing, sending. |
| `user-invocable` | `false` = hidden from the `/` menu; Claude-only background knowledge. |
| `allowed-tools` | Tools pre-approved while the skill is active, e.g. `Bash(git add *) Bash(git commit *)`. Grants permission; doesn't restrict other tools. |
| `disallowed-tools` | Tools removed from the pool while active; clears on your next message. |
| `model` / `effort` | Override model or effort level for the rest of the turn (e.g. drop to a cheaper model for a mechanical formatting skill). |
| `context: fork` | Run the skill in an isolated subagent; the skill body becomes the subagent's prompt. |
| `agent` | Which subagent type executes a forked skill: `Explore`, `Plan`, `general-purpose`, or any custom agent from `.claude/agents/`. |
| `hooks` | Hooks scoped to this skill's lifecycle — see [hooks.md](hooks.md). |
| `paths` | Glob patterns; auto-trigger only when working on matching files (e.g. `paths: chapters/*.md`). |
| `shell` | `bash` (default) or `powershell` for inline command injection on Windows. |

The open standard (and the API/claude.ai surfaces) validate `name` (max 64 chars,
lowercase/numbers/hyphens, no "anthropic"/"claude") and `description` (max 1,024
chars). Fields like `context`, `agent`, and `hooks` are Claude Code extensions —
don't expect them to work on claude.ai.

### Dynamic context and string substitution

- `` !`command` `` in the body runs a shell command *before* Claude sees the
  skill, replacing the line with its output. Example for a chapter-audit skill:
  `` !`wc -w chapters/*.md` `` injects live word counts. Multi-line blocks use a
  fenced ```` ```! ```` code block. Disable with `"disableSkillShellExecution": true`.
- Substitutions: `$ARGUMENTS` (everything after the command), `$0`/`$1`/`$ARGUMENTS[N]`
  (positional), `$name` (declared in `arguments:`), `${CLAUDE_SKILL_DIR}` (the
  skill's own folder — use it for bundled script paths), `${CLAUDE_SESSION_ID}`,
  `${CLAUDE_EFFORT}`.

### Skill lifecycle and compaction

Invoked skill content enters the conversation once and is not re-read on later
turns. During auto-compaction, the most recent invocation of each skill is
re-attached (first 5,000 tokens each, 25,000-token combined budget, newest
first) — older skills can drop out entirely. If a skill "stops working" late in
a long session, re-invoke it, or enforce the behavior with a hook instead.

### Skills + subagents, skills + hooks

- `context: fork` + `agent: Explore` is ideal for read-only research skills (a
  manuscript-wide continuity sweep) that shouldn't pollute your drafting
  conversation. Explore/Plan agents skip CLAUDE.md to stay lean.
- The inverse: a custom subagent can *preload* skills via its `skills` field, so
  your "line-editor" agent always carries the style-guide skill.
- The `hooks` frontmatter field scopes hooks to the skill's lifecycle — e.g. a
  formatting skill that always runs a validator after it edits files.

### Plugins, marketplaces, and the ecosystem

- Anthropic's official repo: [github.com/anthropics/skills](https://github.com/anthropics/skills)
  (~149k stars as of June 2026) — the Agent Skills spec, a skill template, example
  skills, the `skill-creator` skill (a skill that helps you write skills), and the
  source-available document skills (`docx`, `pdf`, `pptx`, `xlsx`). Install in
  Claude Code: `/plugin marketplace add anthropics/skills`, then
  `/plugin install example-skills@anthropic-agent-skills`.
- Anthropic also lists a directory of partner-built skills (Atlassian, Figma,
  Canva, Stripe, Notion, Zapier — announced December 2025) plus enterprise
  management tools. Community marketplaces exist but are unvetted — audit first.
- Any skill folder can become a plugin by adding `.claude-plugin/plugin.json`,
  letting it bundle agents, hooks, and MCP servers alongside the skill.

### Skills across surfaces (verified 2026-06-10)

| Surface | Pre-built skills | Custom skills |
| :--- | :--- | :--- |
| Claude Code | bundled skills (`/code-review`, `/debug`, etc.) | filesystem folders; full network access |
| claude.ai / Desktop | document skills work behind the scenes | upload as .zip via **Settings > Features** (Pro/Max/Team/Enterprise, code execution enabled); per-user, not org-shared |
| Claude API | `pptx`, `xlsx`, `docx`, `pdf` via `skill_id` in the `container` param | upload via `/v1/skills`; workspace-wide; requires beta headers (`skills-2025-10-02`, `code-execution-2025-08-25`, `files-api-2025-04-14`); no network access at runtime |

### Debugging a skill that won't trigger

1. Ask Claude "What skills are available?" — confirm it's listed.
2. Rewrite the `description` in third person with the literal words you say
   ("blurb", "back-cover copy"), what + when.
3. Check it isn't set `disable-model-invocation: true`, denied by a
   `Skill(name)` permission rule, or set to `"off"`/`"name-only"` in
   `skillOverrides` (the `/skills` menu writes these states).
4. Run `/doctor` to see whether the description budget is overflowing
   (raise `skillListingBudgetFraction` or set noisy skills to `"name-only"`).
5. Fires too *often*? Make the description more specific or add
   `disable-model-invocation: true`.
6. Anthropic's recommended authoring loop: have one Claude help write the skill,
   test it with a fresh Claude on real tasks, bring failures back, refine.
   Test with every model you'll use — Fable 5 needs less hand-holding than
   smaller models, so a skill tuned only on Fable 5 may underspecify for Haiku.

## Sources

- https://code.claude.com/docs/en/skills — Claude Code skills reference (accessed 2026-06-10)
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview — Agent Skills overview, surfaces, API details (accessed 2026-06-10)
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices — authoring best practices (accessed 2026-06-10)
- https://github.com/anthropics/skills — official skills repo, spec, marketplace install commands (accessed 2026-06-10)
- https://claude.com/blog/skills — launch announcement, 2025-10-16 (redirect from anthropic.com/news/skills; accessed 2026-06-10)
- https://agentskills.io — Agent Skills open standard (referenced by official docs; accessed 2026-06-10)
- ⚠️ Unverified: the December 2025 open-standard/partner-directory announcement details come from a web-search summary (SiliconANGLE, VentureBeat coverage of Anthropic's announcement), not fetched directly from an Anthropic page.
