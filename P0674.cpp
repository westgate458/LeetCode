class Solution {
// simply scan whole sequence
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int pre = INT_MIN, res = 0, l = 0;       
        for (auto num : nums) {
            if (pre<num) l ++;            
            else {
                if (l > res) res = l;  
                l = 1;
            }
            pre = num;
        }
        return max(res, l);
    }
};