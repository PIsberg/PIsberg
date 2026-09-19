#!/usr/bin/env python3
"""Generate every SVG the profile README uses, except the hand-drawn banner.

Run from the repo root:  python tools/gen_assets.py

Output:
  assets/cards/<repo>.svg   one card per project
  assets/ui/*.svg           section headers, buttons, pipeline, book panel, toolbox, footer

GitHub serves these as images: no scripts, no external fonts, no external images, and no
links inside the SVG (the README wraps each image in its own <a>). Everything shown has to
be in the tables below. Edit a table and rerun; do not hand-edit the generated files.

Animated elements always rest at opacity 0, so a frozen first frame (reduced motion, a
thumbnail, a slow renderer) still shows a finished image.
"""
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "assets" / "cards"
UI = ROOT / "assets" / "ui"

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "Consolas, Menlo, 'DejaVu Sans Mono', monospace"

INK, INK2, PANEL = "#080D19", "#111B2E", "#060B16"
ORANGE, AMBER = "#F97316", "#FBBF24"
WHITE, TEXT, MUTED, DIM = "#F8FAFC", "#CBD5E1", "#AEB9CC", "#7C8BA5"

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

# (repo, icon, language, card text)
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

# One token per tuple: (text, colour). Mirrors the example in the vibetags README.
CODE = [
    [("@AILocked", AMBER), ("(reason = ", TEXT), ('"Legacy payment integration"', "#86EFAC"), (")", TEXT)],
    [("public interface ", ORANGE), ("PaymentProcessor", WHITE), (" {", TEXT)],
    [("    // an agent may read this. It may not rewrite it.", "#64748B")],
    [("}", TEXT)],
]

# The pipeline diagram: (stage title, [(repo, what it does at this stage)]).
# Keep each role under 34 characters or it leaves its column.
PIPELINE = [
    ("BEFORE IT WRITES", [
        ("skill3", "teaches the agent current skills"),
        ("llm-fw", "filters prompts before the model"),
    ]),
    ("WHILE IT WRITES", [
        ("vibetags", "fences off code it must not touch"),
        ("axiom", "shows what a change just broke"),
        ("ghost-mcp", "gives it hands on the desktop"),
    ]),
    ("BEFORE IT SHIPS", [
        ("codekoll", "static analysis for silent bugs"),
        ("async-test-lib", "forces concurrency bugs to fire"),
        ("codekarta", "maps what was actually built"),
    ]),
]

SECTIONS = ["About", "The book", "How it fits together", "Open source", "Toolbox", "Activity"]

TOOLBOX = [
    ("PRIMARY", ["Java", "Spring Boot", "Gradle", "Maven"]),
    ("ALSO FLUENT", ["Rust", "TypeScript", "Go", "Python"]),
    ("PLATFORM + AI", ["Docker", "GitHub Actions", "Claude", "MCP", "Linux", "IntelliJ IDEA"]),
]

# (file, label, primary?)
BUTTONS = [
    ("btn-book", "Read the book", True),
    ("btn-site", "deversity.se", False),
    ("btn-email", "Email me", False),
]


def shell(w, h, uid, label, body, glow=True, top=True):
    """Shared frame: gradient ground, corner glow, top hairline, 1px inner border."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label, {'"': '&quot;'})}">
  <title>{escape(label)}</title>
  <defs>
    <linearGradient id="bg{uid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{INK}"/>
      <stop offset="100%" stop-color="{INK2}"/>
    </linearGradient>
    <linearGradient id="ac{uid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{ORANGE}"/>
      <stop offset="100%" stop-color="{AMBER}"/>
    </linearGradient>
    <linearGradient id="top{uid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{ORANGE}" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="{AMBER}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="fade{uid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{ORANGE}" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="{ORANGE}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="glow{uid}" cx="0%" cy="0%" r="75%">
      <stop offset="0%" stop-color="{ORANGE}" stop-opacity="0.13"/>
      <stop offset="100%" stop-color="{ORANGE}" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft{uid}" x="-20%" y="-400%" width="140%" height="900%">
      <feGaussianBlur stdDeviation="3"/>
    </filter>
    <clipPath id="clip{uid}"><rect width="{w}" height="{h}" rx="12"/></clipPath>
  </defs>
  <style>
    @media (prefers-reduced-motion: reduce) {{ .motion {{ display: none; }} }}
  </style>
  <g clip-path="url(#clip{uid})">
    <rect width="{w}" height="{h}" fill="url(#bg{uid})"/>
{f'    <rect width="{w}" height="{h}" fill="url(#glow{uid})"/>' if glow else ''}
{f'    <rect width="{w}" height="2" fill="url(#top{uid})"/>' if top else ''}
{body}
    <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="11.5" fill="none" stroke="#FFFFFF" stroke-opacity="0.09"/>
  </g>
</svg>
"""


