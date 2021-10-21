class Solution {
public:
    int countPrimes(int n) {
        int res = 0;
        vector<bool> nums(n+1,true);        
        for (int i=2;i<n;i++) {
            if (nums[i]) {
                res ++;
                for (int j=i;j<(n+1)/i+1;j++) nums[i*j] = false;
            }            
        }
        return(res);
    }
};