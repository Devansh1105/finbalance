import json
import tempfile
import unittest
from pathlib import Path

from finbalance.generation.user_dataset import UserDatasetConfig, build_counts, generate_user_dataset


class PublicGenerationScriptTests(unittest.TestCase):
    def test_build_counts_distributes_exact_requested_records(self):
        counts = build_counts(
            industries=["retail"],
            period_types=["month", "quarter"],
            levels=[1, 2],
            records=5,
            records_per_combo=None,
            seed=7,
        )
        total = sum(count for periods in counts.values() for levels in periods.values() for count in levels.values())
        self.assertEqual(total, 5)
        self.assertEqual(set(counts), {"retail"})
        self.assertEqual(set(counts["retail"]), {"month", "quarter"})

    def test_build_counts_supports_records_per_combo(self):
        counts = build_counts(
            industries=["retail", "manufacturing"],
            period_types=["month"],
            levels=[1, 3],
            records=None,
            records_per_combo=2,
            seed=7,
        )
        total = sum(count for periods in counts.values() for levels in periods.values() for count in levels.values())
        self.assertEqual(total, 8)
        self.assertEqual(counts["retail"]["month"][1], 2)
        self.assertEqual(counts["manufacturing"]["month"][3], 2)

    def test_generate_user_dataset_writes_bundle(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_dir = Path(tmp_dir) / "custom"
            summary = generate_user_dataset(
                UserDatasetConfig(
                    output_dir=output_dir,
                    dataset_name="unit_test_custom",
                    records=3,
                    records_per_combo=None,
                    industries=("professional_services",),
                    period_types=("month",),
                    levels=(1, 2),
                    seed=11,
                    negative_control_rate=0.0,
                )
            )
            self.assertEqual(summary["records"], 3)
            self.assertTrue((output_dir / "records.jsonl").exists())
            self.assertTrue((output_dir / "record_manifest.jsonl").exists())
            self.assertTrue((output_dir / "manifest.json").exists())
            self.assertTrue((output_dir / "README.md").exists())
            self.assertTrue((output_dir / "assets").is_dir())

            rows = [json.loads(line) for line in (output_dir / "records.jsonl").read_text(encoding="utf-8").splitlines()]
            manifest = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(len(rows), 3)
            self.assertEqual(manifest["dataset_name"], "unit_test_custom")
            self.assertEqual(manifest["summary"]["records"], 3)


if __name__ == "__main__":
    unittest.main()
