#!/usr/bin/env python3
"""Build a single self-contained HTML site from docs/wiki.

Usage: python3 docs/wiki-site/build.py
Output: docs/wiki-site/index.html

Requires pandoc on PATH (markdown -> HTML conversion).
"""

import posixpath
import re
import subprocess
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
OUT = Path(__file__).resolve().parent / "index.html"

SITE_TITLE = "The Claude Fable Starter Kit Wiki"

# (section label, [(relative path, slug, nav title), ...])
SECTIONS = [
    ("", [
        ("README.md", "home", "Home"),
    ]),
    ("Start here", [
        ("00-start-here/which-tool-when.md", "which-tool-when", "Which tool when"),
        ("00-start-here/quick-start.md", "quick-start", "Quick start"),
        ("00-start-here/managing-usage-and-cost.md", "managing-usage-and-cost", "Managing usage & cost"),
        ("00-start-here/glossary.md", "glossary", "Glossary"),
    ]),
    ("Claude Code basics", [
        ("01-claude-code-basics/installation-setup.md", "installation-setup", "Installation & setup"),
        ("01-claude-code-basics/claude-md-and-memory.md", "claude-md-and-memory", "CLAUDE.md & memory"),
        ("01-claude-code-basics/settings-and-permissions.md", "settings-and-permissions", "Settings & permissions"),
        ("01-claude-code-basics/slash-commands.md", "slash-commands", "Slash commands"),
    ]),
    ("Power features", [
        ("02-power-features/skills.md", "skills", "Skills"),
        ("02-power-features/subagents-and-orchestration.md", "subagents-and-orchestration", "Subagents & orchestration"),
        ("02-power-features/hooks.md", "hooks", "Hooks"),
        ("02-power-features/mcp.md", "mcp", "MCP"),
        ("02-power-features/claude-desktop.md", "claude-desktop", "Claude Desktop"),
    ]),
    ("Author workflows", [
        ("03-author-workflows/drafting-and-revision.md", "drafting-and-revision", "Drafting & revision"),
        ("03-author-workflows/research-and-worldbuilding.md", "research-and-worldbuilding", "Research & worldbuilding"),
        ("03-author-workflows/publishing-ops.md", "publishing-ops", "Publishing ops"),
        ("03-author-workflows/marketing-and-launch.md", "marketing-and-launch", "Marketing & launch"),
        ("03-author-workflows/adopting-and-sharing-tools.md", "adopting-and-sharing-tools", "Adopting & sharing tools"),
    ]),
    ("Reference", [
        ("04-reference/use-case-catalog.md", "use-case-catalog", "Use-case catalog"),
    ]),
]

PAGES = [(path, slug, title) for _, pages in SECTIONS for path, slug, title in pages]
# wiki-relative path -> slug, for cross-page link rewriting
PATH_TO_SLUG = {path: slug for path, slug, _ in PAGES}
# links to a section directory go to that section's first page
DIR_TO_SLUG = {posixpath.dirname(pages[0][0]): pages[0][1] for _, pages in SECTIONS}


def pandoc(md_path: Path) -> str:
    return subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html", "--wrap=none", str(md_path)],
        check=True, capture_output=True, text=True,
    ).stdout


def rewrite_page(html: str, page_rel: str, slug: str) -> str:
    page_dir = posixpath.dirname(page_rel)

    # Namespace ids so the same heading on two pages can't collide.
    html = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{slug}--{m.group(1)}"', html)

    def fix_href(m):
        href = m.group(1)
        if href.startswith(("http://", "https://", "mailto:")):
            return f'href="{href}" target="_blank" rel="noopener"'
        if href.startswith("#"):  # same-page anchor
            return f'href="#{slug}/{href[1:]}"'
        target, frag = (href.split("#", 1) + [""])[:2]
        resolved = posixpath.normpath(posixpath.join(page_dir, target))
        if resolved in PATH_TO_SLUG:
            tslug = PATH_TO_SLUG[resolved]
            return f'href="#{tslug}/{frag}"' if frag else f'href="#{tslug}"'
        if resolved in DIR_TO_SLUG:
            return f'href="#{DIR_TO_SLUG[resolved]}"'
        # Outside the wiki (e.g. ../../fable-documentation/...): point at the
        # repo file relative to docs/wiki-site/.
        repo_rel = posixpath.normpath(posixpath.join("..", "wiki", page_dir, href))
        return f'href="{repo_rel}"'

    html = re.sub(r'href="([^"]+)"', fix_href, html)
    # Wide tables (the use-case catalog) need their own scrollbar.
    html = html.replace("<table>", '<div class="table-wrap"><table>')
    html = html.replace("</table>", "</table></div>")
    return html


