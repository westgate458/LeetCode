class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int res = 1, degree = 1;            
        unordered_map<int, array<int,3>> m; 
        for (int i=0;i<nums.size();i++) {
            m[nums[i]][0] ++;               
            if (m[nums[i]][0] == 1) m[nums[i]][1] = i; 
            m[nums[i]][2] = i;         
        }              
        for (auto p = m.begin(); p != m.end(); p++) { 
            if (p->second[0] > degree) {
                degree = p->second[0];
                res = p->second[2] - p->second[1] + 1;
            }
            else if (p->second[0] == degree)  res = min(res, p->second[2] - p->second[1] + 1);                      
        }
        return res;
    }
};