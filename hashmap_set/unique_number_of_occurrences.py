# https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for val in arr:
            occurrences[val] = occurrences[val] + 1 if val in occurrences else 1


        counts = iter(occurrences.values())
        first = next(counts)
        return all(first == x for x in counts)
