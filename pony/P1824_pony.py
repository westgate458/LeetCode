class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """        
        dp = [1,0,1,0]
        for ob in obstacles:
            dp[ob-1] = 1e9 
            dp[0], dp[1], dp[2] = min(dp[0], dp[1]+1, dp[2]+1), min(dp[0]+1, dp[1], dp[2]+1), min(dp[0]+1, dp[1]+1, dp[2])            
            dp[ob-1] = 1e9  
        return min(dp)