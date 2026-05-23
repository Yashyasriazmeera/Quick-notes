#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def quick_save_note(note: str, file_path: str = "notes.txt") -> str:
    cleaned_note = note.strip()
    if not cleaned_note:
        raise ValueError("Note cannot be empty.")

    target = Path(file_path)
    if target.parent != Path("."):
        target.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    entry = f"[{timestamp}] {cleaned_note}\n"
    target.write_text(
        target.read_text(encoding="utf-8") + entry if target.exists() else entry,
        encoding="utf-8",
    )
    return str(target)


def main() -> int:
    parser = argparse.ArgumentParser(description="Quickly save a note to a text file.")
    parser.add_argument("note", nargs="+", help="The note text to save.")
    parser.add_argument(
        "--file",
        default="notes.txt",
        help="Destination file for notes (default: notes.txt).",
    )
    args = parser.parse_args()

    try:
        file_written = quick_save_note(" ".join(args.note), file_path=args.file)
    except ValueError as exc:
        print(exc)
        return 1

    print(f"Saved note to {file_written}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
