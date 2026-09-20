#!/usr/bin/env python3
"""Generate the SVG charts of "PHP in 2026, the Facts" from charts/data/*.json.

Every data file describes one chart and carries the source of its figures.
The script writes src/charts/<name>.svg (English labels) and
fr/charts/<name>.svg (French labels). Chapters include a chart with
{{#include charts/<name>.svg}}, so the SVG is inlined by mdBook and its text
follows the page theme through currentColor.

Data file format (JSON):

  {
    "type": "hbar" | "line" | "stacked" | "timeline",
    "title": {"en": "...", "fr": "..."},
    "source": {"en": "W3Techs, 1 September 2026", "fr": "W3Techs, 1er septembre 2026"},
    "note": {"en": "optional footnote", "fr": "..."},          # optional
    "unit": "%",                                                # optional, appended to values
    "highlight": ["PHP"],                                       # rows/series drawn in blue
    ... type-specific fields, see each renderer below ...
  }

Only the standard library is used.
"""

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "charts" / "data"
OUT = {"en": ROOT / "src" / "charts", "fr": ROOT / "fr" / "charts"}

BLUE = "#2a78d6"      # the one accent: PHP, or the highlighted series
GREY = "#a5a49f"      # everything else
LIGHT = "#d6d5d0"     # grid, spacers
FONT = "font-family: 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
FONT_MONO = "font-family: 'Source Code Pro', Menlo, monospace"


def esc(text):
    return (str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def label(value, lang):
    if isinstance(value, dict):
        return value.get(lang) or value.get("en") or ""
    return str(value)


def fmt(value, unit, lang):
    if isinstance(value, float) and not value.is_integer():
        text = f"{value:.1f}"
    else:
        text = f"{int(value):,}"
    if lang == "fr":
        text = text.replace(",", " ").replace(".", ",")
    return f"{text}{unit}"


class Svg:
    def __init__(self, width, height, title, desc):
        self.w, self.h = width, height
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" role="img" aria-labelledby="t d" '
            f'style="max-width: 100%; height: auto; {FONT}; font-size: 13px;">',
            f'<title id="t">{esc(title)}</title>',
            f'<desc id="d">{esc(desc)}</desc>',
        ]

    def text(self, x, y, s, size=13, anchor="start", weight="normal", opacity=1, mono=False):
        style = f"font-size: {size}px; font-weight: {weight};" + (f" {FONT_MONO};" if mono else "")
        self.parts.append(
            f'<text x="{x:.1f}" y="{y:.1f}" fill="currentColor" fill-opacity="{opacity}" '
            f'text-anchor="{anchor}" style="{style}">{esc(s)}</text>'
        )

    def rect(self, x, y, w, h, fill, rx=0, opacity=1):
        self.parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'rx="{rx}" fill="{fill}" fill-opacity="{opacity}"/>'
        )

    def line(self, x1, y1, x2, y2, stroke="currentColor", width=1, opacity=0.25, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{width}" stroke-opacity="{opacity}"{d}/>'
        )

    def path(self, points, stroke, width=2):
        d = " ".join(("M" if i == 0 else "L") + f"{x:.1f},{y:.1f}" for i, (x, y) in enumerate(points))
        self.parts.append(
            f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{width}" '
            f'stroke-linejoin="round" stroke-linecap="round"/>'
        )

    def circle(self, x, y, r, fill):
        self.parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}"/>')

    def footer(self, y, source, note):
        lines = wrap(source) + (wrap(note) if note else [])
        for i, line in enumerate(lines):
            self.text(0, y + 15 * i, line, size=11, opacity=0.65)

    @staticmethod
    def footer_lines(source, note):
        return len(wrap(source)) + (len(wrap(note)) if note else 0)

    def render(self):
        return "\n".join(self.parts + ["</svg>"])


