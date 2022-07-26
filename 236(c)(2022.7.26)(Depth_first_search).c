/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) { 
     
    // DFS solution 
    if (!root || root == p || root == q) return root;   // found what we want or there is nothing 
     
    struct TreeNode* left = lowestCommonAncestor(root->left, p, q); 
    struct TreeNode* right = lowestCommonAncestor(root->right, p, q); 
    
    return !left?right:!right?left:root;
     
//     if (left && right) return root; // common ancestor
//     else if (left) return left; 
//     else if (right) return right; 
     
//     return NULL; 
     
}
