# Hooks: Automatic Guardrails for Your Writing Projects

> **In plain words:** A hook is a small rule that runs automatically at a fixed
> moment — for example, "every time Claude edits a file, make a backup copy first."
> Unlike instructions you put in CLAUDE.md (which Claude reads and *usually* follows),
> a hook is enforced by the Claude Code program itself, so it fires **every single
> time**, no exceptions. Think of it as a copyeditor who checks every page before it
> goes in the binder — without ever being asked.

## What it is

When Claude Code works on your project, it moves through predictable moments: a
session starts, you type a prompt, Claude is about to edit a file, Claude just
finished editing a file, Claude finishes responding. A **hook** is a command you
attach to one of those moments. When the moment arrives, Claude Code runs your
command automatically.

The key word is **deterministic** — a fancy way of saying "always happens."
If you write "never touch my published files" in CLAUDE.md, Claude will almost
always respect it, but it's still a request to an AI. A hook that blocks edits to
your `published/` folder is a locked door: even a confused or overeager Claude
cannot get through it. CLAUDE.md is your style memo to a trusted assistant; a hook
is the checklist taped to the binder — every page gets checked, whether anyone
remembers the memo or not.

## Why authors care

- **Protect finished work.** Block any edit to `originals/` or `published/` — archived
  manuscripts become untouchable, even during a sweeping revision.
- **Automatic backups.** Every time Claude edits a chapter, a timestamped copy lands
  in a backups folder. No more "what did that paragraph say before?"
- **Effortless progress tracking.** Log date and word count whenever a chapter
  changes — your writing log writes itself.
- **House style that never gets forgotten.** Inject your style rules at session start,
  automatically — including after long sessions when Claude's memory gets compressed.
- **Desktop notifications.** Get pinged when Claude finishes a long revision pass or
  needs approval, so you can make coffee instead of watching the terminal.

## Getting started

Your first hook in about three minutes: a macOS desktop notification whenever Claude
needs your attention.

1. Open your global settings file in any text editor:
   `~/.claude/settings.json` (that's the hidden `.claude` folder in your home folder).
   If the file doesn't exist, create it.
2. Add this (if the file already has content, merge the `"hooks"` key in rather than
   replacing everything):

   ```json
   {
     "hooks": {
       "Notification": [
         {
           "matcher": "",
           "hooks": [
             {
               "type": "command",
               "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
             }
           ]
         }
       ]
     }
   }
   ```

   On Windows, replace the command with a PowerShell message box (see the official
   guide's Windows tab); on Linux, use `notify-send 'Claude Code' 'Needs your attention'`.

3. In Claude Code, type `/hooks`. A read-only browser opens showing every hook event;
   confirm your new hook is listed under **Notification**. (The `/hooks` menu is for
   viewing only — to add or change hooks you edit the settings file, or simply ask
   Claude to write the hook for you.)
4. Ask Claude to do something that needs permission, then switch to another app.
   You should get a notification. *macOS quirk:* if nothing appears, run
   `osascript -e 'display notification "test"'` in Terminal once, then enable
   **Script Editor** under System Settings → Notifications.

**Where hooks live** decides their reach:

| File | Applies to |
|---|---|
| `~/.claude/settings.json` | All your projects (your machine only) |
| `.claude/settings.json` in a project | That project; can be shared with the project |
| `.claude/settings.local.json` in a project | That project, your machine only |

A tip from the official docs: you can describe the hook you want in plain English and
let Claude write the JSON for you — then review it before saving.

## Author use cases

All four examples below are complete and copy-pasteable. They use `jq`, a small free
tool that reads JSON; install it once with `brew install jq` on macOS. Put the script
files in a `.claude/hooks/` folder inside your book project, and the JSON in your
project's `.claude/settings.json`.

### 1. Manuscript protection: block edits to `originals/` and `published/`

Claude receives the blocked-edit reason as feedback, so it will explain and adjust
instead of silently failing.

Save as `.claude/hooks/protect-manuscript.sh`:

```bash
#!/bin/bash
# Blocks Claude from editing anything in originals/ or published/
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

case "$FILE_PATH" in
  */originals/*|*/published/*)
    echo "Blocked: $FILE_PATH is in a protected folder. Work on a copy in drafts/ instead." >&2
    exit 2
    ;;
esac
exit 0
```

Make it executable (one time): `chmod +x .claude/hooks/protect-manuscript.sh`

Register it in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-manuscript.sh"
          }
        ]
      }
    ]
  }
}
```

`PreToolUse` means "run this *before* Claude's edit happens" — exit code 2 cancels
the edit. Note: Claude can also change files through shell commands (`Bash`). For
belt-and-suspenders protection, pair this hook with a permission deny rule (see
[Settings & Permissions](../01-claude-code-basics/settings-and-permissions.md)).

### 2. Auto-backup: copy every edited chapter to a backups folder

Save as `.claude/hooks/backup-chapter.sh` and `chmod +x` it:

```bash
#!/bin/bash
# After any edit to a file in manuscript/, save a timestamped copy to backups/
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