def text(x, y, s, size, fill, weight=400, family=SANS, anchor="start", spacing=0):
    extra = f' letter-spacing="{spacing}"' if spacing else ""
    anc = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return (f'    <text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}"'
            f' fill="{fill}"{anc}{extra}>{escape(s)}</text>')


def icon(x, y, name, uid):
    return f"""    <rect x="{x}" y="{y}" width="40" height="40" rx="10" fill="{ORANGE}" fill-opacity="0.1" stroke="{ORANGE}" stroke-opacity="0.35"/>
    <path transform="translate({x + 8} {y + 8})" d="{ICONS[name]}" fill="none" stroke="url(#ac{uid})" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>"""


def paragraph(x, y, s, width, size=13.5, lead=20, fill=MUTED):
    return "\n".join(text(x, y + i * lead, line, size, fill) for i, line in enumerate(textwrap.wrap(s, width)))


def card_footer(x, y, right, lang):
    return "\n".join([
        f'    <circle cx="{x + 5}" cy="{y - 4}" r="5" fill="{LANG_COLOR[lang]}"/>',
        text(x + 17, y, lang, 12.5, TEXT),
        text(right, y, "View repository →", 12.5, ORANGE, 600, anchor="end"),
    ])


def card(name, icon_name, lang, desc):
    w, h = 490, 176
    body = "\n".join([
        icon(24, 24, icon_name, name),
        text(78, 36, "PIsberg /", 12, DIM),
        text(78, 58, name, 21, WHITE, 700),
        paragraph(24, 96, desc, 62),
        card_footer(24, h - 20, w - 24, lang),
    ])
    return shell(w, h, name, f"{name}: {desc}", body)


def code_window(px, py, pw, ph, filename, uid):
    rows = []
    for i, tokens in enumerate(CODE):
        spans = "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in tokens)
        rows.append(f'    <text x="{px + 20}" y="{py + 62 + i * 21}" font-family="{MONO}" font-size="13" xml:space="preserve">{spans}</text>')
    return "\n".join([
        f'    <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="10" fill="{PANEL}" stroke="#FFFFFF" stroke-opacity="0.08"/>',
        f'    <circle cx="{px + 20}" cy="{py + 18}" r="4.5" fill="#F87171"/><circle cx="{px + 36}" cy="{py + 18}" r="4.5" fill="{AMBER}"/><circle cx="{px + 52}" cy="{py + 18}" r="4.5" fill="#4ADE80"/>',
        text(px + pw - 16, py + 22, filename, 11, "#64748B", family=MONO, anchor="end"),
        f'    <path d="M{px} {py + 36}h{pw}" stroke="#FFFFFF" stroke-opacity="0.06"/>',
        *rows,
    ])


def featured(name, icon_name, lang, desc):
    w, h = 1000, 210
    body = "\n".join([
        icon(28, 28, icon_name, name),
        text(84, 41, "PIsberg /", 12, DIM),
        text(84, 63, name, 24, WHITE, 700),
        f'    <rect x="196" y="44" width="78" height="22" rx="11" fill="{ORANGE}" fill-opacity="0.14" stroke="{ORANGE}" stroke-opacity="0.5"/>',
        text(235, 59, "FEATURED", 11, ORANGE, 700, anchor="middle", spacing=1.5),
        paragraph(28, 104, desc, 62, 14.5, 22),
        card_footer(28, h - 22, 480, lang),
        code_window(520, 30, 452, 150, "PaymentProcessor.java", name),
    ])
    return shell(w, h, name, f"{name}: {desc}", body)


