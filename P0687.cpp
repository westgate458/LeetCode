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
	// update global max with path sum within, and return larger path sum goint out
    int ans = 0;    
    int DFS(TreeNode* root) {                
        if (root==NULL) return 0;        
        int l = DFS(root->left);
        int r = DFS(root->right);
        int left = 0, right = 0;
        if (root->left != NULL && root->val==root->left->val) left = l + 1;        
        if (root->right != NULL && root->val==root->right->val) right = r + 1;
        ans = max(ans, left+right);
        return left>right?left:right;
    }
    int longestUnivaluePath(TreeNode* root) { 
        int res = DFS(root); 
        return ans;
    }
};