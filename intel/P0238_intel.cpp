class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prod = 1, zero_id = -1;        
        vector<int> res(nums.size());
        for (int i=0;i<nums.size();i++) {
            if (nums[i]!=0) prod = prod * nums[i]; 
            else if(zero_id != -1) return(res);
            else zero_id = i;
        }               
        if (zero_id == -1) {
            for (int i=0;i<nums.size();i++) res[i] = prod/nums[i];                
        }
        else res[zero_id] = prod;     
        return res;
    }
};