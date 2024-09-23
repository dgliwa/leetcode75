# https://leetcode.com/problems/maximum-average-subarray-i
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        rolling_sum = sum(nums[:k])
        max_sum = rolling_sum
        last_val = nums[0]
        
        for i in range(k, len(nums)):
            rolling_sum = rolling_sum - last_val + nums[i]
            last_val = nums[i - k + 1]
            max_sum = rolling_sum if not max_sum else max(max_sum, rolling_sum)
        return max_sum / k
            
