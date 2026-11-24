#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers - make.fun entry."""
from pathlib import Path

ENTRY = (
    "A great change is coming to your codebase. "
    "It is the intern, merging straight to main at 6 p.m. on a Friday."
)
OUTPUT = Path("/output/entry.txt")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
