# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        
        good_node_count = 0
        nodes = []
        nodes.append((root, root.val))

        while nodes:
            node, max_val = nodes.pop()
            new_max_val = max(node.val, max_val)
            
            if node.val == new_max_val:
                good_node_count = good_node_count + 1

            if node.left:
                nodes.append((node.left, new_max_val))
                
            if node.right:
                nodes.append((node.right, new_max_val))
        return good_node_count
