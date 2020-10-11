class Solution {
public:
	// sliding window
    double findMaxAverage(vector<int>& nums, int k) {
        double s = 0.0;
        for (int i=0;i<k;i++) s += nums[i];
        double m = s;
        for (int i=k;i<nums.size();i++) {            
            s += nums[i] - nums[i-k];
            if (s>m)  m = s;                       
        }
        return m/k;
    }
};