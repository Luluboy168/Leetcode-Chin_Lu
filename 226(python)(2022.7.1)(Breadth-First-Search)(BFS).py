# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #BFS reverse solution
        if not root:
            return root
        
        queue = [] #first in first out
        queue.append(root)
        
        while(queue):
            node = queue.pop(0)
            
            left, right = None, None
            
            if node.left:
                left = node.left
            if node.right:
                right = node.right
                
            node.left = right
            node.right = left
            
            if left:
                queue.append(left)
            if right:
                queue.append(right)
            
        return root
