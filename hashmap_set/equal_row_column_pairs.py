# https://leetcode.com/problems/equal-row-and-column-pairs/
from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        column_vals = Counter(
            [tuple(column) for column in grid]
        )

        row_vals = [tuple(row) for row in zip(*grid)]

        return sum(column_vals[row] for row in row_vals if row in column_vals)
