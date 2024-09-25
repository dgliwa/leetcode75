# https://leetcode.com/problems/successful-pairs-of-spells-and-potions
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        successes = []
        for spell in spells:
            min_index = 0
            max_index = len(potions) - 1
            while min_index <= max_index:
                midpoint = (max_index + min_index) // 2
                if spell * potions[midpoint] >= success:
                    max_index = midpoint - 1
                elif spell * potions[midpoint] < success:
                    min_index = midpoint + 1
            successes.append(len(potions) - 1 - max_index)
        return successes
