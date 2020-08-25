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
    //simple recursion
    int res = 0;
    
    int DFS(TreeNode* root) {
        if (root) {
            int L = DFS(root->left);
            int R = DFS(root->right); 
            res += abs(L - R);                      
            return L+R+root->val;
        }
        else return 0;
    }    

    int findTilt(TreeNode* root) {
        DFS(root);
        return res;
    }
};