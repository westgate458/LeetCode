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
    
    vector<int> gather(TreeNode* root) {
        vector<int> results;
        if (root->left != NULL) {
            vector<int> l = gather(root->left);
            vector<int> r = gather(root->right);      
            results.reserve(l.size() + r.size()+1);
            results.insert(results.end(), l.begin(), l.end());
            results.push_back(root->val);
            results.insert(results.end(), r.begin(), r.end());
        }
        else {
            results.push_back(root->val);
        }
        return results;        
    }

    
    int findSecondMinimumValue(TreeNode* root) {
        auto nums = gather(root);
        sort(nums.begin(), nums.end()); 
        int c = 0;
        int pre = -1;
        int res = -1;
        for (auto n : nums) {
            //cout << n << ' ' << endl;
            if (n!=pre) {
                c += 1;
                pre = n;
            }
            if (c == 2) {
                res = n;
                break;
            }
        }
        return res;        
    }
};