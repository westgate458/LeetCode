class Solution {
public:
	// sort and compare
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> t(nums);        
        sort(t.begin(), t.end());
        int i=0, j=nums.size()-1;
        while ((i < nums.size()) && (nums[i] == t[i])) i++;       
        while ((j > i) && (nums[j] == t[j]))  j--;
        if (i == j) return 0;
        else return j-i+1;
    }
};