struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) { 
    if(root == p || root == q || !root) return root;   // found what we want or there is nothing 
    struct TreeNode* left = lowestCommonAncestor(root->left, p, q); 
    struct TreeNode* right = lowestCommonAncestor(root->right, p, q); 
    return !left?right:!right?left:root; 
}