def nice_step(span):
    """A tick step of 1, 2, 2.5 or 5 times a power of ten giving four to six ticks."""
    rough = span / 5
    mag = 10 ** math.floor(math.log10(rough)) if rough > 0 else 1
    for m in (1, 2, 2.5, 5, 10):
        if rough <= m * mag:
            return m * mag
    return 10 * mag


def spread(items, gap, top=None, bottom=None):
    """items = [(y, payload)]; pushes y values apart by at least gap, keeping order, inside [top, bottom].
    Only the labels that collide move; the others stay next to their mark."""
    items = sorted(items, key=lambda t: t[0])
    ys = [y for y, _ in items]
    for i in range(1, len(ys)):
        if ys[i] - ys[i - 1] < gap:
            ys[i] = ys[i - 1] + gap
    if bottom is not None:
        for i in range(len(ys) - 1, -1, -1):
            limit = bottom if i == len(ys) - 1 else ys[i + 1] - gap
            if ys[i] > limit:
                ys[i] = limit
    if top is not None:
        for i in range(len(ys)):
            limit = top if i == 0 else ys[i - 1] + gap
            if ys[i] < limit:
                ys[i] = limit
    return [(y, payload) for y, (_, payload) in zip(ys, items)]


def wrap(text, width=100):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


def footer_h(spec, lang):
    return 15 * Svg.footer_lines(label(spec["source"], lang), label(spec.get("note", ""), lang))


def hbar(spec, lang):
    """Horizontal bars, one per row: rows = [{"label": {...}, "value": n}, ...]."""
    unit = spec.get("unit", "")
    rows = spec["rows"]
    highlight = set(spec.get("highlight", []))
    width = 640
    left = max(150, 14 + int(6.8 * max(len(label(r["label"], lang)) for r in rows)))
    bar_h, gap, top = 20, 8, 44
    fh = footer_h(spec, lang)
    height = top + len(rows) * (bar_h + gap) + 30 + fh
    svg = Svg(width, height, label(spec["title"], lang), label(spec.get("desc", spec["title"]), lang))
    svg.text(0, 18, label(spec["title"], lang), size=15, weight="bold")
    vmax = spec.get("max") or max(r["value"] for r in rows)
    scale = (width - left - 70) / vmax
    for i, row in enumerate(rows):
        y = top + i * (bar_h + gap)
        key = row.get("key", label(row["label"], "en"))
        color = BLUE if key in highlight else GREY
        svg.text(left - 10, y + bar_h - 5, label(row["label"], lang), anchor="end")
        svg.rect(left, y, max(row["value"] * scale, 1), bar_h, color, rx=3)
        svg.text(left + row["value"] * scale + 8, y + bar_h - 5, fmt(row["value"], unit, lang), size=12, opacity=0.85)
    svg.line(left, top - 4, left, top + len(rows) * (bar_h + gap) - gap + 4, opacity=0.4)
    svg.footer(height - fh + 4, label(spec["source"], lang), label(spec.get("note", ""), lang))
    return svg.render()


