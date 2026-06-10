# Settings and Permissions: Keeping Your Manuscript Safe

> **In plain words:** Claude Code asks before it changes your files or runs
> commands — those pop-up questions are the permission system. You can tune it:
> let Claude read everything freely, make certain folders untouchable, and stop
> approving the same harmless action twenty times a day. Settings live in small
> text files you mostly never need to open by hand.

## What it is

When Claude wants to *do* something — edit chapter 12, create a folder, run a
word-count command — Claude Code pauses and asks you first. Reading files generally
doesn't prompt; changing things does. Think of it as a new assistant on day one:
they can read the manuscript all they like, but they ask before marking it up.

Three layers control this:

- **Permission prompts** — the live yes/no questions, with a "yes, don't ask again"
  option that remembers your answer.
- **Permission modes** — overall postures, from cautious to hands-off, switched
  with a keystroke.
- **Permission rules** — written allow/ask/deny lists in settings files, for
  decisions you want made once and enforced forever ("never edit `originals/`").

Unlike instructions in [CLAUDE.md](claude-md-and-memory.md), permission rules are
**enforced by the app itself** — Claude cannot talk its way past a deny rule.

## Why authors care

- **Your manuscript is irreplaceable.** A deny rule on your originals folder is a
  guarantee, not a request.
- **Fewer interruptions.** Approve "word counts" once as a rule and stop clicking
  yes every session.
- **Plan mode = brainstorming-only.** Claude can read and discuss your whole book
  while being physically unable to change a word — perfect for developmental
  feedback you want to review before any edits.
- **It travels with the project.** Rules saved to the project are there next
  session, next book, next collaborator.

## Getting started

1. **Meet the prompt.** Ask Claude to "fix the typo in chapter-03.md." You'll see
   the proposed change and options like **Yes**, **Yes, don't ask again** (for this
   kind of action), and **No** — where you can also tell Claude what to do instead.

2. **Cycle modes with `Shift+Tab`.** The current mode shows near the input box:

   | Mode | What it means for you |
   |---|---|
   | `default` | Asks on first use of each tool/command. The safe everyday setting. |
   | `acceptEdits` | Auto-approves file edits (and basic file commands like `mkdir`, `mv`, `cp`) inside your project folder. Use once you trust the session — e.g., applying an agreed list of line edits. |
   | `plan` | **Plan mode.** Claude reads and analyzes but cannot edit files. Brainstorming, outlining, critique. Enter it any time with `/plan`. |
   | `bypassPermissions` | No prompts at all (the "yolo" mode). Dangerous — see pitfalls. |

   (Two more exist: `auto`, a research-preview mode with background safety checks,
   and `dontAsk`, which auto-denies anything not pre-approved.)

3. **Open the rules screen.** Type `/permissions` to see every allow/ask/deny rule
   and which file it comes from, and to add or remove rules without editing JSON.

4. **Protect your originals.** Have Claude do it for you:

   ```text
   Add permission rules to this project's settings: deny all edits to
   originals/ and deny edits to series-bible.md. Allow reads of everything.
   ```

   Then confirm in `/permissions`. (The `/fewer-permission-prompts` built-in skill
   can also scan your history and propose a sensible allowlist.)

## A safe starter setup for a manuscript folder

This goes in `.claude/settings.json` inside your book folder (Claude can create it
for you — see Advanced for what each line means):

```json
{
  "permissions": {
    "deny": [
      "Edit(originals/**)",
      "Edit(series-bible.md)",
      "Bash(rm *)"
    ],
    "ask": [
      "Edit(chapters/**)"
    ],
    "allow": [
      "Read",
      "Edit(drafts/**)",
      "Edit(notes/**)"
    ]
  }
}
```

Plain-English translation: never touch `originals/` or the series bible; always
show me chapter edits before applying; freely read anything and work without
nagging in `drafts/` and `notes/`; never delete files via `rm`.

Pair this with a workflow habit: Claude copies a chapter into `drafts/`, works
there, and you promote the result yourself. Permission rules are *not* a backup
strategy, though — keep Time Machine/Dropbox/git running regardless.

## Author use cases

1. **Developmental read in plan mode.** `Shift+Tab` to `plan` (or `/plan`), then:
   "Read the whole manuscript and give me a structural critique." Zero risk of
   stray edits while you talk it through.
2. **Revision afternoon in acceptEdits.** After agreeing on a line-edit list for
   `drafts/ch07.md`, switch to `acceptEdits` and let the changes flow without
   twenty confirmations. Switch back when done.
3. **Read-only research vault.** Give Claude reference access to your research
   folder without edit rights: add it via `/add-dir`, then deny edits:
   `"deny": ["Edit(//Users/you/Research/**)"]`.
4. **Shared project, personal looseness.** Team rules (protect originals) in
   `.claude/settings.json`; your personal extra allowances in
   `.claude/settings.local.json`, which stays private.
5. **Block the network, keep the books.** Deny `WebFetch` and `Bash(curl *)` in a
   project where you want Claude working purely from your files — no web sources
   sneaking into your worldbuilding.

## Common pitfalls

