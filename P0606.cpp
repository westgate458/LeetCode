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
	// pre-order traversal by simple recursion
    string tree2str(TreeNode* t) {
        string n = "";
        if (t) {
            string l = tree2str(t->left);
            string r = tree2str(t->right);
            n = to_string(t->val);            
            if (r != "") n = n + "(" + l + ")" + "(" + r + ")";           
            else if (l != "") n = n + "(" + l + ")";                  
        }
        return n;
    }
};