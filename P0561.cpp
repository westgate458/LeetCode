class Solution {
//nums at odd positions after sorting
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end(),greater<int>());
        int res = 0;
        for (int i=1; i<nums.size(); i+=2)  res += nums[i];        
        return res;
    }
};