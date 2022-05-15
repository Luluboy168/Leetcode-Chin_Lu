# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = []
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        
        return res
      
      
###solution 2
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         if not root:
#             return []
        
#         res = []
        
#         def rec(root):
#             if not root:
#                 return []
#             res.append(root.val)
#             return rec(root.left) + rec(root.right)
        
#         rec(root)
#         return res
