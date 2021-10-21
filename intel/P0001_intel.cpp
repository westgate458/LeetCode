class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> h;
        for (int i=0;i<nums.size();i++) {            
            if (h[target-nums[i]]>0) {
                vector<int> vect{h[target-nums[i]]-1,i};
                return(vect);
            }
            h[nums[i]] = i+1;            
        }
        vector<int> vect{0,0};
        return(vect);        
    }
};