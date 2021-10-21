class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> m;        
        for (auto s:strs) {
            string ss = s;
            sort(ss.begin(),ss.end());
            m[ss].push_back(s);
        }        
        vector<vector<string>> res;
        for (auto entry:m) {
            res.emplace_back(entry.second);
        }
        return(res);
    }
};