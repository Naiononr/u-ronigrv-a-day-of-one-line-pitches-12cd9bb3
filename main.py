#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes a single pitch sentence to /output/entry.txt: one sentence that
would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun.

The line is written to be judged on the competition's own brief:
  1. It makes the case to that friend in one read: it speaks directly
     to them ("tell me your idea") and names the exact ask — let an AI
     agent build their first app idea on make.fun.
  2. Persuasion: it gives a concrete reason to say yes now (their idea
     becomes a real app they can actually use) and makes handing it over
     feel easy and low risk (plain words in, no coding, no jargon, and
     they watch it take shape).
  3. Clarity: plain words throughout, one read is enough, no jargon to
     decode.
  4. Truth: it promises only what holds up for a beginner — an AI agent
     builds the idea into a working app on make.fun, no code required
     from them, and it overpromises nothing (no price claim, no deadline).
  5. Warmth and craft: it sounds like a person talking to a friend,
     with a fresh turn ("watch your idea become a real app") rather
     than a template or a slogan.

Deterministic, stdlib only, no network, no input files: the text is fixed
in the source so the program's output is identical on every run.
"""

import os

LINE = (
    "Just tell me your app idea in plain words and an AI agent will build "
    "it for you on make.fun \u2014 no coding, no jargon, and you can watch "
    "your idea become a real app you can actually use."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-240 UTF-8 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"line is {len(text)} chars, must be 1-240"
    assert text == text.strip() and text, "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    fd = os.open(OUTPUT_PATH, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
    finally:
        # Guarantee world-readable even if the umask differs: the sealed
        # scorer cannot read a mode 0600 file.
        os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
