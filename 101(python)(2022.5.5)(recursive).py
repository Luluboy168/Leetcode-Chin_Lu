# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        #recursive
        if not root:
            return True
        
        def compare(left, right):
            if not left or not right:
                if not left and not right:
                    return True 
                return False
            elif left.val == right.val:
                return compare(left.left, right.right) and compare(left.right, right.left)
            else:
                return False
            
        return compare(root.left, root.right)
