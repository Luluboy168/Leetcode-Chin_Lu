# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #DFS recursive
        ans = [True]
        def dfs(root, count):
            if root:
                leftcount = dfs(root.left, count + 1)
                rightcount = dfs(root.right, count + 1)
                if abs(leftcount - rightcount) > 1:
                    ans[0] = False
                return max(leftcount, rightcount) + 1
            return 0 
        
        dfs(root, 0)
        return ans[0]
