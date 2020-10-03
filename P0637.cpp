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
// level order traversal/BFS
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        queue<TreeNode*> q;
        queue<int> l;
        q.push(root);
        l.push(0);
        int pl = -1;
        double s = 0.0;
        int ns = 1;
        while (!q.empty()) {
            TreeNode* n = q.front();            
            int ll = l.front();
            if (ll != pl) {                
                res.push_back(s/ns);
                s = 0;
                ns = 0; 
            }                           
            s += n->val;
            ns += 1;                            
            if (n->left != NULL) {
                q.push(n->left);
                l.push(ll+1);
            }
            if (n->right != NULL) {
                q.push(n->right);
                l.push(ll+1);
            }  
            pl = ll;
            q.pop();
            l.pop();
        }
        res.push_back(s/ns);
        res.erase(res.begin());
        return res;
    }
};