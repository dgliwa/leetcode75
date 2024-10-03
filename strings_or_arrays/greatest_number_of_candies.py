# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]
