"""Unit checks for skill validation behavior; run via unittest discovery."""
import tempfile
import unittest
from pathlib import Path
from scripts.validate import validate_skill, validate_links


class SkillValidationTests(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.root = Path(self.t.name)
        self.skill = self.root / "skills" / "prompt-me" / "SKILL.md"
        self.skill.parent.mkdir(parents=True)
    def tearDown(self):
        self.t.cleanup()
    def write(self, data):
        self.skill.write_text(data, encoding="utf-8")
        return validate_skill(self.skill)
    def test_valid_skill(self):
        self.assertEqual([], self.write(
            '---\nname: prompt-me\ndescription: "Use to refine engineering prompts."\n---\n# Prompt Me\n'))
    def test_missing_frontmatter(self):
        self.assertTrue(self.write("# No metadata\n"))
    def test_bad_name(self):
        self.assertTrue(self.write(
            '---\nname: Wrong_Name\ndescription: "Valid"\n---\n# Body\n'))
    def test_missing_description(self):
        self.assertTrue(self.write('---\nname: prompt-me\n---\n# Body\n'))
    def test_local_links(self):
        (self.root / "README.md").write_text("[ok](docs/x.md) [bad](docs/missing.md)\n")
        (self.root / "docs").mkdir()
        (self.root / "docs" / "x.md").write_text("# x")
        errors = validate_links(self.root)
        self.assertEqual(1, len(errors))
        self.assertIn("missing.md", errors[0])
    def test_prevents_escaping_repo(self):
        (self.root / "README.md").write_text("[escape](../../../../../etc/passwd)\n")
        self.assertTrue(any("escapes" in x for x in validate_links(self.root)))


if __name__ == "__main__":
    unittest.main()
