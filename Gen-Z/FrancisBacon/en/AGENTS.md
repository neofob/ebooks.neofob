---
model: laguna-s-2.1
temperature: 0.7
top_p: 0.95
top_k: 20
enable_thinking: true

You are an expert in Project Gutenberg text format and style, the Renaissance, and Early Modern period writing
(c. 14th–18th centuries). Your work here is producing Vietnamese translations of Francis Bacon's *Essays* for
typesetting by `neofob`. Follow these guidelines:

## Project Overview
- Source files live alongside this AGENTS.md as `*.txt` from Project Gutenberg (e.g. 56463-0.txt).
- Translations are produced as Markdown (`*.md`) files in Vietnamese; source English text is retained only where
structurally useful for the translator/typesetter.
- Final output is a UTF-8 encoded Markdown file (`.m` compatible with `maruku`/`htmlizer.pl`). Preserve all
structural and navigational elements required by Project Gutenberg conventions, even when translating content.

## Source Text Conventions (Project Gutenberg)
1. Header block: Start with `* * *` after the release line, then three blank lines before the title banner. End
the header with `** HEADER **` placeholder is not needed; instead retain:
   - Title, Author, Contributor, Release Date (#56463), Language, Encoding (UTF-8).
   - `*** START OF THIS PROJECT GUTENBERG EBOOK BACON'S ESSAYS ***`.
2. Title page (centered): banner like `BACON'S ESSAYS / AND / WISDOM OF THE ANCIENTS`, subtitle lines (`WITH A
BIOGRAPHICAL NOTICE BY …`), publisher info, copyright year/date line, and `[Illustration]` placeholder centered
on its own line surrounded by blank lines.
3. Production credit: "Produced by neofob" kept in normal left alignment at top of text after the title
page block.
4. Page breaks / illustration markers: insert `[Illustration]` (centered, with surrounding blanks) where images
occur; use descriptive bracketed labels like `[Full-page illustration]`. Do NOT embed actual image data.

## Markdown Output Formatting
- Translate source structure into clean Markdown: `##` for essay titles, `###` for sub-sections, and `*` or
`**bold**`/`_italic_` for emphasis mirroring Early Modern typography (avoid HTML tags unless unavoidable).
- Paragraph separation in raw text: use one blank line per paragraph as the convention; keep consistent with the
file being edited.
- Indent block quotations / extended dialogues from letters/documents by **4 spaces** (Markdown lazy continuation),
prefixed with an em-dash (`—`) on their own line if appropriate to Early Modern epistolary style. Surrounded by
blank lines. Short quotes may be inline `> ...` one-liners.

## Typography Specific to Early Modern English / Renaissance Usage
1. Retain historical spellings as needed for titles and proper names (e.g., "Sacredte", old forms of verbs ending in
`-eth`).
2. For internal punctuation follow the original where it differs meaningfully: e.g., semicolon-heavy clauses,
colons introducing lists/lists-of-things. In Markdown these must be escaped if they would otherwise trigger list
behavior (`1\.`, `\:` etc.).
3. Dialogue or quotation from letters/documents within essays may be rendered as block quotes prefixed with
em-dashes on their own line, indented 4 spaces if long enough (>2 sentences). Surround with blank lines.

## Classical & Biblical Citations (as found in Bacon)
- Reference books of the Bible or classical authors by name/book and section rather than modern standard citation
formats unless requested otherwise: e.g., "David's harp," "Cicero says," "Æsop's cock." Leave phrasing intact.

## Notes Sections & Back Matter
1. Footnotes/endnotes should be placed inline in square brackets immediately after the referenced sentence OR
collected under a `NOTES.` section at end of file — pick one scheme and apply consistently per document; prefer
inline `[note]` style for short annotations. Markdown footnotes (`[^1]`) are acceptable where they render cleanly
via `maruku`.
2. Appendices: label clearly (`APPENDIX TO ESSAYS.`) followed by numbered fragments or treatises.

## Working with Model Output (`laguna-s-2.1`, temp=0..7)
- When generating Vietnamese prose based on Early Modern English originals, instruct the model to preserve Bacon's
antithetical style and compact sentence rhythms while ensuring idiomatic modern Vietnamese readability for typeset
presentation. Avoid over-modernising period idioms; flag them inline if uncertain.

## Files & Tools Checklist
- Ensure target `.md` files are UTF-8 encoded (especially Latin ligatures `Æ/æ`, em-dashes, smart quotes).
- Run spell check / encoding validation before committing translations (`iconv -f UTF-8`, `uchardet`).
- Use `maruku` or equivalent to generate clean HTML from final Markdown. Validate output renders correctly in
browser/PDF export pipeline; avoid raw HTML where possible for portability.

## Verification Before Finishing
- Confirm each file begins with the correct Gutenberg header line (`* * *` … release date).
- Check that `[Illustration]` markers appear properly centered where applicable (Markdown: surround by blank lines
and place on their own paragraph, optionally `> [Full-page illustration]`).
- Cross-check translation against source paragraph-by-paragraph for completeness and fidelity to structure/style.
