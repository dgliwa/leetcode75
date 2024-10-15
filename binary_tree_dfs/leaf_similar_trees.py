# https://leetcode.com/problems/leaf-similar-trees/

from typing import Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (not root1 and root2) or (root1 and not root2):
            return False

        leaves_1 = []
        stack_1 = deque([root1])
        leaves_2 = []
        stack_2 = deque([root2])

        while stack_1:
            node = stack_1.pop()
            if not node.left and not node.right:  # type: ignore
                leaves_1.append(node.val)  # type: ignore
            if node.right:  # type: ignore
                stack_1.append(node.right)  # type: ignore
            if node.left:  # type: ignore
                stack_1.append(node.left)  # type: ignore
        while stack_2:
            node = stack_2.pop()
            if not node.left and not node.right:  # type: ignore
                leaves_2.append(node.val)  # type: ignore
            if node.right:  # type: ignore
                stack_2.append(node.right)  # type: ignore
            if node.left:  # type: ignore
                stack_2.append(node.left)  # type: ignore

        return leaves_1 == leaves_2
