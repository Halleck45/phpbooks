#!/usr/bin/env python3
"""Generate the book's SVG charts from charts/data/*.json.

One chart shows one thing. PHP is always the one hue (blue); everything
else is neutral grey. Text and axes use currentColor so a chart reads in
both the light and the dark theme. Every chart carries its source line.
This script has no dependencies beyond the standard library, on purpose:
a chart here is a small, auditable SVG string, not a rendered plot.
"""
import json
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
OUT_DIR = Path(__file__).parent

BLUE = "#3b82f6"
GREY = "#94a3b8"
WIDTH = 640
FONT = "font-family=\"system-ui, -apple-system, Segoe UI, sans-serif\""


def esc(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def hbar(data):
    rows = data["series"]
    max_value = max(r["value"] for r in rows)
    row_h = 34
    top_pad = 34
    bottom_pad = 34
    height = top_pad + len(rows) * row_h + bottom_pad
    label_w = 150
    bar_area = WIDTH - label_w - 70
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" role="img" aria-label="{esc(data.get("title",""))}">',
        f'<title>{esc(data.get("title",""))}</title>',
    ]
    if data.get("title"):
        out.append(
            f'<text x="0" y="20" {FONT} font-size="14" font-weight="600">{esc(data["title"])}</text>'
        )
    for i, row in enumerate(rows):
        y = top_pad + i * row_h
        bar_w = (row["value"] / max_value) * bar_area if max_value else 0
        color = BLUE if row.get("highlight") else GREY
        out.append(
            f'<text x="0" y="{y + 16}" {FONT} font-size="13">{esc(row["label"])}</text>'
        )
        out.append(
            f'<rect x="{label_w}" y="{y + 4}" width="{bar_w:.1f}" height="16" fill="{color}" />'
        )
        out.append(
            f'<text x="{label_w + bar_w + 8:.1f}" y="{y + 16}" {FONT} font-size="13">{esc(row["value_label"])}</text>'
        )
    src_y = height - 12
    out.append(
        f'<text x="0" y="{src_y}" {FONT} font-size="11" fill-opacity="0.65">{esc(data.get("source",""))}</text>'
    )
    out.append("</svg>")
    return "\n".join(out)


def stacked(data):
    rows = data["series"]
    total = sum(r["value"] for r in rows)
    bar_h = 40
    top_pad = 34
    height = top_pad + bar_h + 70
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" role="img" aria-label="{esc(data.get("title",""))}">',
        f'<title>{esc(data.get("title",""))}</title>',
    ]
    if data.get("title"):
        out.append(
            f'<text x="0" y="20" {FONT} font-size="14" font-weight="600">{esc(data["title"])}</text>'
        )
    x = 0
    greys = ["#94a3b8", "#cbd5e1", "#64748b", "#e2e8f0"]
    grey_i = 0
    legend_y = top_pad + bar_h + 24
    legend_x = 0
    for row in rows:
        w = (row["value"] / total) * WIDTH if total else 0
        if row.get("highlight"):
            color = BLUE
        else:
            color = greys[grey_i % len(greys)]
            grey_i += 1
        out.append(
            f'<rect x="{x:.1f}" y="{top_pad}" width="{w:.1f}" height="{bar_h}" fill="{color}" />'
        )
        out.append(
            f'<rect x="{legend_x}" y="{legend_y}" width="10" height="10" fill="{color}" />'
        )
        out.append(
            f'<text x="{legend_x + 15}" y="{legend_y + 10}" {FONT} font-size="12">{esc(row["label"])} ({esc(row["value_label"])})</text>'
        )
        legend_y += 18
        x += w
    src_y = legend_y + 14
    out.append(
        f'<text x="0" y="{src_y}" {FONT} font-size="11" fill-opacity="0.65">{esc(data.get("source",""))}</text>'
    )
    out[0] = out[0].replace(f'0 {height}"', f'0 {src_y + 10}"')
    out.append("</svg>")
    return "\n".join(out)


def grouped(data):
    groups = data["series"]
    max_value = max(v["value"] for g in groups for v in g["values"])
    group_h = 60
    top_pad = 34
    bottom_pad = 34
    height = top_pad + len(groups) * group_h + bottom_pad
    label_w = 110
    bar_area = WIDTH - label_w - 90
    bar_h = 16
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" role="img" aria-label="{esc(data.get("title",""))}">',
        f'<title>{esc(data.get("title",""))}</title>',
    ]
    if data.get("title"):
        out.append(
            f'<text x="0" y="20" {FONT} font-size="14" font-weight="600">{esc(data["title"])}</text>'
        )
    for gi, g in enumerate(groups):
        gy = top_pad + gi * group_h
        out.append(
            f'<text x="0" y="{gy + 16}" {FONT} font-size="13">{esc(g["label"])}</text>'
        )
        for vi, v in enumerate(g["values"]):
            y = gy + vi * (bar_h + 6)
            bar_w = (v["value"] / max_value) * bar_area if max_value else 0
            color = BLUE if v.get("highlight") else GREY
            out.append(
                f'<rect x="{label_w}" y="{y}" width="{bar_w:.1f}" height="{bar_h}" fill="{color}" />'
            )
            out.append(
                f'<text x="{label_w + bar_w + 8:.1f}" y="{y + bar_h - 3}" {FONT} font-size="12">{esc(v["value_label"])}</text>'
            )
    src_y = height - 12
    out.append(
        f'<text x="0" y="{src_y}" {FONT} font-size="11" fill-opacity="0.65">{esc(data.get("source",""))}</text>'
    )
    out.append("</svg>")
    return "\n".join(out)


RENDERERS = {"hbar": hbar, "stacked": stacked, "grouped": grouped}


def main():
    files = sorted(DATA_DIR.glob("*.json"))
    if not files:
        print("No chart data files found in", DATA_DIR)
        return 1
    for f in files:
        data = json.loads(f.read_text())
        renderer = RENDERERS.get(data.get("type"))
        if not renderer:
            print(f"Skipping {f.name}: unknown type {data.get('type')}")
            continue
        svg = renderer(data)
        out_path = OUT_DIR / f.with_suffix(".svg").name
        out_path.write_text(svg)
        print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
