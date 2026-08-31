# Translation Agents: South — Shackleton's Last Expedition (English to Vietnamese)

This project translates Sir Ernest Shackleton's *South: The Story of Shackleton's Last Expedition, 1914–1917*
(Project Gutenberg `#5199`) from English into Vietnamese. The aim is not a word-for-word transfer but a literary
adaptation that preserves the voice of a British naval officer's first-hand war diary of the Antarctic — its
restraint, its gallows humour, its understated heroism, and its deep affection for his men.

## 📚 Source Material (in `en/`)

| File | Content |
|------|---------|
| `Preface.txt` | Preface |
| `Ch-I.txt` … `Ch-XVIII.txt` | Chapters I–XVIII |
| `Appendix-I.txt` | Appendix I: Scientific work (Wordie) + sea-ice nomenclature, meteorology, physics, whaling |
| `Appendix-II.txt` | Appendix II: The expedition huts at McMurdo Sound |

## 🎯 Project Goal

Produce a Vietnamese that a modern reader experiences the way the book is experienced in English: as an honest,
plainspoken account of a doomed expedition that somehow still becomes one of the great stories of human endurance. The
translation must keep the *understatement* — many of the book's most powerful moments are deliberately dry. Do
not dramatize what the author held back.

## 📜 Translation Guidelines

### 1. Voice and Tone
- **The narrator is Shackleton**: a naval-trained leader in his 30s, writing in the 1920s about events of
1914–1917. The tone is matter-of-fact, often wry, sometimes blunt. Use Vietnamese that is **cứng cỏi mà
ấm áp** (resolute but warm) — short, concrete declarative sentences, rarely ornate.
- **British understatement (understatement/underview)**: English expressions like "it was a fine morning" on
a day that nearly killed everyone must land with the same deadpan force. Resist the instinct to add Vietnamese
intensifiers when the English is flat.
- **Warmth toward the men**: Shackleton never sentimentalizes, but his loyalty to his comrades is constant. In
Vietnamese this reads best as *cảm tình của người đồng ngũ* — comradeship expressed through action
and small details, not lyrical praise.
- **Humour**: dry, self-deprecating, situational (e.g., about penguins, dogs, weather, food). Keep it dry. Pun/wordplay
that cannot be ported should be rendered as the closest *attitude*, not the closest sound.

### 2. Cultural and Linguistic Adaptation (British → Vietnamese)
- **Rank and formality**: 1910s British expedition ranks must be stable and correctly ordered; the same rank
must get the same Vietnamese term all book, in exact order (never promote or demote a man between chapters). Use
the convention common in Vietnamese polar literature, mapping by seniority: *Admiral → Đô đốc, Commodore
→ Chuẩn đô đốc, Commander → Thuyền trưởng, Lieutenant-Commander → Thiếu tá, Lieutenant →
Trung úy, Sub-Lieutenant → Thiếu uý*; on the Ross Sea party, army-style *Major → Thiếu tá, Lieutenant
→ Trung úy, Captain → Đại uý*. Honourifics: *Sir Shackleton → "Sir Shackleton"* (keep *Sir*, *Lord*
untranslated as courtesy forms), *Mrs/Miss/Mr → Bà/Cô/Ông*. All such decisions go into the glossary below
and never change mid-book.
- **Ship names, place names**: ship names are kept in Latin script without quotes and italicised as in the source:
*Endurance, Aurora, James Caird*. Place names follow the English form in the body (Weddell Sea → *biển Weddell*,
James Ross Island → *đảo James Ross*, Vahsel Bay → *vịnh Vahsel*). A first full reference to a place may
carry its English name in parentheses once, then the short form.
- **"The Ice"**: the Weddell Sea pack ice as an antagonist. Choose one consistent Vietnamese term for the great
ice barrier/pack (e.g., *băng bao*, *băng đóng*) and *đảo băng / tấm băng* for floes, per the Appendix
I nomenclature — the Appendix is the in-book dictionary; the main text and Appendix must use the same word.
- **British everyday texture**: items like *"a cup of tea", "biscuit", "marmite", "a good brew"* should be rendered
in Vietnamese that carries the same homespun British warmth (e.g., *một tách trà* is fine) — never localize
into something that belongs to a different culture.
- **Quoted speech**: men's speech on the ice is plain, practical, often clipped. Vietnamese dialogue here should
be brief, un-adorned, and distinct from narration. Keep the 1910s register: no modern slang.
- **Avoid "translation-ese" (văn bản dịch)**: rebuild sentences in natural Vietnamese syntax (topic–comment,
verb-final feel) rather than inverting English clause order. Long English sentences with nested participles should
be split; short clipped English sentences should stay short.

### 3. Quality Benchmarks
- **Faithfulness**: no invented events, no softened deaths, no added sentiment. If the source is grim and brief,
the Vietnamese is grim and brief.
- **Readability**: read the Vietnamese aloud; it must sound like written Vietnamese, not English wearing diacritics.
- **Period accuracy**: the book is set 1914–1917 and written with that generation's plain moral vocabulary (duty,
honour, the Navy's code). Let that *đạo* (duty/rectitude) resonate without turning into Confucian sermon.

## 🛠 Technical Instructions
- **Output**: one file per source file, in the `vn/` directory next to `en/`, named `Preface.txt`, `Ch-I.txt` …
`Ch-XVIII.txt`, `Appendix-I.txt`, `Appendix-II.txt`. Plain text, same paragraph structure as the source. Do not
merge or split chapters.
- **Headings**: chapter heading line 1 is `CHƯƠNG I`, line 2 is the title in uppercase Vietnamese (e.g.,
`CHƯƠNG I` / `VÀO BIỂN WEDDELL`). Keep the original two-line layout and the blank lines after.
- **Illustration notes**: lines like `[Illustration: ...]` → `[Hình: ...]`, keeping the rest of the note translated.
- **Markdown italics in source** (`_Endurance_`, `*word*`): keep the exact marker and the word inside it untranslated
only if it is a proper name to be kept in Latin script; otherwise translate the word and keep the markers.
- **Consistency**: before translating each chapter, check the running glossary in `vn/GLOSSARY.md` for fixed terms
(ranks, ships, place names, sea-ice terms, recurring phrases like *"the white silence"*). Add any new recurring
term there as you go. One term = one Vietnamese rendering for the whole book.
- **Working order**: translate in order `Preface` → `Ch-I` … `Ch-XVIII` → `Appendix-I` → `Appendix-II`,
so later chapters can reuse established choices. The Glossary is the source of truth; the source is the source of
fact; the glossary + source together define the book.
- **Verification**: after finishing a file, re-read it against the English side by side: same paragraphs, same
names, same numbers (dates, distances in miles, temperatures in °F — keep the units and numbers exactly as in
the source), and the same emotional temperature.
