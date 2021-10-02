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
    int res = 0;    
    int helper(TreeNode* root) {              
        int l = 1;
        int r = 1;        
        if (root->left!=nullptr) {            
            l = helper(root->left);
            if (root->val+1!=root->left->val) l = 1;  
            else l ++;            
        }        
        if (root->right!=nullptr) {
            r = helper(root->right);
            if (root->val+1!=root->right->val) r = 1; 
            else r ++;            
        }        
        int t = max(r,l);        
        if (t>res) res = t; 
        return t;   
    }    
    int longestConsecutive(TreeNode* root) {        
        int t = helper(root);
        return(res);        
    }
};
