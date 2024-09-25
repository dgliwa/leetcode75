# https://leetcode.com/problems/n-th-tribonacci-number
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        arr = [0,1, 1]
        for i in range(3, n + 1):
            prev_sum = sum(arr)
            arr.pop(0)
            arr.append(prev_sum)
        return arr[-1]
