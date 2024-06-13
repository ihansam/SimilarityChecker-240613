class SimilarityChecker:
    LENGTH_MAX_SCORE = 60
    ALPHA_MAX_SCORE = 40

    def examine_length_score(self, string1: str, string2: str) -> float:
        longer_length = max(len(string1), len(string2))
        shorter_length = min(len(string1), len(string2))

        if longer_length >= 2 * shorter_length:
            return 0

        return (1 - (longer_length - shorter_length) / shorter_length) * self.LENGTH_MAX_SCORE

    def examine_alphabet_score(self, string1: str, string2: str) -> float:
        alphabets1, alphabets2 = set(string1.upper()), set(string2.upper())
        same_cnt, total_cnt = len(alphabets1 & alphabets2), len(alphabets1 | alphabets2)
        return (same_cnt / total_cnt) * self.ALPHA_MAX_SCORE
