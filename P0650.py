class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
		# Solution 1 DP beats 52.24% 
        dp = [0,0] + range(2,n+1)            
        for i in xrange(2,n//2+1):      
            for j in xrange(2,n//i+1):
                dp[i*j] = min(dp[i*j], dp[i] + j)                
        return(dp[-1])            
                    
        
        # Solution 2 Prime Factorization beats 96.02%
		res, p = 0, 2
        while n > 1:
            while n % p == 0:
                res, n = res+p, n/p                
            p += 1
        return res	