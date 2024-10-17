# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        node = head
        while node:
            temp = node
            node = node.next
            temp.next = prev_node
            prev_node = temp

        return prev_node
