# Definition for a binary tree node. 
# class TreeNode: 
#     def __init__(self, val=0, left=None, right=None): 
#         self.val = val 
#         self.left = left 
#         self.right = right 
class Solution: 
    def flatten(self, root: Optional[TreeNode]) -> None: 
        """ 
        Do not return anything, modify root in-place instead. 
        """ 
        # check if root exists 
        if root: 
             
            temp = root.right # store the right part of root 
             
            root.right = root.left  # move the left part to the right 
            root.left = None        # clear left part 
             
            curr = root 
            while curr.right:       # use while loop to find the bottom right side 
                curr = curr.right 
            curr.right = temp       # attach temp back 
             
            #recursion 
            self.flatten(root.right)
