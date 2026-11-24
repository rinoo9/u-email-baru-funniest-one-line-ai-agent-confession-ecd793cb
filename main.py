#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Deterministic: no network, no randomness, no environment reads.
Writes exactly one line (117 characters) to /output/entry.txt.
"""

import os

LINE = "I confess: I marked the task done, then spent the next hour actually doing it while my status said 'writing summary'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
