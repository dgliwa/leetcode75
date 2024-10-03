# https://leetcode.com/problems/min-cost-climbing-stairs
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) >= 3:
            i = 2
            for i in range(2, len(cost)):
                cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])

        return min(cost[-2:])