case "$FILE_PATH" in
  */manuscript/*)
    mkdir -p "$CLAUDE_PROJECT_DIR/backups"
    BASENAME=$(basename "$FILE_PATH")
    cp "$FILE_PATH" "$CLAUDE_PROJECT_DIR/backups/${BASENAME%.*}-$(date +%Y%m%d-%H%M%S).${BASENAME##*.}"
    ;;
esac
exit 0
```

Register under `PostToolUse` ("run *after* a successful edit"):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/backup-chapter.sh"
          }
        ]
      }
    ]
  }
}
```

### 3. Word-count logger: progress log that writes itself

Save as `.claude/hooks/log-wordcount.sh`, `chmod +x` it, and register it as a second
entry in the same `PostToolUse` → `Edit|Write` hooks array as the backup script
(multiple hooks on one event are fine — they run in parallel):

```bash
#!/bin/bash
# Append date, chapter name, and word count to progress-log.txt
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

case "$FILE_PATH" in
  */chapters/*.md)
    WORDS=$(wc -w < "$FILE_PATH" | tr -d ' ')
    echo "$(date '+%Y-%m-%d %H:%M') | $(basename "$FILE_PATH") | $WORDS words" \
      >> "$CLAUDE_PROJECT_DIR/progress-log.txt"
    ;;
esac
exit 0
```

After a writing day, ask Claude: "Summarize progress-log.txt — how many words this
week?"

### 4. Session-start house style reminder

Whatever a `SessionStart` hook prints is added directly to Claude's context. Keep
a `house-style.md` in your project (POV rules, comma style, banned words, series
spellings) and inject it every session:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|compact",
        "hooks": [
          {
            "type": "command",
            "command": "cat \"$CLAUDE_PROJECT_DIR\"/house-style.md"
          }
        ]
      }
    ]
  }
}
```

The `compact` matcher value is the quiet hero: when a long session fills up and
Claude Code compresses the conversation ("compaction"), details can get lost — this
re-injects your style rules right after. For style guidance that should *always*
load, [CLAUDE.md](../01-claude-code-basics/claude-md-and-memory.md) is the simpler
tool; use the hook when you specifically want re-injection after compaction or
dynamic content (e.g., `git log --oneline -5` to show recent changes).

Any of these patterns can also be bundled into a shareable [plugin or skill](skills.md)
so your whole ARC team or course cohort gets the same guardrails.

## Common pitfalls

- **Hooks run real commands with *your* permissions.** A hook can do anything you can
  do at the keyboard — including delete files. Only install hooks you understand line
  by line; review anything pasted from the internet (or ask Claude to explain it
  first). This is the single most important rule on this page.
- **Hooks on `Edit|Write` don't see every file change.** Claude can also modify files
  via shell commands. For airtight coverage, also match `Bash` or add a `Stop` hook
  that scans for changes once per turn.
- **`PostToolUse` can't undo.** By the time it fires, the edit already happened. Use
  `PreToolUse` to prevent; `PostToolUse` to react.
- **JSON is unforgiving.** A trailing comma or stray comment breaks the whole settings
  file. If `/hooks` shows nothing after an edit, validate your JSON; restarting the
  session forces a reload.
- **Matchers are case-sensitive.** `edit|write` matches nothing; it must be `Edit|Write`.
- **`jq` may not be installed.** macOS: `brew install jq` — or write hook scripts in
  Python/Node instead.
- **Stop-hook loops are capped.** A `Stop` hook that keeps blocking is overridden
  after 8 consecutive blocks; check the `stop_hook_active` input field to exit early.
- **Cost note:** ordinary command hooks are free — they run on your machine. `prompt`
  and `agent` hook types (Advanced, below) make extra model calls, which count
  against your plan usage.

## Advanced

### Full configuration schema

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolNameOrPattern",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/script.sh",
            "timeout": 60,
            "statusMessage": "Checking manuscript rules…"
          }
        ]
      }
    ]
  },
  "disableAllHooks": false
}
```

Hook sources merge (they don't override each other): the three settings files above,
managed policy settings, plugin `hooks/hooks.json`, and skill/agent frontmatter
(active only while that component runs). Identical hook commands are deduplicated;
all matching hooks run in parallel, and when several return decisions the most
restrictive wins (`deny` > `defer` > `ask` > `allow`).

### Hook events (as of June 2026)

The event list has grown far beyond the original nine. Core events:

| Event | Fires | Matcher filters on |
|---|---|---|
| `SessionStart` | Session begins/resumes | `startup`, `resume`, `clear`, `compact` |
| `UserPromptSubmit` | You submit a prompt, before Claude sees it | (no matcher) |
| `PreToolUse` | Before a tool call; **can block** | Tool name (`Bash`, `Edit\|Write`, `mcp__.*`) |
| `PermissionRequest` | A permission dialog is about to appear; can answer it | Tool name |
| `PostToolUse` | After a tool call succeeds | Tool name |
| `PostToolUseFailure` | After a tool call fails | Tool name |
| `Notification` | Claude Code sends a notification | `permission_prompt`, `idle_prompt`, `auth_success`, … |
| `Stop` | Claude finishes responding | (no matcher) |
| `SubagentStart` / `SubagentStop` | Subagent spawned / finishes | Agent type |
| `PreCompact` / `PostCompact` | Before/after context compaction | `manual`, `auto` |
| `SessionEnd` | Session terminates | `clear`, `resume`, `logout`, `prompt_input_exit`, … |

Newer events (selected): `Setup`, `UserPromptExpansion`, `PermissionDenied`,
`PostToolBatch`, `StopFailure`, `InstructionsLoaded` (a CLAUDE.md/rules file loads),
`ConfigChange`, `CwdChanged`, `FileChanged` (watch named files),
`WorktreeCreate`/`WorktreeRemove`, `TaskCreated`/`TaskCompleted`, `TeammateIdle`,
`Elicitation`/`ElicitationResult` (MCP input forms), `MessageDisplay`. The docs list
~31 events total — see the reference for the full table.

### Matcher patterns

- `"*"`, `""`, or omitted → match everything.
- Plain names with `|` → exact match list: `Edit|Write`.
- Anything else → JavaScript regex: `^Notebook`, `mcp__memory__.*`.
- MCP tools follow `mcp__<server>__<tool>` naming, so `mcp__github__.*` targets one server.
- `FileChanged` is special: its matcher is a `|`-separated list of *literal filenames*.

The `if` field (v2.1.85+) filters by tool name *and arguments* using permission-rule
syntax, e.g. `"if": "Bash(git *)"` — but it's best-effort (fails open on unparseable
commands), so use real permission rules for hard enforcement.

### Mechanics: stdin, exit codes, JSON output

Every hook receives event JSON on **stdin**. Common fields: `session_id`,
`transcript_path`, `cwd`, `permission_mode`, `hook_event_name`. Event-specific
fields include `tool_name` + `tool_input` (tool events), `tool_output`
(`PostToolUse`), `prompt` (`UserPromptSubmit`), `source` (`SessionStart`).

Exit codes:

- **0** — no objection; action proceeds. Stdout is parsed for optional JSON; for
  `UserPromptSubmit`, `UserPromptExpansion`, and `SessionStart`, plain stdout is
  added to Claude's context. Exit 0 does **not** auto-approve a `PreToolUse` call —
  the normal permission flow still applies.
- **2** — blocking error. Stderr is fed to Claude as feedback. Some events
  (`SessionStart`, `Notification`, etc.) can't be blocked; exit 2 just shows stderr.
- **Anything else** — non-blocking error; first line of stderr shows in the
  transcript, full output goes to the debug log.

For finer control, exit 0 and print structured JSON (don't combine JSON with exit 2 —
it's ignored):

```json
{
  "continue": true,
  "stopReason": "shown to user when continue is false",
  "suppressOutput": false,
  "systemMessage": "optional warning shown to user",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Use the drafts folder instead"
  }
}
```

Decision control varies by event: `PreToolUse` uses
`hookSpecificOutput.permissionDecision` (`allow` / `deny` / `ask`, plus `defer` in
headless `-p` mode); `PostToolUse`, `Stop`, `SubagentStop`, `UserPromptSubmit`,
`PreCompact`, and others use top-level `"decision": "block"` + `"reason"`;
`PermissionRequest` uses `hookSpecificOutput.decision.behavior` (`allow`/`deny`,
optionally with `updatedPermissions`); `SessionStart`/`SubagentStart` return
`additionalContext`.

Timeouts: 600 s default for `command`/`http`/`mcp_tool` hooks (30 s for
`UserPromptSubmit`, 10 s for `MessageDisplay`), 30 s for `prompt`, 60 s for `agent`.
Override per hook with `"timeout"` (seconds).

### Hook types beyond `command`

- `"type": "http"` — POST the event JSON to a URL; the response body uses the same
  JSON output format (status codes alone can't block).
- `"type": "mcp_tool"` — call a tool on a connected [MCP server](mcp.md), with
  `${tool_input.file_path}`-style substitution.
- `"type": "prompt"` — one-shot model evaluation (fast model by default) returning
  `{"ok": true/false, "reason": "…"}`. Good for judgment calls on `Stop` hooks
  ("did Claude actually finish the revision checklist?").
- `"type": "agent"` — experimental multi-turn [subagent](subagents-and-orchestration.md)
  with tool access (up to 50 turns) for checks that require reading files.

Path placeholders available everywhere: `${CLAUDE_PROJECT_DIR}`,
`${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}` (also set as environment variables).

### Hooks and permission modes

`PreToolUse` hooks fire **before** any permission-mode check. A hook `deny` blocks
the tool even in `bypassPermissions` mode or with `--dangerously-skip-permissions` —
hooks are policy users can't sidestep by switching modes. The reverse doesn't hold:
a hook `allow` skips the prompt but never overrides deny rules from settings
(including managed/enterprise settings). Hooks can tighten, never loosen.

### Debugging

1. `Ctrl+O` toggles the transcript view: one line per fired hook (success silent,
   blocks show stderr, errors show a `<hook name> hook error` notice).
2. Full detail (which hooks matched, exit codes, stdout/stderr): start with
   `claude --debug-file /tmp/claude.log` and `tail -f /tmp/claude.log` in a second
   terminal, or run `/debug` mid-session.
3. Test scripts by hand:
   `echo '{"tool_name":"Edit","tool_input":{"file_path":"published/book.md"}}' | ./protect-manuscript.sh; echo $?`
4. Classic failures: script not executable (`chmod +x`), `jq` missing, relative paths
   (use `${CLAUDE_PROJECT_DIR}`), shell profile `echo` statements polluting JSON
   output (wrap them in an interactive-shell check).

### Hooks vs CLAUDE.md instructions

| | CLAUDE.md | Hook |
|---|---|---|
| Nature | Advisory — Claude reads and interprets | Deterministic — the app executes it |
| Reliability | High, not absolute | Absolute (for blockable events) |
| Good for | Style, voice, preferences, judgment | Protection, backups, logging, enforcement |
| Survives compaction | Re-read, but nuance can fade | Always fires; can re-inject context |

Rule of thumb: if breaking the rule once would genuinely hurt (overwriting a
published manuscript), it belongs in a hook or a permission rule, not in prose.

## Sources

- https://code.claude.com/docs/en/hooks-guide — "Automate actions with hooks" guide
  (accessed 2026-06-10): setup walkthrough, event table, exit codes, matchers, `if`
  field, hook locations, prompt/agent/HTTP hooks, troubleshooting, debug techniques.
- https://code.claude.com/docs/en/hooks — Hooks reference (accessed 2026-06-10):
  full event list (~31 events), configuration schema, matcher patterns, hook handler
  types and fields, input/output JSON shapes, decision control per event, timeout
  defaults, permission-mode interaction.
- ⚠️ Unverified: the exact wording of the reference page's "Security considerations"
  section could not be extracted (the guide links to it, confirming it exists). The
  safety guidance above states the principle — hooks execute shell commands with your
  user permissions — without quoting that section.
