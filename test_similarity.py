from unittest import TestCase

from similarity import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        self.checker = SimilarityChecker()

    def examine_length(self, str1, str2, expected_score):
        self.assertEqual(expected_score, self.checker.examine_length_score(str1, str2))

    def test_same_length(self):
        self.examine_length("ASD", "DSA", 60)

    def test_more_than_2x_length(self):
        self.examine_length("A", "BB", 0)
