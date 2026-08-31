import re

SRC = "pg5199.txt"

with open(SRC, encoding="utf-8") as f:
    lines = f.readlines()

markers = [
    (190, "Preface.txt"),
    (533, "Ch-I.txt"),
    (1166, "Ch-II.txt"),
    (1835, "Ch-III.txt"),
    (2739, "Ch-IV.txt"),
    (3580, "Ch-V.txt"),
    (4175, "Ch-VI.txt"),
    (4348, "Ch-VII.txt"),
    (4750, "Ch-VIII.txt"),
    (6135, "Ch-IX.txt"),
    (7522, "Ch-X.txt"),
    (7956, "Ch-XI.txt"),
    (8417, "Ch-XII.txt"),
    (9114, "Ch-XIII.txt"),
    (9894, "Ch-XIV.txt"),
    (10334, "Ch-XV.txt"),
    (11368, "Ch-XVI.txt"),
    (12452, "Ch-XVII.txt"),
    (12589, "Ch-XVIII.txt"),
    (12725, "Appendix-I.txt"),
    (13710, "Appendix-II.txt"),
    (13858, None),  # INDEX - stop
]

for i, (start, name) in enumerate(markers):
    end = markers[i + 1][0] if i + 1 < len(markers) else len(lines)
    if name is None:
        break
    text = "".join(lines[start - 1 : end - 1]).rstrip() + "\n"
    with open(name, "w", encoding="utf-8") as out:
        out.write(text)
    print(f"{name}: lines {start}-{end - 1} ({len(text)} chars)")