def line(spec, lang):
    """Lines over time: x = [...], series = [{"key", "label", "values": [...]}]."""
    unit = spec.get("unit", "")
    xs = spec["x"]
    series = spec["series"]
    highlight = set(spec.get("highlight", []))
    fh = footer_h(spec, lang)
    width, height = 640, 290 + fh
    longest = max(len(f'{label(s_["label"], lang)} ({fmt([v for v in s_["values"] if v is not None][-1], unit, lang)})') for s_ in series)
    left, right, top, bottom = 50, max(130, 16 + int(6.6 * longest)), 44, 40 + fh
    plot_w, plot_h = width - left - right, height - top - bottom
    svg = Svg(width, height, label(spec["title"], lang), label(spec.get("desc", spec["title"]), lang))
    svg.text(0, 18, label(spec["title"], lang), size=15, weight="bold")
    raw_max = max(v for s in series for v in s["values"] if v is not None)
    vmin = spec.get("min", 0)
    step = nice_step((spec.get("max") or raw_max) - vmin)
    vmax = spec.get("max") or math.ceil(raw_max / step) * step
    ticks = spec.get("ticks") or [vmin + step * k for k in range(int(round((vmax - vmin) / step)) + 1)]
    def X(i): return left + plot_w * i / (len(xs) - 1)
    def Y(v): return top + plot_h - plot_h * (v - vmin) / (vmax - vmin)
    for t in ticks:
        svg.line(left, Y(t), left + plot_w, Y(t), opacity=0.15)
        svg.text(left - 8, Y(t) + 4, fmt(t, unit, lang), size=11, anchor="end", opacity=0.7)
    for i, x in enumerate(xs):
        svg.text(X(i), top + plot_h + 18, str(x), size=11, anchor="middle", opacity=0.7)
    ends = []
    for s in series:
        color = BLUE if s["key"] in highlight else GREY
        pts = [(X(i), Y(v)) for i, v in enumerate(s["values"]) if v is not None]
        svg.path(pts, color, width=2.5 if color == BLUE else 2)
        for p in pts:
            svg.circle(p[0], p[1], 3.5, color)
        last = [v for v in s["values"] if v is not None][-1]
        ends.append((pts[-1][1], (f'{label(s["label"], lang)} ({fmt(last, unit, lang)})', color)))
    for ly, (text, color) in spread(ends, 15, top=top + 6, bottom=top + plot_h + 2):
        svg.text(left + plot_w + 10, ly + 4, text, size=12,
                 weight="bold" if color == BLUE else "normal", opacity=1 if color == BLUE else 0.8)
    svg.footer(height - fh + 4, label(spec["source"], lang), label(spec.get("note", ""), lang))
    return svg.render()


def stacked(spec, lang):
    """One 100% bar per row: rows = [{"label", "parts": [{"key","label","value"}]}]."""
    unit = spec.get("unit", "%")
    rows = spec["rows"]
    highlight = set(spec.get("highlight", []))
    width, left = 640, spec.get("left", 200)
    bar_h, gap, top = 26, 14, 44
    fh = footer_h(spec, lang)
    height = top + len(rows) * (bar_h + gap) + 50 + fh
    svg = Svg(width, height, label(spec["title"], lang), label(spec.get("desc", spec["title"]), lang))
    svg.text(0, 18, label(spec["title"], lang), size=15, weight="bold")
    plot_w = width - left - 20
    shades = ["#2a78d6", "#5598e7", "#86b6ef", "#b7d3f6"]
    greys = ["#8b8a85", "#a5a49f", "#c1c0bb", "#d6d5d0"]
    legend = {}
    for i, row in enumerate(rows):
        y = top + i * (bar_h + gap)
        svg.text(left - 10, y + bar_h - 8, label(row["label"], lang), anchor="end")
        x = left
        total = sum(p["value"] for p in row["parts"]) or 1
        hi, lo = 0, 0
        for p in row["parts"]:
            w = plot_w * p["value"] / total
            if p["key"] in highlight:
                color = shades[min(hi, 3)]; hi += 1
            else:
                color = greys[min(lo, 3)]; lo += 1
            legend.setdefault(p["key"], (label(p["label"], lang), color))
            svg.rect(x, y, max(w - 2, 0), bar_h, color, rx=2)
            if w > 44:
                svg.text(x + w / 2 - 1, y + bar_h - 8, fmt(p["value"], unit, lang), size=11, anchor="middle",
                         opacity=1)
            x += w
    ly = top + len(rows) * (bar_h + gap) + 8
    lx = left
    for key, (name, color) in legend.items():
        svg.rect(lx, ly, 12, 12, color, rx=2)
        svg.text(lx + 17, ly + 10, name, size=12, opacity=0.85)
        lx += 17 + 7.5 * len(name) + 22
        if lx > width - 80:
            lx, ly = left, ly + 20
    svg.footer(height - fh + 4, label(spec["source"], lang), label(spec.get("note", ""), lang))
    return svg.render()


