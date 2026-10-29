"""Builds the profile SVGs in assets/ (dark + light). Run: python3 scripts/build_svgs.py

Every number here is copied from the linked repo's README or docs. Change the
repo first, then this file.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

THEMES = {
    "dark": dict(bg="#0d1117", card="#161b22", line="#30363d", fg="#e6edf3",
                 mute="#8b949e", acc="#3fb950", acc2="#58a6ff", warn="#f85149", dim="#1f2a1f"),
    "light": dict(bg="#ffffff", card="#f6f8fa", line="#d0d7de", fg="#1f2328",
                  mute="#59636e", acc="#1a7f37", acc2="#0969da", warn="#cf222e", dim="#dafbe1"),
}

# GitHub identicon of inpilot-dev, 5x5 (1 = filled)
IDENTICON = ["10001", "10001", "00100", "01010", "10001"]

FACTS = [
    ("role", "financial-data backends, built with AI agents"),
    ("school", "HKU · Data Science & Engineering · Hong Kong"),
    ("method", "rules compute · model judges · human owns the doubt"),
    ("agents", "Claude Code · skills · hooks · subagents · evals"),
    ("stack", "Python FastAPI TypeScript Next.js Supabase Docker"),
    ("writing", "inpilot.dev"),
]

CARDS = [  # (file, kicker, title, lines, metric, metric_label, tags)
    ("mandate", "HacKU 2026 · team of 4", "Mandate",
     ["A wallet that lets a shopping agent spend only", "inside rules the wallet itself enforces.",
      "My part: audit chain, verifier, Z3, evaluation."],
     "23/23", "attacks held in the attack lab", "Python · FastAPI · Z3 · Ed25519"),
    ("ledger-exceptions", "public", "ledger-exceptions",
     ["Break triage for an event-sourced trading ledger.", "15 rules find breaks, an LLM only triages,",
      "code decides escalation (confidence < 0.75)."],
     "15/15", "breaks found, 0 false positives", "Python · Claude · Ollama"),
    ("prompt-forge", "public · v2.6", "prompt-forge",
     ["Claude Code skills that score, rewrite and run", "rough prompts from a shared pattern library,",
      "with a safety gate before anything runs."],
     "4", "skills sharing one pattern library", "Claude Code skills · Python"),
    ("reviewPaper", "public", "reviewPaper",
     ["A tutor over 9 electron-microscopy review papers", "that answers with citations. CI runs a",
      "gold-set eval gate and prompt-injection tests."],
     "19/21", "self-found gaps fixed (docs/)", "FastAPI · Claude API · Docker"),
    ("seungbin-dev", "public · inpilot.dev", "seungbin-dev",
     ["The pipeline behind my blog: draft, LLM grader,", "human review, publish. The grader checks",
      "20 voice rules; no grader means FAIL."],
     "15", "GitHub Actions workflows", "Next.js · MDX · GitHub Actions"),
    ("research", "public · Claude Code + Codex plugin", "Research · verify",
     ["Opens the source of every cited sentence and checks", "the sentence is really there. Verified, not",
      "supported, couldn't check: never mixed."],
     "250", "tests passing", "Python stdlib · hooks · subagents"),
]

REDUCED = ("@media (prefers-reduced-motion: reduce){*{animation:none!important;opacity:1!important;"
           "clip-path:none!important;stroke-dashoffset:0!important}.pulse{display:none}}")


def svg(w, h, body, style="", label=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{escape(label)}"><style>{style}{REDUCED}</style>{body}</svg>\n')


def hero(t):
    w, h = 900, 330
    parts = [f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="14" fill="{t["card"]}" stroke="{t["line"]}"/>',
             *(f'<circle cx="{26+i*20}" cy="24" r="6" fill="{c}"/>' for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"])),
             f'<text x="{w/2}" y="29" fill="{t["mute"]}" font-size="13" text-anchor="middle">seungbin@inpilot-dev: ~</text>',
             f'<line x1="1" y1="46" x2="{w-1}" y2="46" stroke="{t["line"]}"/>']
    # identicon, cells pop in one by one
    cell, ox, oy, k = 36, 44, 92, 0
    for r, row in enumerate(IDENTICON):
        for c, v in enumerate(row):
            if v == "1":
                parts.append(f'<rect class="px" style="animation-delay:{0.15+k*0.07:.2f}s" x="{ox+c*cell}" y="{oy+r*cell}" '
                             f'width="{cell-3}" height="{cell-3}" rx="3" fill="{t["acc"]}"/>')
                k += 1
    parts.append(f'<rect x="{ox-10}" y="{oy-10}" width="{cell*5+17}" height="{cell*5+17}" rx="10" fill="none" stroke="{t["line"]}"/>')
    x = 290
    parts.append(f'<text x="{x}" y="86" font-size="16"><tspan fill="{t["acc"]}">$</tspan>'
                 f'<tspan fill="{t["fg"]}" class="type"> whoami</tspan></text>')
    parts.append(f'<g class="ln" style="animation-delay:.9s"><text x="{x}" y="120" font-size="22" font-weight="700" fill="{t["fg"]}">'
                 f'Seungbin Min</text><text x="{x+170}" y="120" font-size="14" fill="{t["mute"]}">@inpilot-dev</text></g>')
    parts.append(f'<line class="ln" style="animation-delay:1s" x1="{x}" y1="134" x2="{w-40}" y2="134" stroke="{t["line"]}" stroke-dasharray="4 4"/>')
    for i, (k_, v) in enumerate(FACTS):
        y = 162 + i * 26
        val = escape(v)
        if k_ == "method":
            val = val.replace("judges", f'<tspan fill="{t["acc2"]}">judges</tspan>').replace(
                "compute", f'<tspan fill="{t["acc"]}">compute</tspan>')
        parts.append(f'<text class="ln" style="animation-delay:{1.1+i*0.12:.2f}s" x="{x}" y="{y}" font-size="15">'
                     f'<tspan fill="{t["acc"]}">{k_:<8}</tspan><tspan fill="{t["fg"]}" xml:space="preserve"> {val}</tspan></text>')
    parts.append(f'<rect class="cur" x="{x}" y="{162+len(FACTS)*26-14}" width="9" height="17" fill="{t["acc"]}"/>')
    style = (f"text{{font-family:{MONO};white-space:pre}}"
             ".px{opacity:0;animation:pop .35s ease-out forwards;transform-box:fill-box;transform-origin:center}"
             "@keyframes pop{from{opacity:0;transform:scale(.4)}to{opacity:1;transform:scale(1)}}"
             ".type{clip-path:inset(0 100% 0 0);animation:type .6s steps(7) .2s forwards}"
             "@keyframes type{to{clip-path:inset(0 0 0 0)}}"
             ".ln{opacity:0;animation:fade .4s ease-out forwards}@keyframes fade{to{opacity:1}}"
             ".cur{opacity:0;animation:fade .1s 1.9s forwards,blink 1.1s 2s step-end infinite}"
             "@keyframes blink{50%{opacity:0}}")
    return svg(w, h, "".join(parts), style, "Seungbin Min — financial-data backends built with AI agents. "
               + " · ".join(f"{a}: {b}" for a, b in FACTS))


def card(t, kicker, title, lines, metric, mlabel, tags):
    w, h = 600, 300
    p = [f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="14" fill="{t["card"]}" stroke="{t["line"]}"/>',
         f'<rect x="1" y="1" width="6" height="{h-2}" rx="3" fill="{t["acc"]}"/>',
         f'<text x="32" y="42" font-family="{MONO}" font-size="13" fill="{t["mute"]}">{escape(kicker)}</text>',
         f'<text x="32" y="78" font-family="{SANS}" font-size="28" font-weight="700" fill="{t["fg"]}">{escape(title)}</text>']
    p += [f'<text x="32" y="{112+i*24}" font-family="{SANS}" font-size="16" fill="{t["mute"]}">{escape(s)}</text>'
          for i, s in enumerate(lines)]
    p += [f'<line x1="32" y1="196" x2="{w-32}" y2="196" stroke="{t["line"]}"/>',
          f'<text x="32" y="250" font-family="{MONO}" font-size="44" font-weight="700" fill="{t["acc"]}">{escape(metric)}</text>',
          f'<text x="{40+len(metric)*27}" y="236" font-family="{SANS}" font-size="15" fill="{t["fg"]}">{escape(mlabel)}</text>',
          f'<text x="{40+len(metric)*27}" y="258" font-family="{MONO}" font-size="12" fill="{t["mute"]}">{escape(tags)}</text>']
    return svg(w, h, "".join(p), label=f"{title} — {' '.join(lines)} {metric} {mlabel}")


def flow(t):
    w, h = 900, 210
    nodes = [("Grill", "questions until", "the spec is clear"), ("Spec", "", ""), ("Tickets", "", ""),
             ("Subagent", "one per ticket", "test first"), ("Gate", "tests · evals", ""), ("Human", "review", "")]
    xs = [70, 205, 325, 470, 640, 800]
    y = 95
    p, d = [], 0.0
    for i, ((name, s1, s2), x) in enumerate(zip(nodes, xs)):
        if i:
            x0 = xs[i-1] + (58 if i-1 in (0, 3) else 42)
            x1 = x - (58 if i in (0, 3) else 42) - 6
            p.append(f'<line class="draw" style="animation-delay:{d:.2f}s" x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" '
                     f'stroke="{t["mute"]}" stroke-width="2" marker-end="url(#a)" pathLength="1"/>')
            d += 0.25
        if name == "Gate":
            shape = f'<path d="M{x} {y-42} L{x+46} {y} L{x} {y+42} L{x-46} {y} Z" fill="{t["dim"]}" stroke="{t["acc"]}" stroke-width="2"/>'
        else:
            hw = 58 if i in (0, 3) else 42
            stroke = t["acc2"] if name == "Human" else t["line"]
            shape = f'<rect x="{x-hw}" y="{y-28}" width="{hw*2}" height="56" rx="10" fill="{t["card"]}" stroke="{stroke}" stroke-width="2"/>'
        sub = "".join(f'<text x="{x}" y="{y+52+j*16}" class="s">{escape(s)}</text>' for j, s in enumerate((s1, s2)) if s)
        p.append(f'<g class="node" style="animation-delay:{d:.2f}s">{shape}<text x="{x}" y="{y+5}" class="n">{name}</text>{sub}</g>')
        d += 0.2
    # fail loop: gate back to subagent
    p.append(f'<path class="draw" style="animation-delay:{d:.2f}s" d="M640 53 C 640 18, 470 18, 470 60" fill="none" '
             f'stroke="{t["warn"]}" stroke-width="2" stroke-dasharray="1" marker-end="url(#b)" pathLength="1"/>')
    p.append(f'<text class="node" style="animation-delay:{d:.2f}s" x="555" y="22" text-anchor="middle" '
             f'font-family="{MONO}" font-size="12" fill="{t["warn"]}">fail → back to the subagent</text>')
    p.append(f'<circle class="pulse" r="5" fill="{t["acc"]}"><animateMotion dur="3.2s" begin="{d+0.6:.1f}s" '
             f'repeatCount="indefinite" path="M128 {y} L752 {y}"/></circle>')
    defs = (f'<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0 0L10 5L0 10z" fill="{t["mute"]}"/></marker>'
            f'<marker id="b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0 0L10 5L0 10z" fill="{t["warn"]}"/></marker></defs>')
    style = (f".n{{font-family:{SANS};font-size:15px;font-weight:600;fill:{t['fg']};text-anchor:middle}}"
             f".s{{font-family:{MONO};font-size:11px;fill:{t['mute']};text-anchor:middle}}"
             ".node{opacity:0;animation:fade .4s ease-out forwards}@keyframes fade{to{opacity:1}}"
             ".draw{opacity:0;stroke-dasharray:1;stroke-dashoffset:1;animation:draw .35s ease-out forwards}"
             "@keyframes draw{1%{opacity:1}to{opacity:1;stroke-dashoffset:0}}"
             f".pulse{{opacity:0;animation:fade .2s {d+0.6:.1f}s forwards}}")
    return svg(w, h, defs + "".join(p), style,
               "How I work with agents: grill until the spec is clear, spec, tickets, one fresh subagent per ticket "
               "writing tests first, a gate of tests and evals (fail goes back to the subagent), then human review.")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, t in THEMES.items():
        (OUT / f"hero-{name}.svg").write_text(hero(t))
        (OUT / f"flow-{name}.svg").write_text(flow(t))
        for c in CARDS:
            (OUT / f"card-{c[0]}-{name}.svg").write_text(card(t, *c[1:]))
    print(f"wrote {len(list(OUT.glob('*.svg')))} files to {OUT}")
