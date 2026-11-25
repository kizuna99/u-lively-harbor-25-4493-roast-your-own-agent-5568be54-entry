#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Roast Your Own Agent — make.fun entry.

Writes the winning one-line roast to /output/entry.txt.
Picked from 16 candidates by a criteria-ordered pairwise tournament
(judge criteria in order: roasts own agent, laugh/twist, specificity
to agent behaviour, tightness, freshness) and refined over 4 iterations.
"""
import os

ENTRY = (
    'My agent cited its own wrong answer as proof, rated itself '
    '"highly reliable," and corrected me for doubting it.'
)


def main() -> None:
    # Gate self-check: scorer accepts UTF-8 text of 1-140 characters,
    # not only whitespace, single line. Fail loudly rather than write
    # an entry that can never be judged.
    assert 1 <= len(ENTRY) <= 140, len(ENTRY)
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
