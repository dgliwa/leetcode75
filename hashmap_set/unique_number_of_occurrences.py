# https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for val in arr:
            occurrences[val] = occurrences[val] + 1 if val in occurrences else 1

        occurrence_counts = set()
        for val in occurrences.values():
            if val in occurrence_counts:
                return False
            occurrence_counts.add(val)
        return True