- **bypassPermissions ("yolo mode") on your real manuscript.** `claude
  --dangerously-skip-permissions` skips nearly every prompt. The docs are blunt:
  use it only in isolated environments (containers/VMs) where Claude cannot cause
  damage. An AI that misreads "clean up the drafts folder" can delete files. Almost
  no author needs this mode; deletions of your home folder still prompt as a
  circuit breaker, but that's the *only* net.
- **"Yes, don't ask again" is sticky.** For commands it's remembered permanently
  per project (file edits: until session end). Audit what you've accumulated in
  `/permissions`.
- **Deny rules don't cover indirect access.** `Edit` deny rules stop Claude's file
  tools and recognized file commands (`sed`, `cat`...), but a script Claude writes
  and runs could still modify files. For real OS-level walls, see sandboxing in the
  official docs. For most authors: deny + backups is plenty.
- **CLAUDE.md is not protection.** "Never edit originals/" in CLAUDE.md is a polite
  request. The deny rule is the lock. Use both.
- **Mode is per session.** `Shift+Tab` changes don't persist; set
  `"defaultMode"` in settings if you want a different startup posture.

## Advanced

**Settings file locations and precedence (highest wins; verified 2026-06-10):**

1. Managed/enterprise settings (IT-deployed; e.g. `/Library/Application Support/ClaudeCode/managed-settings.json` on macOS)
2. Command-line flags (session-only)
3. `.claude/settings.local.json` — project, personal (auto-gitignored)
4. `.claude/settings.json` — project, shared
5. `~/.claude/settings.json` — user-global

Permission rules **merge** across scopes rather than override, and evaluation order
is **deny → ask → allow** — first match wins, so a deny at any level beats an allow
at every other level. (`~/.claude.json` is a separate state file: OAuth session,
MCP servers, per-project trust. Leave it alone.)

**Rule syntax:** `Tool` or `Tool(specifier)`.

- Bare tool name matches everything: `Read`, `Edit`, `Bash`, `WebFetch`. As a deny,
  a bare name removes the tool from Claude's awareness entirely.
- **Bash:** glob with `*`, e.g. `Bash(git commit *)`, `Bash(* --help)`. The space
  matters: `Bash(ls *)` matches `ls -la` but not `lsof`. Compound commands
  (`a && b`) must match per-subcommand. A built-in set of read-only commands
  (`ls`, `cat`, `grep`, `pwd`, read-only `git`, ...) never prompts in any mode.
- **Read/Edit:** gitignore-style paths with four anchors —
  `Read(//absolute/path/**)`, `Read(~/Documents/*.docx)`,
  `Edit(/src-relative-to-project-root/**)`, `Edit(relative-to-cwd/**)`.
  Watch out: `Edit(/Users/you/...)` is project-root-relative, **not** absolute —
  absolute needs `//`. Bare filenames match at any depth: `Read(.env)` ≡
  `Read(**/.env)`. Deny rules also catch symlinks pointing at denied targets.
- **WebFetch:** `WebFetch(domain:example.com)`.
- **MCP tools:** `mcp__server` or `mcp__server__tool`
  (see [MCP](../02-power-features/mcp.md) if present).

**Other useful keys** in settings.json: `"defaultMode": "plan"` (or any mode),
`"additionalDirectories"` (extra readable folders), `"model"`, `"autoMemoryEnabled"`,
`"env"`, `"hooks"`, `"cleanupPeriodDays"` (session retention, default 30),
`"permissions": {"disableBypassPermissionsMode": "disable"}` to lock yourself out
of yolo mode entirely. Add
`"$schema": "https://json.schemastore.org/claude-code-settings.json"` for editor
autocomplete. Claude Code keeps timestamped backups of config files (5 most recent).

**CLI equivalents:** `claude --permission-mode plan`, `--allowedTools` /
`--disallowedTools` for one-off sessions, `--add-dir <path>`.

**Beyond rules:** PreToolUse **hooks** run your own script before each tool call
and can block or approve with arbitrary logic (e.g., block any edit to a file whose
name ends in `-FINAL.md`) — this can be packaged as a hook; see
[hooks](../02-power-features/hooks.md) if present. **Sandboxing** adds OS-level
filesystem/network isolation for Bash on supported platforms (`/sandbox`).

Related: [Installation & setup](installation-setup.md) ·
[CLAUDE.md and memory](claude-md-and-memory.md) · [Slash commands](slash-commands.md)
(`/permissions`, `/config`, `/plan`).

## Sources

- https://code.claude.com/docs/en/permissions (permission system, modes table, rule syntax, evaluation order, working directories, hooks interaction) — accessed 2026-06-10
- https://code.claude.com/docs/en/settings (file locations, precedence, available settings, ~/.claude.json, schema, backups) — accessed 2026-06-10
- https://code.claude.com/docs/en/interactive-mode (Shift+Tab mode cycling) — accessed 2026-06-10
- https://code.claude.com/docs/en/commands (/permissions, /plan, /fewer-permission-prompts, /sandbox) — accessed 2026-06-10
- ⚠️ Unverified: the exact wording of permission-prompt buttons may vary by version/surface; descriptions here follow the documented behavior ("Yes, don't ask again" persistence per the permissions page table).
