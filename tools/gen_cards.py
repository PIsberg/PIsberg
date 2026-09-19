#!/usr/bin/env python3
"""Generate the project cards in assets/cards/ that README.md links to.

Run from the repo root:  python tools/gen_cards.py

The cards are plain SVG, so GitHub serves them as images: no scripts, no external
fonts, no external images. Everything a card shows has to be in the PROJECTS table
below. Edit the table and rerun; do not hand-edit the generated files.
"""
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "cards"

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "Consolas, Menlo, 'DejaVu Sans Mono', monospace"

# GitHub's own language colours, so the dot matches what the repo page shows.
LANG_COLOR = {"Java": "#B07219", "TypeScript": "#3178C6", "Rust": "#DEA584", "Go": "#00ADD8"}

# Icons are drawn on a 24x24 grid, stroked, never filled.
ICONS = {
    "shield": "M12 3l8 3v6c0 5-3.4 8.5-8 10c-4.6-1.5-8-5-8-10V6zM8.5 12l2.5 2.5l4.5-5",
    "wall": "M3 5h18v14H3zM3 9.7h18M3 14.3h18M9 5v4.7M15 5v4.7M12 9.7v4.6M9 14.3V19M15 14.3V19",
    "graph": "M6 6.5L18 5M6 6.5L12 18M18 5L12 18M6 6.5m-2.5 0a2.5 2.5 0 1 0 5 0a2.5 2.5 0 1 0-5 0M18 5m-2.5 0a2.5 2.5 0 1 0 5 0a2.5 2.5 0 1 0-5 0M12 18m-2.5 0a2.5 2.5 0 1 0 5 0a2.5 2.5 0 1 0-5 0",
    "refresh": "M20 12a8 8 0 0 1-14.3 4.9M4 12a8 8 0 0 1 14.3-4.9M18.5 3v4.3h-4.3M5.5 21v-4.3h4.3",
    "cursor": "M5 3l14 7.5l-6.2 1.8L10.5 19z",
    "barrier": "M3 7h7M3 12h7M3 17h7M12 4v16M14 12h7M18 9l3 3l-3 3",
    "search": "M10.5 10.5m-6.5 0a6.5 6.5 0 1 0 13 0a6.5 6.5 0 1 0-13 0M15.5 15.5L21 21",
    "map": "M3 6l6-2l6 2l6-2v14l-6 2l-6-2l-6 2zM9 4v14M15 6v14",
    "lock": "M6 11h12v9H6zM8.5 11V8a3.5 3.5 0 0 1 7 0v3M12 14.5v2.5",
}

PROJECTS = [
    ("llm-fw", "wall", "TypeScript",
     "Local prompt injection firewall. Malicious prompts are blocked and logged, clean ones pass through."),
    ("axiom", "graph", "Rust",
     "The codebase as a live queryable graph, so an agent can see what it just broke."),
    ("skill3", "refresh", "Java",
     "Relearns a technical skill for an agent, anchored to a target model cutoff, and vets the result."),
    ("ghost-mcp", "cursor", "Go",
     "MCP server that exposes OS level UI automation to AI clients."),
    ("async-test-lib", "barrier", "Java",
     "Forces concurrency bugs to happen using synchronized barriers, then names the one that fired."),
    ("codekoll", "search", "Java",
     "Static analyzer for Java that finds the bugs which compile perfectly and detonate in production."),
    ("codekarta", "map", "Java",
     "Parses Java source and emits SVG maps: call graphs, exception flow, state machines."),
    ("blindbean", "lock", "Java",
     "Homomorphic encryption hidden behind ordinary Java objects and annotations."),
]

FEATURED = ("vibetags", "shield", "Java",
            "Java annotations as AI guardrails. Mark the code an agent must not rewrite, "
            "and it stops rewriting it. Works with Claude, Cursor and Codex.")


def defs(w, h, uid):
    return f"""  <defs>
    <linearGradient id="bg{uid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0B1220"/>
      <stop offset="100%" stop-color="#111B2E"/>
    </linearGradient>
    <linearGradient id="ac{uid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F97316"/>
      <stop offset="100%" stop-color="#FBBF24"/>
    </linearGradient>
    <linearGradient id="top{uid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F97316" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#FBBF24" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="glow{uid}" cx="0%" cy="0%" r="75%">
      <stop offset="0%" stop-color="#F97316" stop-opacity="0.13"/>
      <stop offset="100%" stop-color="#F97316" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="clip{uid}"><rect width="{w}" height="{h}" rx="12"/></clipPath>
  </defs>"""


