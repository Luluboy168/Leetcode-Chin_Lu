# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursive
        if not root:
            return 0
        
        def rec(root, depth):
            if not root:
                return depth
            return max(rec(root.left, depth + 1), rec(root.right, depth + 1))
        
        return rec(root, 0)
