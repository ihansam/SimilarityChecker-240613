from unittest import TestCase

from similarity import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        self.checker = SimilarityChecker()

    def examine_length(self, str1, str2, expected_score):
        self.assertAlmostEqual(expected_score, self.checker.examine_length_score(str1, str2), delta=1e-14)

    def test_same_length(self):
        self.examine_length("ASD", "DSA", 60)

    def test_more_than_2x_length(self):
        self.examine_length("A", "BB", 0)

    def test_less_than_2x_length(self):
        self.examine_length("AAABB", "BAA", 20)
        self.examine_length("AA", "AAE", 30)

    def examine_alphabets(self, str1, str2, expected_score):
        self.assertAlmostEqual(expected_score, self.checker.examine_alphabet_score(str1, str2), delta=1e-14)

    def test_all_same_alphabets(self):
        self.examine_alphabets("ASD", "DSA", 40)
        # self.examine_alphabets("AAABB", "BAA", 40)

    def test_all_diff_alphabets(self):
        self.examine_alphabets("A", "BB", 0)

    def test_similar_alphabets(self):
        self.examine_alphabets("AA", "AAE", 20)
