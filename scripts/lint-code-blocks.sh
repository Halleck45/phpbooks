#!/usr/bin/env bash
#
# Syntax-check every ```php code block found in the Markdown files of the
# given folders with `php -l`. Blocks that contain no opening tag at all get
# one prepended, so short fragments are checked too; blocks mixing HTML and
# PHP sections are checked as they are.
#
# Usage:
#   scripts/lint-code-blocks.sh [folder ...]     default: src
#
# Environment:
#   PHP   php binary to use, default: php. Point it at a newer build (or a
#         wrapper around `docker run php:8.5-cli`) to check code that uses
#         syntax your local PHP does not know yet.
#
# Exit status is 1 when at least one block fails.

set -euo pipefail

PHP="${PHP:-php}"
FOLDERS=("$@")
[ ${#FOLDERS[@]} -gt 0 ] || FOLDERS=(src)

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

failed=0
checked=0

for folder in "${FOLDERS[@]}"; do
    while IFS= read -r file; do
        # Split the file into numbered block files: <line>.php
        awk -v out="$TMP" -v name="$(basename "$file" .md)" '
            /^```php/ { in_block = 1; start = NR + 1; body = ""; next }
            /^```/ && in_block {
                in_block = 0
                path = out "/" name "." start ".php"
                # A fragment with no opening tag gets one; a block that mixes
                # HTML and <?php ... ?> sections is left as it is.
                if (body !~ /<\?(php|=)/) body = "<?php\n" body
                printf "%s", body > path
                close(path)
                next
            }
            in_block { body = body $0 "\n" }
        ' "$file"
        for block in "$TMP"/"$(basename "$file" .md)".*.php; do
            [ -e "$block" ] || continue
            checked=$((checked + 1))
            if ! msg="$("$PHP" -l "$block" 2>&1)"; then
                line="${block##*.md.}"; line="${block%.php}"; line="${line##*.}"
                echo "$file:$line: $(echo "$msg" | head -1 | sed 's/ in .*//')"
                failed=$((failed + 1))
            fi
            rm -f "$block"
        done
    done < <(find "$folder" -name '*.md' | sort)
done

echo "checked $checked block(s), $failed failure(s)"
[ "$failed" -eq 0 ]
