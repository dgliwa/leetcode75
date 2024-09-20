# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nex
class Solution(object):
    def pairSum(self, head):
    #     ""
    #     :type head: Optional[ListNode]
    #     :rtype: int
    #     """
        node = head
        node_vals = []
        while node:
            node_vals.append(node.val)
            node = node.next
        
        max_sum = 0
        while node_vals:
            first = node_vals.pop(0)
            last = node_vals.pop()
            max_sum = max(max_sum, first + last)
        return max_sum

    # Not my answer, but much faster:
    # def pairSum(self, head):
    #     slow, fast = head, head
    #     maxVal = 0
    #
    #     # Get middle of linked list
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #
    #     # Reverse second part of linked list
    #     curr, prev = slow, None
    #
    #     while curr:       
    #         curr.next, prev, curr = prev, curr, curr.next   
    #
    #     # Get max sum of pairs
    #     while prev:
    #         maxVal = max(maxVal, head.val + prev.val)
    #         prev = prev.next
    #         head = head.next
    #
    #     return maxVal
