/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {    
public:    
	//simple recursion
    void dfs(Node* root, vector<int> &res) {                
        for (auto n : root->children) dfs(n, res);
        res.push_back(root->val);
    }
    vector<int> postorder(Node* root) {
        vector<int> res;
        if (root) dfs(root, res);
        return res;
    }
};