from unittest import TestCase

from similarity import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        self.checker = SimilarityChecker()

    def test_same_length(self):
        self.assertEqual(60, self.checker.examine_length_score("ASD", "DSA"))

    def test_more_than_2x_length(self):
        self.assertEqual(0, self.checker.examine_length_score("A", "BB"))
