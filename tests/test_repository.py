import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_repo import ROOT, check_links, check_packs, unique_keys, validate_pack


class PackTests(unittest.TestCase):
    def setUp(self):
        self.pack = json.loads((ROOT / "packs/ch-diagnosis-demo.json").read_text())

    def test_committed_packs(self):
        self.assertGreaterEqual(check_packs(ROOT / "packs"), 2)

    def test_another_country_needs_no_validator_branch(self):
        self.pack.update(id="xx-design-example", country="XX", locales=["xx-XX"])
        self.assertEqual(validate_pack(self.pack), "xx-design-example")

    def test_missing_and_unknown_fields(self):
        for key in self.pack:
            with self.subTest(missing=key):
                changed = copy.deepcopy(self.pack)
                del changed[key]
                with self.assertRaises(ValueError):
                    validate_pack(changed)
        self.pack["surprise"] = True
        with self.assertRaises(ValueError):
            validate_pack(self.pack)

    def test_permissive_or_invalid_values_rejected(self):
        cases = [
            ((), "schema_version", True),
            ((), "schema_version", 2),
            ((), "country", "Switzerland"),
            ((), "id", "../escape"),
            ((), "locales", []),
            ((), "locales", ["de-CH", "de-CH"]),
            ((), "locales", [{}]),
            ((), "status", "approved"),
            ((), "clinical_use", True),
            ((), "clinical_use", 0),
            (("coding",), "system", ""),
            (("coding",), "task", "billing"),
            (("coding",), "effective_from", "2026-02-30"),
            (("coding",), "effective_from", "20260101"),
            (("coding",), "effective_from", "2027-01-01"),
            (("coding",), "applicability", "approved"),
            (("catalog",), "redistribute", True),
            (("catalog",), "review_status", "approved"),
            (("catalog",), "source_url", "http://example.org"),
            (("catalog",), "terms_url", "https://user:password@example.org"),
            (("boundary",), "synthetic_only", False),
            (("boundary",), "identity_location", "cloud"),
            (("boundary",), "failure_mode", "allow"),
            (("boundary",), "cloud_egress", "authorized"),
        ]
        for path, key, value in cases:
            with self.subTest(path=path, key=key, value=value):
                changed = copy.deepcopy(self.pack)
                target = changed
                for part in path:
                    target = target[part]
                target[key] = value
                with self.assertRaises(ValueError):
                    validate_pack(changed)

    def test_unknown_nested_fields(self):
        for key in ("coding", "catalog", "boundary"):
            with self.subTest(key=key):
                changed = copy.deepcopy(self.pack)
                changed[key]["unknown"] = "value"
                with self.assertRaises(ValueError):
                    validate_pack(changed)

    def test_invalid_pack_types(self):
        for value in (None, [], "pack", 1):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_pack(value)

    def test_duplicate_json_keys_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate key"):
            json.loads('{"id": "a", "id": "b"}', object_pairs_hook=unique_keys)

    def test_empty_directory_and_filename_mismatch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(ValueError, "no packs"):
                check_packs(root)
            (root / "wrong-name.json").write_text(json.dumps(self.pack))
            with self.assertRaisesRegex(ValueError, "filename"):
                check_packs(root)

    def test_duplicate_pack_id(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("ch-diagnosis-demo", "duplicate"):
                (root / f"{name}.json").write_text(json.dumps(self.pack))
            with self.assertRaisesRegex(ValueError, "duplicate pack id"):
                check_packs(root)


class DocumentationTests(unittest.TestCase):
    def test_local_links(self):
        self.assertGreater(check_links(ROOT), 0)

    def test_broken_link_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("[missing](missing.md)")
            with self.assertRaisesRegex(ValueError, "broken link"):
                check_links(root)


if __name__ == "__main__":
    unittest.main()