def shell(w, h, uid, label, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label, {'"': '&quot;'})}">
  <title>{escape(label)}</title>
{defs(w, h, uid)}
  <g clip-path="url(#clip{uid})">
    <rect width="{w}" height="{h}" fill="url(#bg{uid})"/>
    <rect width="{w}" height="{h}" fill="url(#glow{uid})"/>
    <rect width="{w}" height="2" fill="url(#top{uid})"/>
{body}
    <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="11.5" fill="none" stroke="#FFFFFF" stroke-opacity="0.09"/>
  </g>
</svg>
"""


def icon(x, y, name, uid):
    return f"""    <rect x="{x}" y="{y}" width="40" height="40" rx="10" fill="#F97316" fill-opacity="0.1" stroke="#F97316" stroke-opacity="0.35"/>
    <path transform="translate({x + 8} {y + 8})" d="{ICONS[name]}" fill="none" stroke="url(#ac{uid})" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>"""


def heading(x, y, name, size=21):
    return f"""    <text x="{x}" y="{y - 22}" font-family="{SANS}" font-size="12" fill="#7C8BA5">PIsberg /</text>
    <text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}" font-weight="700" fill="#F8FAFC">{escape(name)}</text>"""


def paragraph(x, y, text, width, size=13.5, lead=20):
    lines = textwrap.wrap(text, width)
    return "\n".join(
        f'    <text x="{x}" y="{y + i * lead}" font-family="{SANS}" font-size="{size}" fill="#AEB9CC">{escape(line)}</text>'
        for i, line in enumerate(lines))


def footer(x, y, right, lang):
    return f"""    <circle cx="{x + 5}" cy="{y - 4}" r="5" fill="{LANG_COLOR[lang]}"/>
    <text x="{x + 17}" y="{y}" font-family="{SANS}" font-size="12.5" fill="#CBD5E1">{lang}</text>
    <text x="{right}" y="{y}" text-anchor="end" font-family="{SANS}" font-size="12.5" font-weight="600" fill="#F97316">View repository &#8594;</text>"""


def card(name, icon_name, lang, desc):
    w, h = 490, 176
    body = "\n".join([
        icon(24, 24, icon_name, name),
        heading(78, 58, name),
        paragraph(24, 96, desc, 62),
        footer(24, h - 20, w - 24, lang),
    ])
    return shell(w, h, name, f"{name}: {desc}", body)


# One token per tuple: (text, colour). Mirrors the example in the vibetags README.
CODE = [
    [("@AILocked", "#FBBF24"), ("(reason = ", "#CBD5E1"), ('"Legacy payment integration"', "#86EFAC"), (")", "#CBD5E1")],
    [("public interface ", "#F97316"), ("PaymentProcessor", "#F8FAFC"), (" {", "#CBD5E1")],
    [("    // an agent may read this. It may not rewrite it.", "#64748B")],
    [("}", "#CBD5E1")],
]


def featured(name, icon_name, lang, desc):
    w, h = 1000, 210
    px, py, pw, ph = 520, 30, 452, 150
    rows = []
    for i, tokens in enumerate(CODE):
        spans = "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in tokens)
        rows.append(f'    <text x="{px + 20}" y="{py + 62 + i * 21}" font-family="{MONO}" font-size="13" xml:space="preserve">{spans}</text>')
    body = "\n".join([
        icon(28, 28, icon_name, name),
        heading(84, 63, name, 24),
        f'    <rect x="196" y="44" width="78" height="22" rx="11" fill="#F97316" fill-opacity="0.14" stroke="#F97316" stroke-opacity="0.5"/>',
        f'    <text x="235" y="59" text-anchor="middle" font-family="{SANS}" font-size="11" font-weight="700" letter-spacing="1.5" fill="#F97316">FEATURED</text>',
        paragraph(28, 104, desc, 62, 14.5, 22),
        footer(28, h - 22, 480, lang),
        f'    <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="10" fill="#060B16" stroke="#FFFFFF" stroke-opacity="0.08"/>',
        f'    <circle cx="{px + 20}" cy="{py + 18}" r="4.5" fill="#F87171"/><circle cx="{px + 36}" cy="{py + 18}" r="4.5" fill="#FBBF24"/><circle cx="{px + 52}" cy="{py + 18}" r="4.5" fill="#4ADE80"/>',
        f'    <text x="{px + pw - 16}" y="{py + 22}" text-anchor="end" font-family="{MONO}" font-size="11" fill="#64748B">PaymentProcessor.java</text>',
        f'    <path d="M{px} {py + 36}h{pw}" stroke="#FFFFFF" stroke-opacity="0.06"/>',
        *rows,
    ])
    return shell(w, h, name, f"{name}: {desc}", body)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    written = {FEATURED[0]: featured(*FEATURED)}
    written.update({p[0]: card(*p) for p in PROJECTS})
    for name, svg in written.items():
        (OUT / f"{name}.svg").write_text(svg, encoding="utf-8", newline="\n")
    print(f"wrote {len(written)} cards to {OUT}")


if __name__ == "__main__":
    main()
