class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return len(s)
        l = len(s)
        dp = [[1] * l for _ in range(l)] 
            
        for i in range(l-1):            
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
                
        for ll in range(3,l+1):           
            for i in range(l-ll+1):               
                j = i + ll - 1                             
                if s[i] == s[j]:                    
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])                  
        return dp[0][-1]
                    
                
        