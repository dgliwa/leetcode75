# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        solution = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            solution[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            solution[i] *= right
            right *= nums[i]

        return solution
