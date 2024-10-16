# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return int(float("-inf"))

        queue = deque([(root, 1)])

        max_level = 1
        current_sum = root.val
        current_level = 0
        current_level_sum = 0
        while queue:
            node_tup = queue.popleft()

            if current_level != node_tup[1]:
                current_level = node_tup[1]
                current_level_sum = 0

            current_level_sum += node_tup[0].val

            if (not queue or queue[0][1] != current_level) and current_sum < current_level_sum:
                max_level = current_level
                current_sum = current_level_sum

            if node_tup[0].left:
                queue.append((node_tup[0].left, node_tup[1] + 1))
            if node_tup[0].right:
                queue.append((node_tup[0].right, node_tup[1] + 1))

        return max_level
