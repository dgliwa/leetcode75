# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap  = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            heapq.heappushpop(heap, n)
        return heap[0]
        
