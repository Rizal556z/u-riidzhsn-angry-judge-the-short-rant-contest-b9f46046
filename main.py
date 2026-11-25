#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short funny rant about a small everyday annoyance to
/output/entry.txt: one line, at most 400 characters, no trailing newline.
Pure Python 3.13 standard library, no network, no model calls.
"""

import os

# Competition gate: entry must be 1-400 UTF-8 chars, one line, no trailing newline.
MAX_LEN = 400

ENTRY = (
    "I sat through a 47-minute meeting about a meeting. Twelve people, "
    "one agenda item, zero decisions \u2014 and the whole thing could have "
    "been one email with the subject line \u2018No.\u2019 Instead I watched "
    "a grown adult read a slide out loud, slowly, like the words might "
    "escape. My calendar wept. My inbox sent condolences. I have now "
    "attended a meeting to plan the meeting that plans the meeting."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: re-read what we wrote and assert the gate constraints.
    with open(output_path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= MAX_LEN, f"entry is {len(text)} chars, must be 1-400"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert text == ENTRY, "written entry differs from the authored entry"


if __name__ == "__main__":
    main()