def section(index, title):
    """Numbered section header. Replaces a markdown heading, so the alt text carries the title."""
    w, h = 1000, 58
    # rough advance width of the title, to start the rule just after it
    rule_x = 96 + int(len(title) * 12.5) + 24
    body = "\n".join([
        text(28, 37, f"{index:02d}", 15, ORANGE, 700, family=MONO),
        f'    <path d="M62 20v18" stroke="{ORANGE}" stroke-opacity="0.5" stroke-width="1.5"/>',
        text(78, 38, title, 22, WHITE, 700),
        f'    <rect x="{rule_x}" y="29" width="{w - rule_x - 28}" height="1.5" fill="url(#fadesec{index})"/>',
    ])
    return shell(w, h, f"sec{index}", title, body, glow=False, top=False)


def pipeline():
    w, h = 1000, 372
    uid = "pipe"
    rail_y, x0, x1 = 104, 70, 930
    centers = [230, 500, 770]
    out = [
        text(40, 44, "HOW THE PROJECTS FIT TOGETHER", 12.5, ORANGE, 600, spacing=3),
        text(960, 44, "one pipeline, agent to production", 12.5, DIM, anchor="end"),
        # rects, not a stroked line: a horizontal path has a zero-height bounding box, and a
        # gradient or filter resolved against that box paints nothing at all
        f'    <rect x="{x0}" y="{rail_y - 3}" width="{x1 - x0}" height="6" rx="3" fill="{ORANGE}" fill-opacity="0.3" filter="url(#soft{uid})"/>',
        f'    <rect x="{x0}" y="{rail_y - 1}" width="{x1 - x0}" height="2" rx="1" fill="url(#ac{uid})"/>',
    ]
    for delay in (0, 1.7, 3.4):
        out.append(f"""    <circle class="motion" r="3.5" fill="#FFF7ED" opacity="0">
      <animateMotion dur="5s" begin="{delay}s" repeatCount="indefinite" path="M{x0} {rail_y}H{x1}"/>
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.06;0.92;1" dur="5s" begin="{delay}s" repeatCount="indefinite"/>
    </circle>""")
    for x, label, anchor in ((x0, "AI agent", "start"), (x1, "production", "end")):
        lx = x - 8 if anchor == "start" else x + 8
        out.append(f'    <circle cx="{x}" cy="{rail_y}" r="7" fill="{INK}" stroke="{ORANGE}" stroke-width="2"/>')
        out.append(text(lx, rail_y - 18, label, 12, TEXT, family=MONO, anchor=anchor))
    for i, (cx, (stage, rows)) in enumerate(zip(centers, PIPELINE), start=1):
        left = cx - 135
        out += [
            f'    <path d="M{cx} {rail_y + 14}V136" stroke="{ORANGE}" stroke-opacity="0.45" stroke-width="1.5" stroke-dasharray="3 4"/>',
            f'    <circle cx="{cx}" cy="{rail_y}" r="14" fill="{INK}" stroke="url(#ac{uid})" stroke-width="2"/>',
            text(cx, rail_y + 4.5, str(i), 13, AMBER, 700, family=MONO, anchor="middle"),
            f'    <rect x="{left}" y="136" width="270" height="212" rx="10" fill="{PANEL}" fill-opacity="0.7" stroke="#FFFFFF" stroke-opacity="0.07"/>',
            text(left + 20, 166, stage, 11.5, ORANGE, 700, family=MONO, spacing=1.5),
            f'    <path d="M{left + 20} 178h230" stroke="#FFFFFF" stroke-opacity="0.07"/>',
        ]
        for r, (repo, role) in enumerate(rows):
            y = 206 + r * 50
            out += [
                f'    <circle cx="{left + 25}" cy="{y - 5}" r="3" fill="{ORANGE}"/>',
                text(left + 38, y, repo, 15, WHITE, 700),
                text(left + 38, y + 18, role, 12.5, MUTED),
            ]
    label = "How the projects fit together. " + " ".join(
        f"Stage {i}, {stage.lower()}: " + ", ".join(f"{repo} {role}" for repo, role in rows) + "."
        for i, (stage, rows) in enumerate(PIPELINE, start=1))
    return shell(w, h, uid, label, "\n".join(out))


