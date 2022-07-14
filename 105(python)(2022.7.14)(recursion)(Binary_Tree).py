# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #recursive solution
        if inorder:
            INDEX = inorder.index(preorder.pop(0))   # the first element in preorder is the root
            root = TreeNode(inorder[INDEX])
            root.left = self.buildTree(preorder, inorder[:INDEX])     #left to INDEX is the left subtree
            root.right = self.buildTree(preorder, inorder[INDEX+1:])  #right to INDEX is the right subtree
            
            return root
