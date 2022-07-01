# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #DFS reverse solution
        
        if not root:
            return root
        
        def DFSreverse(root):
            if not root:
                return 
            
            #swap left node and right node
            root.left, root.right = root.right, root.left
            
            DFSreverse(root.left)
            DFSreverse(root.right)
            
        DFSreverse(root)
        
        return root
