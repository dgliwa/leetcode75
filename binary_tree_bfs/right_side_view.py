# https://leetcode.com/problems/binary-tree-right-side-view
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        nodes = [(1, root)]
        vals = []
        while nodes:
            level, node = nodes.pop(0)
            if len(vals) < level:
                vals.append(node.val)
            if node.right:
                nodes.append((level + 1, node.right))
            if node.left:
                nodes.append((level + 1, node.left))

        return vals
