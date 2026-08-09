#!/usr/bin/env python3
"""
split_essays.py — Split Project Gutenberg file `56463-0.txt` (Bacon's Essays)
into one plain-text file per Essay.

Essay boundaries are the lines:  I.—OF TRUTH.   II.—OF DEATH.[53] ... LVIII.—…
Appendices restart at Roman-I after LVIII, so they are captured separately:
    I.—A FRAGMENT OF AN ESSAY OF FAME.[610]
    II.—OF A KING.
    III.—ON DEATH.

Stopping rule: begin skipping once the *second* occurrence of a line starting
with `THE WISDOM OF THE ANCIENTS` is encountered (the first lives in CONTENTS).

Output files are written under ./essays/ and named 01-of-truth.txt … etc.
A manifest is emitted as split-manifest.json listing every file produced.
Run from the directory containing this script:

    python3 split_essays.py
"""

import json
import re
from pathlib import Path

SOURCE = "56463-0.txt"
OUT_DIR = Path("essays")
WISDOM_MARKER = "THE WISDOM OF THE ANCIENTS"

# Roman numeral → int helper --------------------------------------------------
def roman_to_int(num: str) -> int:
    num = num.replace(".", "").replace("_", "")
    vals = {"I": 1, "V": 5, "X": 10, "L": 50}
    total = prev = 0
    for ch in reversed(num.upper()):
        cur = vals.get(ch, 0)
        if cur < prev:
            total -= cur
        else:
            total += cur
        prev = cur
    return total


# Heading regex ---------------------------------------------------------------
HEAD_RE = re.compile(r"^([A-Z]+)\.—(.+)$")

# Non-essay headings that share the same pattern but belong to other sections.
SKIP_HEADINGS = {"EXPLANATION", "FABLE", "INTRODUCTION"}


def safe_name(title: str) -> str:
    words = re.split(r"[,\.]|\s+", title.strip())
    words = [w.lower() for w in words if w and w.upper() == w]
    slug = "-".join(words).replace("—", "").strip("-") or "untitled"
    return slug


def collect_heads(src_lines):
    heads = []            # (line_index, order_int, full_heading)
    appendix_started = False
    essay_count = 0

    wisdom_seen = 0       # track occurrences of the WISDOM marker line

    for i, raw in enumerate(src_lines):
        stripped = raw.strip()

        if WISDOM_MARKER in stripped:
            wisdom_seen += 1
            if wisdom_seen >= 2:          # second occurrence ⇒ real fables start
                break
            continue                      # first is just the contents entry

        m = HEAD_RE.match(stripped)
        if not m:
            continue

        num_str, title_part = m.group(1), m.group(2)
        if num_str in SKIP_HEADINGS:
            continue                     # keep this line inside the previous essay block

        order = roman_to_int(num_str)
        full_heading = f"{num_str}.—{title_part}"

        if num_str == "I" and essay_count >= 58:
            appendix_started = True
            order = 100 + order          # appendices sort after essays

        heads.append((i, order, full_heading.strip()))
        essay_count += 1

    return heads


def main():
    src_path = Path(SOURCE)
    src_lines = src_path.read_text(encoding="utf-8").splitlines(keepends=True)

    OUT_DIR.mkdir(exist_ok=True)
    heads = collect_heads(src_lines)

    files_written = []
    for n, (start, order, title_text) in enumerate(heads):
        end_line = heads[n + 1][0] if n + 1 < len(heads) else None
        body_lines = src_lines[start:end_line]

        is_appendix = order >= 100
        name_slug = safe_name(title_text.split("—", 1)[-1]) or f"essay-{n+1}"

        if not is_appendix:
            fname = f"{n + 1:02d}-{name_slug}.txt"
        else:
            fname = f"a-{n - 58:02d}-{name_slug}.txt"

        out_path = OUT_DIR / fname
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.writelines(body_lines)
        files_written.append(str(out_path))

    manifest = {
        "source": str(src_path),
        "count": len(files_written),
        "files": files_written,
    }
    Path("split-manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(f"Wrote {len(files_written)} files to ./essays/")


if __name__ == "__main__":
    main()