# Quick-notes

Quickly save timestamped notes from the command line.

## Usage

```bash
python quick_save_notes.py "Buy milk on the way home"
```

This appends the note to `notes.txt` with a UTC timestamp.

Optional custom output file:

```bash
python quick_save_notes.py "Team sync at 2pm" --file my_notes/today.txt
```