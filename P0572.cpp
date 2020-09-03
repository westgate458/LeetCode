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
	//check if one is identical to certain subtree of the other
    bool isIdentical(TreeNode* s, TreeNode* t) {
        if (s == NULL || t == NULL)  return s == t;  
        return (t->val == s->val) && isIdentical(s->left, t->left) && isIdentical(s->right, t->right);
    }    
    bool isSubtree(TreeNode* s, TreeNode* t) {  
        return isIdentical(s, t) || (s != NULL && (isSubtree(s->left, t) || s->right && isSubtree(s->right, t)));
    }
};