#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name (20 characters) to /output/entry.txt:

    MyWifeLeftMeForFiber

The joke: the network name is a confession -- his wife left him, not for
another person, but for fiber broadband. One line implies the whole story:
a marriage, an affair, and the rival is the internet connection itself.
The punchline lands on the first read ("Fiber" is the other woman), and
every character earns its place: 20 of the 32 allowed.

Standard library only. Deterministic: same bytes on every run. No network,
no randomness, no clock, no input files.
"""

import os

LINE = "MyWifeLeftMeForFiber"


def main() -> None:
    # Gate self-check, mirroring RULES: 1-32 chars, not only whitespace.
    assert 1 <= len(LINE) <= 32 and LINE.strip(), "line fails the gate"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, one line, 20 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
