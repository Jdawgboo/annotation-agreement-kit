import unittest

from annotation_agreement_kit import cohen_kappa


class AgreementTests(unittest.TestCase):
    def test_perfect_agreement(self) -> None:
        result = cohen_kappa(["cat", "dog"], ["cat", "dog"])
        self.assertEqual(result.observed, 1.0)
        self.assertEqual(result.cohen_kappa, 1.0)

    def test_reports_disagreement_indexes(self) -> None:
        result = cohen_kappa(["yes", "no", "yes"], ["yes", "yes", "no"])
        self.assertEqual(result.disagreements, (1, 2))
        self.assertLess(result.cohen_kappa, 1.0)


if __name__ == "__main__":
    unittest.main()
