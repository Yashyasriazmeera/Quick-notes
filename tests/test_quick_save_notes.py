import re
import tempfile
import unittest
from pathlib import Path

from quick_save_notes import quick_save_note


class QuickSaveNotesTests(unittest.TestCase):
    def test_rejects_empty_note(self) -> None:
        with self.assertRaises(ValueError):
            quick_save_note("   ")

    def test_appends_note_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_file = Path(tmp_dir) / "notes" / "today.txt"
            quick_save_note("first", str(output_file))
            quick_save_note("second", str(output_file))

            content = output_file.read_text(encoding="utf-8").splitlines()
            self.assertEqual(2, len(content))
            self.assertRegex(
                content[0], r"^\[\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+00:00\]\s"
            )
            self.assertRegex(
                content[1], r"^\[\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+00:00\]\s"
            )
            self.assertIn("first", content[0])
            self.assertIn("second", content[1])


if __name__ == "__main__":
    unittest.main()
