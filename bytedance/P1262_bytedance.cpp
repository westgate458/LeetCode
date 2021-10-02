class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        int l = nums.size();
        vector<vector<int>> dp(l+1,vector<int>(3,0));                
        int m;
        for (int i=0;i<l;i++) {   
            
            dp[i+1][0] = dp[i][0];
            dp[i+1][1] = dp[i][1];
            dp[i+1][2] = dp[i][2];   
            
            m = (nums[i]+dp[i][0])%3;                     
            dp[i+1][m] = max(dp[i+1][m], dp[i][0]+nums[i]);
            
            m = (nums[i]+dp[i][1])%3;                  
            dp[i+1][m] = max(dp[i+1][m], dp[i][1]+nums[i]);
            
            m = (nums[i]+dp[i][2])%3;                  
            dp[i+1][m] = max(dp[i+1][m], dp[i][2]+nums[i]);                        
           
        }
        return(dp[l][0]);
    }
};