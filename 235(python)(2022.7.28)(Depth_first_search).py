class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root == p or root == q or not root): return root    #found what we want or there is nothing 
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root    #common ancestor 
        elif left: return left
        elif right: return right
        
        return None