def timeline(spec, lang):
    """Support windows: rows = [{"label", "start": "YYYY-MM", "active": "YYYY-MM", "end": "YYYY-MM"}]."""
    rows = spec["rows"]
    highlight = set(spec.get("highlight", []))
    width = 640
    left = max(90, 14 + int(8 * max(len(label(r["label"], lang)) for r in rows)))
    bar_h, gap, top = 18, 10, 44
    fh = footer_h(spec, lang)
    height = top + len(rows) * (bar_h + gap) + 70 + fh
    svg = Svg(width, height, label(spec["title"], lang), label(spec.get("desc", spec["title"]), lang))
    svg.text(0, 18, label(spec["title"], lang), size=15, weight="bold")
    def ym(s):
        y, m = s.split("-"); return int(y) + (int(m) - 1) / 12
    t0, t1 = ym(spec["from"]), ym(spec["to"])
    plot_w = width - left - 20
    def X(t): return left + plot_w * (t - t0) / (t1 - t0)
    for year in range(math.ceil(t0), math.floor(t1) + 1):
        svg.line(X(year), top - 6, X(year), top + len(rows) * (bar_h + gap), opacity=0.12)
        svg.text(X(year), top + len(rows) * (bar_h + gap) + 14, str(year), size=11, anchor="middle", opacity=0.7)
    if spec.get("today"):
        svg.line(X(ym(spec["today"])), top - 10, X(ym(spec["today"])), top + len(rows) * (bar_h + gap), stroke=BLUE,
                 width=1.5, opacity=0.9, dash="4 3")
        svg.text(X(ym(spec["today"])), top - 14, label(spec.get("today_label", "today"), lang), size=11,
                 anchor="middle", opacity=0.8)
    for i, row in enumerate(rows):
        y = top + i * (bar_h + gap)
        color = BLUE if row.get("key", label(row["label"], "en")) in highlight else GREY
        svg.text(left - 10, y + bar_h - 5, label(row["label"], lang), anchor="end", mono=True)
        a, b, c = X(ym(row["start"])), X(ym(row["active"])), X(ym(row["end"]))
        svg.rect(a, y, b - a, bar_h, color, rx=3)
        svg.rect(b, y, c - b, bar_h, color, rx=3, opacity=0.35)
    ly = top + len(rows) * (bar_h + gap) + 34
    svg.rect(left, ly, 12, 12, GREY, rx=2)
    first = label(spec["legend_active"], lang)
    svg.text(left + 17, ly + 10, first, size=12, opacity=0.85)
    lx2 = left + 17 + int(6.6 * len(first)) + 24
    svg.rect(lx2, ly, 12, 12, GREY, rx=2, opacity=0.35)
    svg.text(lx2 + 17, ly + 10, label(spec["legend_security"], lang), size=12, opacity=0.85)
    svg.footer(height - fh + 4, label(spec["source"], lang), label(spec.get("note", ""), lang))
    return svg.render()


RENDERERS = {"hbar": hbar, "line": line, "stacked": stacked, "timeline": timeline}


def main(names):
    files = sorted(DATA.glob("*.json"))
    if names:
        files = [f for f in files if f.stem in names]
    if not files:
        print("no data file found", file=sys.stderr)
        return 1
    for f in files:
        spec = json.loads(f.read_text(encoding="utf-8"))
        if "source" not in spec:
            print(f"{f.name}: missing 'source' field, refusing to draw an unsourced chart", file=sys.stderr)
            return 1
        render = RENDERERS[spec["type"]]
        for lang, out in OUT.items():
            out.mkdir(parents=True, exist_ok=True)
            (out / f"{f.stem}.svg").write_text(render(spec, lang) + "\n", encoding="utf-8")
        print(f"ok    {f.stem}.svg")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
