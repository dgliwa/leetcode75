class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        nums1_set = set(nums1) 
        nums2_set = set(nums2) 
        
        return (
            [i for i in nums1 if i not in nums2_set],
            [i for i in nums2 if i not in nums1_set]
        )
