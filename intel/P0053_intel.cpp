class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        float res = nums[0];
        float s = nums[0];
        for (int i=1;i<nums.size();i++) {
            if (s < 0) s = 0; 
            s += nums[i];  
            if (s > res) res = s;            
        }
        return res;
    }
};