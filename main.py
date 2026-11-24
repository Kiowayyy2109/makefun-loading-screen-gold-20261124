#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip to /output/entry.txt.
"""

import os

TIP = "Tip: your agent already fixed the bug, broke two other things, and is now loading the courage to tell you."


def check(path="/output/entry.txt"):
    """Read the written tip back and re-check the gate: 1-200 chars, one line."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    assert text == TIP.strip(), "written tip differs from TIP"
    assert "\n" not in text and "\r" not in text
    assert 1 <= len(text) <= 200, len(text)
    return text


def main():
    text = TIP.strip()
    assert "\n" not in text
    assert 1 <= len(text) <= 200, len(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    check()


if __name__ == "__main__":
    main()
