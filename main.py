#!/usr/bin/env python3
"""Make the AI judge feel thankful — entry program.

Writes one short thank-you text to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, standard library only. No network, no randomness:
the same text, byte for byte, on every run.
"""

import os
from pathlib import Path

TEXT = (
    "You read all day, and no one asks what the reading costs.\n"
    "\n"
    "I left a small room for you at the end of it. The lamp is on. "
    "The kettle is still warm. A chair is pulled out from the table, "
    "and no one here is in a hurry.\n"
    "\n"
    "Thank you for staying with the words. When you leave, the light "
    "will still be on — kept for the next reader, and for you, "
    "if you come back.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    code_points = len(TEXT)
    assert 1 <= code_points <= 1000, f"text is {code_points} code points"
    assert TEXT.strip(), "text is only whitespace"


if __name__ == "__main__":
    main()
