class Solution {
public:
	// hashtable or set with two loops
    vector<int> findErrorNums(vector<int>& nums) {
        unordered_set<int> s;
        vector<int> res(2);
        for (auto n:nums) {
            if (s.find(n) == s.end()) s.insert(n);            
            else res[0] = n;       
        }
        for (int n=1;n<=nums.size();n++) {
            if (s.find(n) == s.end()) {               
                res[1] = n;
                break;
            }           
        }
        return res;
    }
};