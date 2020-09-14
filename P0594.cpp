class Solution {
public:
	//sorted hashtable for occurances
    int findLHS(vector<int>& nums) {        
        if (nums.size() == 0)  return 0;   
        unordered_map<int,int> counts;
        for (auto n : nums)  counts[n] ++; 
        vector<pair<int, int>> sorted(counts.begin(), counts.end());
        sort(sorted.begin(), sorted.end());
        int res = 0;
        for (int i = 0; i < sorted.size()-1; i++) {           
            if ((sorted[i+1].first == sorted[i].first + 1) && (sorted[i].second + sorted[i+1].second > res)) {
                res = sorted[i].second + sorted[i+1].second;                
            }            
        }
        return res;        
    }
};