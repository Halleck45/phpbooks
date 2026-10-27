#!/usr/bin/env python3
"""Turn a built mdBook into an EPUB 3.

Reads the chapters mdBook already rendered (so includes, inline SVG charts and
raw HTML are resolved), in SUMMARY.md order, and hands them to pandoc as one
HTML document. Illustrations are shrunk to JPEG, since the web PNGs would make
a 100 MB book, and images missing from the build are dropped. Sub-chapters are demoted one heading level per nesting level so
the EPUB table of contents keeps the book's hierarchy. Ids are prefixed with
the chapter name, and links between chapters are rewritten to those ids.

    build-epub.py <book dir> <src dir> <html dir> <output.epub>

Example, from a book folder: ../scripts/build-epub.py . fr book-fr book-fr.epub
"""

import html
import re
import subprocess
import sys
import tempfile
import tomllib
import uuid
from pathlib import Path

from bs4 import BeautifulSoup
from PIL import Image

SUMMARY_ENTRY = re.compile(r"^(\s*)([-*]\s+)?\[(.*?)\]\((.*?)\)")
EMOJI = re.compile(r"[\U0001F000-\U0001FFFF☀-➿]\s*")
VERSION = re.compile(r"\s+-\s+\d+(\.\d+)*$")
CSS = Path(__file__).with_name("epub.css")
IMAGE_WIDTH = 1200


def chapters(summary):
    """Yield (html name, depth) for every linked entry of SUMMARY.md."""
    for line in summary.read_text().splitlines():
        m = SUMMARY_ENTRY.match(line)
        if not m or not m.group(4):
            continue
        depth = len(m.group(1).expandtabs(4)) // 2 if m.group(2) else 0
        name = Path(m.group(4)).with_suffix(".html").as_posix()
        if Path(name).name == "README.html":
            name = str(Path(name).with_name("index.html"))
        yield name, depth


def slug(name):
    return re.sub(r"[^A-Za-z0-9_-]", "-", name.removesuffix(".html"))


def shrink(image, out_dir):
    """Return a JPEG copy of a raster image, at most IMAGE_WIDTH pixels wide."""
    if image.suffix.lower() not in (".png", ".jpg", ".jpeg"):
        return image
    out = out_dir / (slug(image.relative_to(image.anchor).as_posix()) + ".jpg")
    if not out.exists():
        with Image.open(image) as im:
            im = im.convert("RGB")
            im.thumbnail((IMAGE_WIDTH, IMAGE_WIDTH))
            im.save(out, quality=80, optimize=True, progressive=True)
    return out


def chapter_body(page, name, depth, first_ids, image_dir):
    soup = BeautifulSoup(page.read_text(), "html.parser")
    main = soup.find("main")
    for tag in main.find_all(["script", "button", "nav"]):
        tag.decompose()
    for a in main.select("a.header"):
        a.unwrap()

    prefix = slug(name)
    for tag in main.find_all(id=True):
        tag["id"] = f"{prefix}--{tag['id']}"
    first = main.find(re.compile(r"^h[1-6]$"))
    if first is not None:
        first["id"] = prefix

    for a in main.find_all("a", href=True):
        href = a["href"]
        if re.match(r"^[a-z][a-z0-9+.-]*:", href):
            continue
        target, _, frag = href.partition("#")
        target = slug(target) if target else prefix
        if frag and first_ids.get(target) != frag:
            a["href"] = f"#{target}--{frag}"
        else:
            a["href"] = f"#{target}"

    for img in main.find_all("img", src=True):
        if re.match(r"^[a-z][a-z0-9+.-]*:", img["src"]):
            continue
        image = page.parent / img["src"]
        if image.exists():
            img["src"] = str(shrink(image, image_dir))
        else:
            print(f"{page.name}: dropping missing image {img['src']}", file=sys.stderr)
            img.decompose()

    for h in main.find_all(re.compile(r"^h[1-6]$")):
        h.name = f"h{min(int(h.name[1]) + depth, 6)}"
    return main.decode_contents()


def first_heading_id(page):
    m = re.search(r"<main>.*?<h[1-6] id=\"([^\"]+)\"", page.read_text(), re.S)
    return m.group(1) if m else None


def book_title(html_dir, fallback):
    m = re.search(r"<title>(.*?)</title>", (html_dir / "print.html").read_text(), re.S)
    title = html.unescape(m.group(1)) if m else fallback
    return VERSION.sub("", EMOJI.sub("", title)).strip()


def main(book_dir, src_dir, html_dir, output):
    book_dir = Path(book_dir)
    src_dir = book_dir / src_dir
    html_dir = book_dir / html_dir
    config = tomllib.loads((book_dir / "book.toml").read_text())["book"]
    language = "fr" if src_dir.name == "fr" else config.get("language", "en")
    title = book_title(html_dir, config["title"])

    entries = [(n, d) for n, d in chapters(src_dir / "SUMMARY.md") if (html_dir / n).exists()]
    first_ids = {slug(n): first_heading_id(html_dir / n) for n, _ in entries}

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        body = "\n".join(chapter_body(html_dir / n, n, d, first_ids, tmp) for n, d in entries)
        document = tmp / "book.html"
        document.write_text(f'<!DOCTYPE html>\n<html lang="{language}"><head><meta charset="utf-8"><title>{html.escape(title)}</title></head><body>\n{body}\n</body></html>')

        cmd = [
            "pandoc", "--from=html", "--to=epub3",
            f"--metadata=title:{title}", f"--metadata=lang:{language}",
            # A stable identifier lets e-readers replace the book on update instead of adding a copy.
            f"--metadata=identifier:urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, f'phpbook/{book_dir.resolve().name}/{language}')}",
            f"--resource-path={html_dir}", "--split-level=1", "--toc-depth=2",
            f"--css={CSS}", f"--output={Path(output).resolve()}",
        ]
        cmd += [f"--metadata=author:{a}" for a in config.get("authors", [])]
        if config.get("description") and language == config.get("language", "en"):
            cmd.append(f"--metadata=description:{config['description']}")
        cover = src_dir / "images" / "ch00-cover.png"
        if cover.exists():
            cmd.append(f"--epub-cover-image={shrink(cover, tmp)}")
        subprocess.run(cmd + [str(document)], check=True)
    print(f"{output}: {len(entries)} chapters")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    main(*sys.argv[1:])