def book_panel():
    # 740x296 next to a 24%-wide cover (1216x1500) at 74% width gives both the same rendered height.
    w, h = 740, 296
    uid = "book"
    body = "\n".join([
        text(36, 54, "THE BOOK", 12.5, ORANGE, 600, spacing=3),
        text(36, 98, "Vibe Coding Architecture at Scale", 30, WHITE, 700),
        text(36, 136, "Vibe coding gives you speed. Vibe Architecture gives you scale.", 16, AMBER, 600),
        paragraph(36, 172, "When syntax is free, structure is your only asset. The book on designing, scaling "
                  "and guardrailing large-scale systems in the age of AI orchestration.", 84, 14.5, 23, TEXT),
        f'    <rect x="36" y="224" width="196" height="42" rx="21" fill="url(#ac{uid})"/>',
        text(134, 250.5, "Get it on Amazon →", 14.5, INK, 700, anchor="middle"),
        text(252, 250.5, "Kindle edition", 12.5, DIM),
    ])
    return shell(w, h, uid, "Vibe Coding Architecture at Scale. Vibe coding gives you speed. Vibe Architecture "
                 "gives you scale. Get it on Amazon.", body)


def toolbox():
    w, row_h, top = 1000, 46, 22
    h = top * 2 + row_h * len(TOOLBOX) - 8
    out = []
    for r, (label, items) in enumerate(TOOLBOX):
        y = top + r * row_h
        out.append(text(28, y + 21, label, 11.5, ORANGE, 700, family=MONO, spacing=1.5))
        x = 190
        for item in items:
            cw = int(len(item) * 7.6) + 30
            out.append(f'    <rect x="{x}" y="{y}" width="{cw}" height="32" rx="16" fill="#FFFFFF" fill-opacity="0.04" stroke="#FFFFFF" stroke-opacity="0.12"/>')
            out.append(text(x + cw / 2, y + 21, item, 13.5, WHITE if r == 0 else TEXT, 600 if r == 0 else 400, anchor="middle"))
            x += cw + 10
    label = "Toolbox. " + " ".join(f"{name.title()}: {', '.join(items)}." for name, items in TOOLBOX)
    return shell(w, h, "tools", label, "\n".join(out), glow=False)


def button(uid, label, primary):
    w, h = 220, 46
    fill = f'fill="url(#b{uid})"' if primary else f'fill="{INK2}" stroke="#FFFFFF" stroke-opacity="0.16"'
    colour = INK if primary else WHITE
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}">
  <title>{escape(label)}</title>
  <defs>
    <linearGradient id="b{uid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{ORANGE}"/>
      <stop offset="100%" stop-color="{AMBER}"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="22" {fill}/>
{text(w / 2, 28.5, label + "  →", 15, colour, 700, anchor="middle")}
</svg>
"""


def footer():
    w, h = 1000, 132
    uid = "foot"
    body = "\n".join([
        text(40, 58, "Building with AI agents and want it to stay correct?", 24, WHITE, 700),
        text(40, 92, "isberg.peter@gmail.com   ·   deversity.se   ·   Gothenburg, Sweden", 14.5, MUTED),
        f'    <rect x="782" y="44" width="178" height="44" rx="22" fill="url(#ac{uid})"/>',
        text(871, 71.5, "Get in touch →", 15, INK, 700, anchor="middle"),
    ])
    return shell(w, h, uid, "Building with AI agents and want it to stay correct? Get in touch: isberg.peter@gmail.com", body)


def main():
    files = {CARDS / f"{FEATURED[0]}.svg": featured(*FEATURED)}
    files.update({CARDS / f"{p[0]}.svg": card(*p) for p in PROJECTS})
    for i, title in enumerate(SECTIONS, start=1):
        files[UI / f"section-{i:02d}.svg"] = section(i, title)
    files[UI / "pipeline.svg"] = pipeline()
    files[UI / "book-panel.svg"] = book_panel()
    files[UI / "toolbox.svg"] = toolbox()
    files[UI / "footer.svg"] = footer()
    for uid, label, primary in BUTTONS:
        files[UI / f"{uid}.svg"] = button(uid.replace("-", ""), label, primary)
    for path, svg in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(svg, encoding="utf-8", newline="\n")
    print(f"wrote {len(files)} files")


if __name__ == "__main__":
    main()
