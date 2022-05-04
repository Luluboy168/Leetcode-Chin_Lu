# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        #Recursive
        if not root:
            return False
        
        def rec(root, target):
            if not root:
                return False
            else:
                if not root.left and not root.right and target - root.val == 0:
                    return True
            return rec(root.left, target - root.val) or rec(root.right, target - root.val)
        
        return rec(root, targetSum)
