#!/usr/bin/env bash
#
# Generate the book illustrations described in illustrations.md through the
# OpenAI Images API, and drop them into src/images/.
#
# Usage:
#   OPENAI_API_KEY=sk-... scripts/generate-illustrations.sh [options] [name ...]
#
#   name        illustration file name from illustrations.md, with or without
#               the .png extension (e.g. ch02-flowchart). Default: all of them.
#
# Options:
#   --force     regenerate images that already exist in src/images/
#   --dry-run   print the prompts that would be sent and exit, no API call
#   --list      list the illustrations with their priority and format
#   --must-have only generate the illustrations marked "must have"
#   -h, --help  show this help
#
# Environment:
#   OPENAI_API_KEY        required
#   OPENAI_IMAGE_MODEL    default: gpt-image-2.5-flare (gpt-image-2.5-sunburst favors editing precision)
#   OPENAI_IMAGE_QUALITY  low | medium | high | xhigh | max | auto, default: high
#
# Requires curl, jq and base64.
#
# The prompt sent for each image is the "Common style" block of
# illustrations.md followed by the illustration's own "**Prompt.**" paragraph.
# The "- Format:" line picks the size (landscape 1536x1024, portrait
# 1024x1536, square 1024x1024).

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPEC="$ROOT/illustrations.md"
OUT_DIR="$ROOT/src/images"
API_URL="https://api.openai.com/v1/images/generations"
MODEL="${OPENAI_IMAGE_MODEL:-gpt-image-2.5-flare}"
QUALITY="${OPENAI_IMAGE_QUALITY:-high}"

FORCE=0
DRY_RUN=0
LIST=0
MUST_HAVE=0
WANTED=()

usage() {
    sed -n '2,/^$/p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
}

while [ $# -gt 0 ]; do
    case "$1" in
        --force) FORCE=1 ;;
        --dry-run) DRY_RUN=1 ;;
        --list) LIST=1 ;;
        --must-have) MUST_HAVE=1 ;;
        -h|--help) usage; exit 0 ;;
        -*) echo "unknown option: $1" >&2; usage >&2; exit 2 ;;
        *) WANTED+=("${1%.png}") ;;
    esac
    shift
done

for tool in curl jq base64; do
    command -v "$tool" >/dev/null 2>&1 || { echo "missing required tool: $tool" >&2; exit 2; }
done
[ -f "$SPEC" ] || { echo "spec not found: $SPEC" >&2; exit 2; }

# The style block: every "> " line under the "## Common style" heading.
STYLE="$(awk '
    /^## Common style/ { in_style = 1; next }
    /^## / { in_style = 0 }
    in_style && /^> / { sub(/^> /, ""); print }
' "$SPEC")"
[ -n "$STYLE" ] || { echo "no common style block found in $SPEC" >&2; exit 2; }

# One TSV line per illustration: name, format, priority, prompt.
entries() {
    awk '
        function flush() {
            if (name != "") printf "%s\t%s\t%s\t%s\n", name, fmt, prio, prompt
            name = ""; fmt = "landscape"; prio = ""; prompt = ""
        }
        /^## .*\.png$/ { flush(); name = $2; sub(/\.png$/, "", name); next }
        /^- Format: /   { fmt = $3; sub(/\.$/, "", fmt); next }
        /^- Priority: / { prio = $0; sub(/^- Priority: /, "", prio); sub(/\..*$/, "", prio); next }
        /^\*\*Prompt\.\*\* / { prompt = $0; sub(/^\*\*Prompt\.\*\* /, "", prompt); gsub(/`/, "", prompt); next }
        END { flush() }
    ' "$SPEC"
}

size_for() {
    case "$1" in
        portrait) echo "1024x1536" ;;
        square) echo "1024x1024" ;;
        landscape) echo "1536x1024" ;;
        *) echo "unknown format '$1', using landscape" >&2; echo "1536x1024" ;;
    esac
}

format_hint() {
    case "$1" in
        portrait) echo "Portrait format, 2:3, read from top to bottom." ;;
        square) echo "Square format, 1:1." ;;
        *) echo "Landscape format, 3:2." ;;
    esac
}

wanted() {
    [ ${#WANTED[@]} -eq 0 ] && return 0
    local w
    for w in "${WANTED[@]}"; do [ "$w" = "$1" ] && return 0; done
    return 1
}

if [ "$LIST" -eq 1 ]; then
    entries | awk -F'\t' '{ printf "%-28s %-10s %s\n", $1 ".png", $2, $3 }'
    exit 0
fi

if [ "$DRY_RUN" -eq 0 ] && [ -z "${OPENAI_API_KEY:-}" ]; then
    echo "OPENAI_API_KEY is not set" >&2
    exit 2
fi

mkdir -p "$OUT_DIR"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

generated=0
skipped=0
failed=()

while IFS=$'\t' read -r name fmt prio prompt; do
    wanted "$name" || continue
    if [ "$MUST_HAVE" -eq 1 ] && [ "$prio" != "must have" ]; then continue; fi
    [ -n "$prompt" ] || { echo "$name: no prompt found, skipping" >&2; failed+=("$name"); continue; }

    target="$OUT_DIR/$name.png"
    size="$(size_for "$fmt")"
    full_prompt="$STYLE $(format_hint "$fmt")

$prompt"

    if [ "$DRY_RUN" -eq 1 ]; then
        printf '==> %s.png  (%s, %s, %s)\n%s\n\n' "$name" "$fmt" "$size" "$prio" "$full_prompt"
        continue
    fi

    if [ -f "$target" ] && [ "$FORCE" -eq 0 ]; then
        echo "skip  $name.png (exists, use --force to regenerate)"
        skipped=$((skipped + 1))
        continue
    fi

    echo "gen   $name.png ($size, $QUALITY)"
    body="$TMP/$name.request.json"
    resp="$TMP/$name.response.json"
    jq -n --arg model "$MODEL" --arg prompt "$full_prompt" --arg size "$size" --arg quality "$QUALITY" \
        '{model: $model, prompt: $prompt, size: $size, quality: $quality, n: 1, output_format: "png", background: "opaque"}' \
        > "$body"

    status="$(curl -sS -o "$resp" -w '%{http_code}' --max-time 300 \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -H "Content-Type: application/json" \
        -d @"$body" "$API_URL" || echo "000")"

    if [ "$status" != "200" ]; then
        msg="$(jq -r '.error.message // empty' "$resp" 2>/dev/null || true)"
        echo "fail  $name.png: HTTP $status ${msg:+: $msg}" >&2
        failed+=("$name")
        continue
    fi

    b64="$(jq -r '.data[0].b64_json // empty' "$resp")"
    url="$(jq -r '.data[0].url // empty' "$resp")"
    if [ -n "$b64" ]; then
        printf '%s' "$b64" | base64 -d > "$target"
    elif [ -n "$url" ]; then
        curl -sS --max-time 120 -o "$target" "$url"
    else
        echo "fail  $name.png: no image in response" >&2
        failed+=("$name")
        continue
    fi
    echo "ok    $target"
    generated=$((generated + 1))
done < <(entries)

[ "$DRY_RUN" -eq 1 ] && exit 0

echo
echo "generated: $generated, skipped: $skipped, failed: ${#failed[@]}"
if [ ${#failed[@]} -gt 0 ]; then
    printf '  %s\n' "${failed[@]}"
    exit 1
fi