def validate(sections_html: dict):
    ids = set()
    for h in sections_html.values():
        ids.update(re.findall(r'\bid="([^"]+)"', h))
    bad = []
    for slug, h in sections_html.items():
        for href in re.findall(r'href="#([^"]+)"', h):
            page, _, frag = href.partition("/")
            if page not in PATH_TO_SLUG.values():
                bad.append((slug, href, "unknown page"))
            elif frag and f"{page}--{frag}" not in ids:
                bad.append((slug, href, "missing anchor"))
    for slug, href, why in bad:
        print(f"  warn: {slug} -> #{href} ({why})", file=sys.stderr)
    return bad


CSS = """
:root {
  --bg: #ffffff;
  --text: #161616;
  --muted: #6e6e6e;
  --faint: #9b9b9b;
  --hairline: #e7e7e7;
  --code-bg: #f5f5f5;
  --link: #1f5f93;
  --sidebar-w: 252px;
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font: 400 15.5px/1.65 -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", system-ui, sans-serif;
  letter-spacing: -0.006em;
}

/* ---- sidebar ---- */
nav {
  position: fixed;
  inset: 0 auto 0 0;
  width: var(--sidebar-w);
  overflow-y: auto;
  border-right: 1px solid var(--hairline);
  padding: 28px 20px 40px 28px;
}
nav .site-title {
  display: block;
  font-size: 14px;
  font-weight: 600;
  line-height: 1.35;
  color: var(--text);
  text-decoration: none;
  margin-bottom: 6px;
}
nav .site-sub {
  font-size: 12px;
  color: #767676;
  margin: 0 0 28px;
}
nav .section {
  font-size: 10.5px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  color: #767676;
  margin: 26px 0 8px;
}
nav a.page {
  display: block;
  padding: 4px 0;
  font-size: 13.5px;
  color: #3c3c3c;
  text-decoration: none;
}
nav a.page:hover { color: var(--text); }
nav a.page.active { color: var(--text); font-weight: 600; }

/* ---- content ---- */
main {
  margin-left: var(--sidebar-w);
  padding: 56px 56px 96px;
}
main > section { display: none; max-width: 42.5rem; }
main > section.active { display: block; }

h1 {
  font-size: 27px;
  font-weight: 650;
  letter-spacing: -0.022em;
  line-height: 1.2;
  margin: 0 0 20px;
}
h2 {
  font-size: 19px;
  font-weight: 600;
  letter-spacing: -0.014em;
  line-height: 1.3;
  margin: 44px 0 12px;
  padding-top: 24px;
  border-top: 1px solid var(--hairline);
}
h3 { font-size: 16px; font-weight: 600; letter-spacing: -0.01em; margin: 30px 0 8px; }
h4 { font-size: 14.5px; font-weight: 600; margin: 24px 0 6px; }
p { margin: 0 0 14px; }
ul, ol { margin: 0 0 14px; padding-left: 22px; }
li { margin: 4px 0; }
li > ul, li > ol { margin-bottom: 0; }
hr { border: 0; border-top: 1px solid var(--hairline); margin: 36px 0; }

a { color: var(--link); text-decoration: underline; text-decoration-color: rgba(31, 95, 147, 0.3); text-underline-offset: 2.5px; }
a:hover { text-decoration-color: currentColor; }

blockquote {
  margin: 0 0 18px;
  padding: 2px 0 2px 18px;
  border-left: 2px solid var(--text);
  color: #3d3d3d;
}
blockquote p:last-child { margin-bottom: 0; }

code, kbd {
  font-family: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, monospace;
  font-size: 0.86em;
}
code { background: var(--code-bg); border-radius: 4px; padding: 1.5px 5px; }
pre {
  background: var(--code-bg);
  border-radius: 6px;
  padding: 14px 16px;
  overflow-x: auto;
  margin: 0 0 16px;
  line-height: 1.55;
}
pre code { background: none; padding: 0; font-size: 13px; }
kbd {
  background: #fafafa;
  border: 1px solid var(--hairline);
  border-bottom-width: 2px;
  border-radius: 4px;
  padding: 1px 5px;
  font-size: 0.8em;
}

.table-wrap { overflow-x: auto; margin: 0 0 18px; }
table { border-collapse: collapse; width: 100%; font-size: 13.5px; line-height: 1.5; }
th {
  text-align: left;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--muted);
  padding: 8px 14px 8px 0;
  border-bottom: 1px solid var(--text);
}
td {
  vertical-align: top;
  padding: 9px 14px 9px 0;
  border-bottom: 1px solid var(--hairline);
}

.pager {
  display: flex;
  justify-content: space-between;
  gap: 24px;
  margin-top: 56px;
  padding-top: 20px;
  border-top: 1px solid var(--hairline);
  font-size: 13.5px;
}
.pager a { text-decoration: none; color: var(--text); max-width: 48%; }
.pager a:hover .pager-title { text-decoration: underline; }
.pager .label { display: block; font-size: 10.5px; text-transform: uppercase; letter-spacing: 0.09em; color: var(--faint); margin-bottom: 3px; }
.pager .next { margin-left: auto; text-align: right; }

footer.colophon {
  margin-top: 28px;
  font-size: 12px;
  color: var(--faint);
}

/* ---- small screens ---- */
.menu-toggle { display: none; }
@media (max-width: 880px) {
  .menu-toggle {
    display: block;
    position: fixed;
    top: 14px;
    right: 16px;
    z-index: 3;
    background: var(--bg);
    border: 1px solid var(--hairline);
    border-radius: 6px;
    padding: 6px 12px;
    font: 600 12.5px/1 inherit;
    font-family: inherit;
    color: var(--text);
    cursor: pointer;
  }
  nav {
    width: min(320px, 86vw);
    background: var(--bg);
    z-index: 2;
    transform: translateX(-100%);
    transition: transform 0.2s ease;
  }
  body.nav-open nav { transform: none; box-shadow: 8px 0 24px rgba(0,0,0,0.06); }
  main { margin-left: 0; padding: 56px 22px 80px; }
}
"""

