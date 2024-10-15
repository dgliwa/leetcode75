# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        first_even = head.next
        even = first_even
        odd = head

        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next

        odd.next = first_even
        return head
