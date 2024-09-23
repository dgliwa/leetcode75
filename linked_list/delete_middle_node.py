# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        fast = head
        slow = head

        while fast.next:
            fast = fast.next.next if fast.next else None
            slow_prev = slow
            slow = slow.next
        
        slow_prev.next = slow.next
        return head
