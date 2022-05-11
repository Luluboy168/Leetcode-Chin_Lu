# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def rec(root, depth):
            if not root.left and not root.right:
                return depth
            if not root.left:
                return rec(root.right, depth + 1)
            elif not root.right:
                return rec(root.left, depth + 1)
            else:
                return min(rec(root.right, depth + 1), rec(root.left, depth + 1))        
        
        return rec(root, 1)
