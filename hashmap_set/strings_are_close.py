
# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1_occurrences = {}
        word2_occurrences = {}
        for i in range(len(word1)):
            word1_occurrences[word1[i]] = word1_occurrences[word1[i]] + 1 if word1[i] in word1_occurrences else 1
            word2_occurrences[word2[i]] = word2_occurrences[word2[i]] + 1 if word2[i] in word2_occurrences else 1

        if not all(k in word2_occurrences for k in word1_occurrences.keys()) or not all(k in word1_occurrences for k in word2_occurrences.keys()):
            return False

        word1_counts_sorted = sorted(list(word1_occurrences.values()))
        word2_counts_sorted = sorted(list(word2_occurrences.values()))

        if word1_counts_sorted != word2_counts_sorted:
            return False

        return True
