#!/usr/bin/env python3
"""Weirdest Job Title — make.fun bounty entry.

Writes a single original job title (1 to 60 characters) to
/output/entry.txt, exactly as the competition gate expects: the weirdest
job title imaginable, and nothing else.
"""

import os

# REVISION PASS (against the RULES judging criteria, in order):
# 1. A weird job title, a few words naming an odd job — nothing else.
# 2. Stranger than ordinary work: apologising TO a printer, a machine
#    humans already fight with daily, is a gloriously odd twist.
# 3. Funny on the first read: the senior title clashes with the
#    humiliating duty — a VP whose whole job is saying sorry to hardware.
# 4. Sounds like a real job: the corporate "Senior Vice President of ..."
#    frame is instantly picture-able, the person doing it easy to see.
# 5. Reads instantly: one title, no setup, no wasted words. The draft
#    ("Director of Lost Socks, Laundromat Division") was cut — odd, but
#    its twist was too gentle to beat a title with a real punchline.
LINE = "Senior Vice President of Apologizing to Printers"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 60, f"title must be 1-60 chars, got {len(text)}"
    # Single line, no trailing newline: the gate counts the file's characters.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
