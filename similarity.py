class SimilarityChecker:
    def examine_length_score(self, string1, string2):
        longer_length = max(len(string1), len(string2))
        shorter_length = min(len(string1), len(string2))

        if longer_length >= 2 * shorter_length:
            return 0

        if longer_length == shorter_length:
            return 60