JS = """
const sections = document.querySelectorAll('main > section');
const navLinks = document.querySelectorAll('nav a.page');

function route() {
  const raw = decodeURIComponent(location.hash.slice(1)) || 'home';
  const [slug, anchor] = raw.split('/');
  let found = false;
  sections.forEach(s => {
    const on = s.dataset.page === slug;
    s.classList.toggle('active', on);
    if (on) found = true;
  });
  if (!found) { location.hash = '#home'; return; }
  navLinks.forEach(a => a.classList.toggle('active', a.dataset.page === slug));
  const active = document.querySelector('nav a.page.active');
  document.title = (active && slug !== 'home' ? active.textContent + ' · ' : '') + SITE_TITLE;
  document.body.classList.remove('nav-open');
  if (anchor) {
    const el = document.getElementById(slug + '--' + anchor);
    if (el) { el.scrollIntoView(); return; }
  }
  window.scrollTo(0, 0);
}

window.addEventListener('hashchange', route);
document.querySelector('.menu-toggle').addEventListener('click', () => {
  document.body.classList.toggle('nav-open');
});
route();
"""


def build():
    sections_html = {}
    for path, slug, _ in PAGES:
        sections_html[slug] = rewrite_page(pandoc(WIKI / path), path, slug)

    validate(sections_html)

    nav = [f'<a class="site-title" href="#home">{SITE_TITLE}</a>',
           '<p class="site-sub">For fiction authors, terminal optional</p>']
    for label, pages in SECTIONS:
        if label:
            nav.append(f'<div class="section">{label}</div>')
        for _, slug, title in pages:
            if slug == "home":
                continue
            nav.append(f'<a class="page" data-page="{slug}" href="#{slug}">{title}</a>')

    body = []
    for i, (_, slug, title) in enumerate(PAGES):
        pager = []
        if i > 0:
            _, pslug, ptitle = PAGES[i - 1]
            pager.append(f'<a href="#{pslug}"><span class="label">Previous</span><span class="pager-title">{ptitle}</span></a>')
        if i < len(PAGES) - 1:
            _, nslug, ntitle = PAGES[i + 1]
            pager.append(f'<a class="next" href="#{nslug}"><span class="label">Next</span><span class="pager-title">{ntitle}</span></a>')
        body.append(
            f'<section data-page="{slug}">\n{sections_html[slug]}\n'
            f'<div class="pager">{"".join(pager)}</div>\n'
            '<footer class="colophon">Generated from docs/wiki · verified against official Anthropic docs 2026-06-10</footer>\n'
            '</section>'
        )

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{SITE_TITLE}</title>
<style>{CSS}</style>
</head>
<body>
<button class="menu-toggle" aria-label="Toggle navigation">Menu</button>
<nav>
{chr(10).join(nav)}
</nav>
<main>
{chr(10).join(body)}
</main>
<script>const SITE_TITLE = {SITE_TITLE!r};{JS}</script>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.0f} KB, {len(PAGES)} pages)")


if __name__ == "__main__":
    build()
