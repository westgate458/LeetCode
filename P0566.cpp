class Solution {
public:
	// fill elelemts in array one by one
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {        
        if (nums.size() * nums[0].size() != r * c) return nums;        
        vector<vector<int>> res(r,vector<int>(c));
        int i = 0, j = 0;        
        for (auto row:nums) {
            for (auto num:row) {
                res[i][j] = num;                
                if (++j == c)  j = 0, i ++; 
            }            
        }        
        return res;
    }
};