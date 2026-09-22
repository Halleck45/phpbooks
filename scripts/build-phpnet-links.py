#!/usr/bin/env python3
"""Generate <book>/theme/phpnet-links.js for every book.

The list of PHP built-in functions comes from the function index of the php.net
manual, so a name is only linked when its manual page exists. The script is
scripts/phpnet-links.src.js with that list injected.

Usage (from the repository root):
    python3 scripts/build-phpnet-links.py                 download the index
    python3 scripts/build-phpnet-links.py --index FILE    use a saved copy
    python3 scripts/build-phpnet-links.py --check         fail if a copy is stale
"""

import argparse
import html
import json
import pathlib
import re
import sys
import urllib.request

INDEX_URL = "https://www.php.net/manual/en/indexes.functions.php"
BOOKS = ["beginner", "polyglot", "pragmatic", "skeptic", "engineering"]
TARGET = "theme/phpnet-links.js"

# Documented as functions, but too generic to link safely: they are methods of
# PECL classes listed in the function index under a bare name.
EXCLUDED = {"expression", "getsession"}

ENTRY_RE = re.compile(r'<a href="function\.([a-z0-9-]+)\.php"[^>]*>([^<]+)</a>')
NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read_index(path):
    if path:
        return pathlib.Path(path).read_text(encoding="utf-8")
    request = urllib.request.Request(INDEX_URL, headers={"User-Agent": "phpbook-build"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def parse(source):
    """Return ({name: slug}) for every plain function of the index."""
    functions = {}
    for slug, label in ENTRY_RE.findall(source):
        name = html.unescape(label).strip().lower()
        # Namespaced PECL functions (UI\run, CommonMark\Parse) are skipped.
        if not NAME_RE.match(name) or name in EXCLUDED:
            continue
        functions[name] = slug
    return functions


def render(functions):
    names = sorted(functions)
    irregular = {n: s for n, s in functions.items() if n.replace("_", "-") != s}
    template = (ROOT / "scripts" / "phpnet-links.src.js").read_text(encoding="utf-8")
    return (
        template.replace("__NAMES__", " ".join(names))
        .replace("__SLUGS__", json.dumps(irregular, sort_keys=True))
        .replace("__SOURCE__", INDEX_URL)
        .replace("__COUNT__", str(len(names)))
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--index", help="saved copy of the php.net function index")
    parser.add_argument("--check", action="store_true", help="do not write, fail if a copy differs")
    args = parser.parse_args()

    functions = parse(read_index(args.index))
    if len(functions) < 3000:
        sys.exit(f"error: only {len(functions)} functions found, the index page probably changed")

    output = render(functions)
    stale = []
    for book in BOOKS:
        target = ROOT / book / TARGET
        if args.check:
            if not target.is_file() or target.read_text(encoding="utf-8") != output:
                stale.append(str(target.relative_to(ROOT)))
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output, encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)}")

    if stale:
        sys.exit("stale: " + ", ".join(stale) + " (run make phpnet-links)")
    print(f"{len(functions)} functions")


if __name__ == "__main__":
    main()
