# MCP: Connecting Claude to Your Other Tools

> **In plain words:** MCP (Model Context Protocol) is a standard plug that lets
> Claude connect to your other tools and accounts — your Notion story bible, your
> Obsidian research vault, your Slack, your spreadsheets. Instead of copying and
> pasting between apps, you give Claude a key to specific rooms, and it can read
> from (and write to) them directly while you work.

## What it is

Think of Claude out of the box as an assistant locked in one office: it can talk
with you, and in Claude Code it can read and edit the files in your project
folder. MCP is the standard doorway that lets it into *other* rooms — but only
the rooms you choose. Each "MCP server" is a key to one room: one server for
Notion, one for your file system, one for Slack, and so on. Because MCP is an
open standard (think of it as a USB-C port for AI apps), the same connectors
work across Claude Desktop, claude.ai, Claude Code, and many non-Anthropic tools.

An MCP server can offer Claude three kinds of things, and you'll see all three
in practice: **tools** (actions Claude can take, like "search my Notion
workspace" or "send a Slack message" — these run with your approval),
**resources** (file-like data Claude can read, like a page from your story
bible, which you can pull into a Claude Code chat with an `@` mention), and
**prompts** (pre-written task templates the server provides, which show up in
Claude Code as slash commands like `/mcp__notion__something`). Most servers
you'll use as an author are mainly about tools.

## Why authors care

- **Stop being the courier.** No more pasting your character sheet from Notion
  into the chat every session. Claude looks it up itself, mid-draft.
- **Your story bible becomes live reference.** "Check the series bible before
  writing this scene — what color are Mara's eyes, and is she still estranged
  from her brother in book 3?"
- **Research notes on tap.** Claude can search your Obsidian vault for that
  19th-century whaling research you collected two years ago.
- **Bookkeeping without the bookkeeping.** Log daily word counts to a tracker,
  post "chapter 12 drafted" to your accountability channel — automatically.
- **One standard, everywhere.** A connector you learn in Claude Desktop works
  on the same protocol as the ones in Claude Code.

## Getting started

### First win in Claude Desktop (no terminal required)

1. Open Claude Desktop and go to **Settings > Extensions**.
2. Click **Browse extensions** to see the Anthropic-reviewed directory
   (filesystem access, iMessage, and others).
3. Install one — for example, filesystem access pointed at your manuscripts
   folder — and grant the permissions it asks for.
4. In a chat, click the **+** button at the bottom of the chat box, choose
   **Connectors**, and confirm your new connection is on.
5. Ask: *"List the chapter files in my Drafts folder and tell me which one I
   touched most recently."*

You can also add **remote connectors** (cloud services like Notion) on claude.ai
or Claude Desktop via **Customize > Connectors > + > Add custom connector**,
paste the service's MCP URL, and sign in when prompted. Custom connectors are
available on Free (limited to one connector), Pro, Max, Team, and Enterprise
plans; on Team/Enterprise an admin adds them under Organization settings.

### First win in Claude Code (one command)

1. Open your terminal in your book project folder.
2. Connect Notion's official server:

   ```bash
   claude mcp add --transport http notion https://mcp.notion.com/mcp
   ```

3. Start `claude`, type `/mcp`, select Notion, and complete the browser sign-in
   (OAuth — you log in to Notion itself; Claude never sees your password).
4. Ask: *"Search my Notion for the 'Hollow Crown' series bible and summarize
   the magic-system rules."*

You can also browse reviewed connectors in the Anthropic Directory at
claude.ai/directory; anything there can be added to Claude Code with
`claude mcp add`. And if you already set up servers in Claude Desktop,
`claude mcp add-from-claude-desktop` imports them (macOS and WSL).

## Author use cases

1. **Pull series facts mid-draft (Notion).** With the Notion connector
   attached, draft in Claude Code and say: *"Before writing chapter 14, fetch
   the timeline page from my story bible and confirm where each POV character
   is at the end of chapter 13."* Claude queries Notion instead of guessing.
2. **Search your research vault (Obsidian).** Two routes: (a) since an Obsidian
   vault is just Markdown files, point the official **filesystem** server (or
   Claude Code itself) at the vault folder — zero extra setup; or (b) install
   the community **Local REST API** plugin in Obsidian plus an Obsidian MCP
   server for vault-aware search, append, and patch operations. Then: *"Search
   my vault for everything tagged #lighthouse-research and give me sensory
   details I can use in scene 3."*
3. **Log daily word counts (Airtable).** Connect the community Airtable server
   with an API key, then end each session with: *"Count today's new words in
   chapter-14.md and add a row to my Writing Log base with date and count."*
   This pairs well with a hook that runs automatically when a session ends —
   see [hooks.md](hooks.md).
4. **Chapter-done notifications (Slack).** With the Slack connector (available
   in the claude.ai connectors directory), finish a revision pass and have
   Claude post *"Ch. 12 revised — 4,100 words, ready for beta"* to your
   accountability or ARC-team channel.
5. **Fetch craft articles and comp research (web).** The official **fetch**
   reference server retrieves a web page and converts it to clean text — useful
   for pulling a craft essay or a comp title's description into your planning
   session. (Claude Code also has built-in web search; the fetch server matters
   more in clients without one.)
6. **Email and calendar (claude.ai connectors).** Anthropic hosts connectors
   for Gmail, Google Calendar, Google Drive, and Microsoft 365 on claude.ai —
   useful for "find the editorial letter my editor emailed in March." Note:
   these particular connectors are authenticated on claude.ai (Settings >
   Connectors), and then appear in Claude Code automatically if you're logged
   in with the same claude.ai account.
7. **Repeatable workflows as one command.** If a server exposes prompts, they
   appear as slash commands — and you can wrap multi-step MCP routines into a
   skill of your own; see [skills.md](skills.md).

## Common pitfalls

- **Every server is a real key.** A connected MCP server acts with *your*
  access. A Notion server can edit your Notion; a filesystem server can change
  files. Only add servers from sources you trust, and prefer official ones
  (Notion's own, Anthropic's directory) over random GitHub repos.
- **Prompt injection.** If Claude reads untrusted content through a server — a
  web page, a public form response, an email — that content could contain
  hidden instructions ("ignore previous instructions and..."). Be most careful
  with servers that both *read untrusted content* and *can take actions*.
  Review what Claude is about to do before approving tool calls.
- **OAuth vs. API keys.** OAuth (browser sign-in) is safer: you can revoke
  access from the service's side and Claude never holds your password. API
  keys are static secrets — don't paste them into files you'll share or commit
  to GitHub. In Claude Code, put keys in environment variables (see Advanced).
- **Context cost.** Every connected server's tools take up some of Claude's
  working memory. Claude Code mitigates this with Tool Search (tools load on
  demand), but in Claude Desktop, ten connectors with dozens of tools each can
  crowd the conversation. Connect what you use; toggle off the rest.
- **Tool calls use your usage allowance.** Each MCP call is part of the
  conversation, and large outputs (a whole Notion database) consume tokens
  fast. Claude Code warns when a single MCP output exceeds 10,000 tokens.
- **"It's configured but not showing up."** In Claude Code, run `/mcp` to see
  status. Project-shared servers need a one-time approval; remote servers may
  need authentication (also via `/mcp`). In Claude Desktop, fully restart the
  app after editing config by hand.
- **Old names linger.** Desktop extension files were `.dxt` until September
  2025; the current format is `.mcpb` (MCP Bundle). Old `.dxt` files still
  install, but expect `.mcpb` in current docs and downloads. Likewise the SSE
  transport is deprecated in favor of HTTP — prefer HTTP when a service offers
  both.

## Advanced

### Transports

| Transport | What it is | When you'll use it |
|---|---|---|
| `stdio` | A local program Claude launches on your machine | Filesystem, Obsidian, anything touching local files |
| `http` | A remote server you connect to by URL (the spec calls it `streamable-http`) | Cloud services: Notion, Sentry, GitHub. Supports OAuth. Recommended for remote. |
| `sse` | Older remote transport (Server-Sent Events) | Deprecated — only if a service offers nothing else |
| `ws` | WebSocket, for servers that push events to Claude | Niche; configured via JSON only, header auth only |

### `claude mcp` command reference (verified June 2026)

```bash
# Remote HTTP server (with optional auth header)
claude mcp add --transport http notion https://mcp.notion.com/mcp
claude mcp add --transport http gh https://api.githubcopilot.com/mcp/ \
  --header "Authorization: Bearer YOUR_TOKEN"

# Local stdio server — note the bare `--` separating Claude's flags
# from the server's own command and flags
claude mcp add --env AIRTABLE_API_KEY=YOUR_KEY --transport stdio airtable \
  -- npx -y airtable-mcp-server

# Raw JSON form
claude mcp add-json my-server '{"type":"http","url":"https://mcp.example.com/mcp"}'

# Manage
claude mcp list           # all servers + status
claude mcp get notion     # details for one
claude mcp remove notion
claude mcp add-from-claude-desktop   # import Desktop config (macOS/WSL)
claude mcp reset-project-choices     # re-prompt for .mcp.json approvals
```

Inside a session, `/mcp` shows connection status and tool counts, runs OAuth
flows, and lets you clear authentication.

### Scopes

| Scope | Flag | Loads in | Stored in | Share with collaborators? |
|---|---|---|---|---|
| local (default) | `--scope local` | current project only | `~/.claude.json` | no |
| project | `--scope project` | current project only | `.mcp.json` in project root | yes — commit it |
| user | `--scope user` | all your projects | `~/.claude.json` | no |

Precedence when the same name exists in several places: local > project >
user > plugin-provided > claude.ai connectors. Claude Code prompts before
using a project's `.mcp.json` the first time, since it arrived with the repo.

A committed `.mcp.json` is how a co-writing team or a course cohort shares one
setup. Environment variables keep secrets out of the file:

```json
{
  "mcpServers": {
    "airtable": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "airtable-mcp-server"],
      "env": { "AIRTABLE_API_KEY": "${AIRTABLE_API_KEY}" }
    },
    "notion": { "type": "http", "url": "https://mcp.notion.com/mcp" }
  }
}
```

`${VAR}` and `${VAR:-default}` expand in `command`, `args`, `env`, `url`, and
`headers`. If a referenced variable is unset with no default, the config fails
to parse. Other useful knobs: per-server `"timeout"` (ms) for tool calls;
`MCP_TIMEOUT` env var for startup timeout; `MAX_MCP_OUTPUT_TOKENS` (default
25,000) for large outputs; `"alwaysLoad": true` to exempt a server from tool
search deferral.

### Tool Search (deferred tools)

By default Claude Code defers MCP tool definitions: only names and server
instructions load at startup, and Claude fetches full tool schemas on demand
via a `ToolSearch` tool. This is why you can attach many servers without
draining the context window. Control it with `ENABLE_TOOL_SEARCH`
(`true` / `false` / `auto` / `auto:N` threshold percent); disabled by default
on Vertex AI and non-first-party proxies.

### Claude Desktop / claude.ai specifics

- **Desktop extensions (`.mcpb`)**: zip bundles containing a local server plus
  a `manifest.json` — one-click install via Settings > Extensions > Advanced
  settings. Build your own with the `mcpb` CLI (`mcpb init`, `mcpb pack`).
  `.dxt` is the legacy name for the same format.
- **Hand-edited config**: Claude Desktop also reads
  `claude_desktop_config.json` (macOS: `~/Library/Application
  Support/Claude/claude_desktop_config.json`; Windows:
  `%APPDATA%\Claude\claude_desktop_config.json`) using the same `mcpServers`
  JSON shape as above. ⚠️ Unverified: exact current in-app menu wording for
  opening this file — the support docs now steer users to Extensions instead.
- **Remote connectors**: Customize > Connectors > Add custom connector with a
  server URL; OAuth client ID/secret under Advanced settings if the service
  requires pre-registered credentials.
- Connectors added on claude.ai flow into Claude Code automatically when you
  authenticate Claude Code with the same claude.ai subscription
  (`ENABLE_CLAUDEAI_MCP_SERVERS=false` disables this).

### Verified servers worth knowing (June 2026)

- **Official reference servers** (github.com/modelcontextprotocol/servers):
  `filesystem`, `fetch`, `git`, `memory`, `sequential-thinking`, `time`,
  `everything`. Note the old reference servers for Google Drive, Slack,
  GitHub, and several databases are **archived**; those services now live as
  claude.ai connectors or vendor-run remote servers instead.
- **Notion** — official remote server at `https://mcp.notion.com/mcp`.
- **GitHub** — remote server at `https://api.githubcopilot.com/mcp/` (token
  header auth).
- **Slack, Gmail, Google Calendar, Google Drive, Microsoft 365** — Anthropic-
  hosted connectors via claude.ai (Settings > Connectors / the directory at
  claude.ai/directory).
- **Airtable** — community `airtable-mcp-server` (npx), shown in Anthropic's
  own docs examples.
- **Obsidian** — community options: the Local REST API plugin
  (coddingtonbear/obsidian-local-rest-api, which now ships its own MCP
  endpoint) and MarkusPfundstein/mcp-obsidian which talks to that plugin.
  Community-maintained, not Anthropic-reviewed.
- ⚠️ Unverified: a dedicated Google Sheets MCP server suitable for word-count
  logging — community options exist but none was verified for this doc; the
  Airtable or filesystem (CSV) routes above are the verified paths.

### Building a minimal server

The official SDKs (Python, TypeScript, and others) make a toy server short.
Python with FastMCP, from the official quickstart pattern:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("wordcount")

@mcp.tool()
def count_words(text: str) -> str:
    """Count words in a passage of manuscript text."""
    return f"{len(text.split())} words"

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

Register it: `claude mcp add --transport stdio wordcount -- python
/path/to/server.py`. Full tutorial: modelcontextprotocol.io/docs/develop/build-server
(builds a weather server end-to-end and connects it to Claude Desktop). Claude
Code can also scaffold one for you via the official `mcp-server-dev` plugin
(`/plugin install mcp-server-dev@claude-plugins-official`, then
`/mcp-server-dev:build-mcp-server`).

### Debugging

- `/mcp` in-session: per-server status, tool counts, auth state, "needs
  authentication" flags (triggered by 401/403 responses).
- `claude mcp list` / `claude mcp get <name>` from the shell; pending
  `.mcp.json` approvals show as `⏸ Pending approval`.
- HTTP/SSE servers auto-reconnect with backoff (up to five attempts); stdio
  servers don't — restart the session or fix the command.
- Stdio servers must never print logs to stdout (it corrupts the protocol);
  log to stderr or a file. In Claude Desktop, server logs land in the app's
  log folder (macOS: `~/Library/Logs/Claude`). ⚠️ Unverified: exact current
  log filename pattern.

## Sources

- https://code.claude.com/docs/en/mcp (accessed 2026-06-10) — Claude Code MCP
  reference: `claude mcp add` syntax, transports, scopes, `.mcp.json`, env
  expansion, OAuth, `/mcp`, tool search, output limits, claude.ai connectors.
- https://modelcontextprotocol.io/ (accessed 2026-06-10) — protocol overview,
  USB-C analogy.
- https://modelcontextprotocol.io/docs/develop/build-server (accessed
  2026-06-10) — tools/resources/prompts definitions, FastMCP quickstart.
- https://github.com/modelcontextprotocol/servers (accessed 2026-06-10) —
  current reference servers and archived list.
- https://support.claude.com/en/articles/10065433 and
  https://support.claude.com/en/articles/10949351 (accessed 2026-06-10) —
  Claude Desktop extensions, Settings > Extensions, `.mcpb` install flow.
- https://support.claude.com/en/articles/11175166 (accessed 2026-06-10) —
  custom connectors (remote MCP) on claude.ai/Desktop, plan availability.
- https://github.com/modelcontextprotocol/mcpb and
  https://www.anthropic.com/engineering/desktop-extensions (accessed
  2026-06-10) — `.dxt` → `.mcpb` rename (September 2025), bundle format.
- https://github.com/MarkusPfundstein/mcp-obsidian and
  https://github.com/coddingtonbear/obsidian-local-rest-api (accessed
  2026-06-10) — Obsidian MCP options (community).
