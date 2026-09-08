"""Regression checks for plugin growth and broken skill packaging."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ("plugins", ".agents", "scripts"):
            shutil.copytree(ROOT / directory, self.root / directory)
        self.plugin = self.root / "plugins" / "wagner-engineering-security"
        self.skills = self.plugin / "skills"

    def validate(self, success, message=""):
        result = subprocess.run(
            [sys.executable, "-X", "utf8", str(self.root / "scripts" / "validate.py")],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0 if success else 1, result.stdout + result.stderr)
        self.assertIn(message, result.stdout)

    def test_current_package(self):
        self.validate(True)

    def test_additional_skill_is_discovered(self):
        folder = self.skills / "fixture-skill"
        folder.mkdir()
        (folder / "SKILL.md").write_text(
            "---\nname: fixture-skill\ndescription: Test fixture.\n---\n\n# Fixture\n",
            encoding="utf-8",
        )
        self.validate(True)

    def test_skill_directory_requires_entrypoint(self):
        (self.skills / "incomplete-skill").mkdir()
        self.validate(False, "SKILL.md")

    def test_empty_folded_description_is_rejected(self):
        target = self.skills / "python-scripting" / "SKILL.md"
        target.write_text("---\nname: python-scripting\ndescription: >\n---\n# Python\n", encoding="utf-8")
        self.validate(False, "description")

    def test_invalid_name_is_rejected(self):
        folder = self.skills / "Invalid_Name"
        folder.mkdir()
        (folder / "SKILL.md").write_text(
            "---\nname: Invalid_Name\ndescription: Fixture.\n---\n# Fixture\n", encoding="utf-8"
        )
        self.validate(False, "nome")

    def test_broken_link_in_reference_is_rejected(self):
        target = self.skills / "python-scripting" / "references" / "automation.md"
        with target.open("a", encoding="utf-8") as stream:
            stream.write("\n[Missing resource](missing-resource.md)\n")
        self.validate(False, "referência")

    def test_missing_direct_reference_is_rejected(self):
        (self.skills / "python-scripting" / "references" / "automation.md").unlink()
        self.validate(False, "referência")


if __name__ == "__main__":
    unittest.main()
