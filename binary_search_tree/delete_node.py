# https://leetcode.com/problems/delete-node-in-a-bst/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            return self.delete(root)

        node = root
        while node:
            if node.val > key:
                if node.left and node.left == key:
                    node.left = self.delete(node.left)
                    break
                node = node.left
            elif node.val < key:
                if node.right and node.right == key:
                    node.right = self.delete(node.right)
                    break
                node = node.right
        return root

    def delete(self, node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left

        right = node.right
        last_right = right.right
        while last_right.right:
            last_right = last_right.right
        last_right.right = right
        return node.left
