class Solution {
	// sort and compare two cases
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());        
        int l = nums.size(); 
        return max(nums[l-3] * nums[l-2], nums[0] * nums[1])* nums[l-1];
    }
};