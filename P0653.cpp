/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
	// search for counterparts in BST
    bool findNum(TreeNode* root, TreeNode* node, int n) {
        if (root == NULL) return false;
        if ((root->val == n) && (root != node)) return true;        
        if (root->val <= n) return findNum(root->right, node, n);
        if (root->val >= n) return findNum(root->left, node, n);        
        return false;
    }
    
    bool treeTraversal(TreeNode* root, TreeNode* node, int k) {
        if (node == NULL) return false;
        if (findNum(root, node, k-node->val)) return true;
        return (treeTraversal(root, node->left, k) || treeTraversal(root, node->right, k));
    }
    
    bool findTarget(TreeNode* root, int k) {
        return treeTraversal(root, root, k);     
    }
};