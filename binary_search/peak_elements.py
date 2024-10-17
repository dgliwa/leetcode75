# https://leetcode.com/problems/find-peak-element/

from collections import deque


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        min_i = 0
        max_i = len(nums) - 1
        queue = deque([(min_i, max_i)])

        while queue:
            i, j = queue.popleft()
            midpoint = (i + j) // 2
            print(i, j, midpoint)
            val = nums[midpoint]
            if (midpoint == 0 or val > nums[midpoint - 1]) and (midpoint + 1 > max_i or val > nums[midpoint + 1]):
                return midpoint

            if i <= midpoint and midpoint > min_i:
                queue.append((i, midpoint - 1))
            if midpoint <= j and midpoint < max_i:
                queue.append((midpoint + 1, j))
        return -1
