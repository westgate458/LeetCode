class Solution {
public:
	// look at ill position and try possible rearrangements
    bool checkPossibility(vector<int>& nums) {
        bool flag = false;        
        for (int i=0; i<nums.size()-1; i++) {
            if (nums[i] > nums[i+1]) {
                if (flag) return false;                
                else {                    
                    if ((i==0) || (nums[i-1]<=nums[i+1]) || (i==nums.size()-2) || (nums[i]<=nums[i+2])) {
                        flag = true;                        
                    }
                    else return false;                                       
                }
            }
        }
        return true;        
    }
};