# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:52:06 2019

@author: Tianqi Guo
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1 beats 94.48%: empirical observation
        # from observation: lets have as many 3's as possible
        # stop breaking when meet 4 since 1 * 3 < 4, but 2 * 3 > 5
        # deal with trivial cases
        if n==2: return 1
        if n==3: return 2        
        # check how many 3's are there
        a, b = n//3, n%3        
        # if final remainder is 3 or 4, step back and do not break
        if b <= 1: return 3 ** (a-1) * (b+3)
        # otherwise just take the product of all the 3's and the final remainder
        return 3 ** a * b
        
        # Solution 2 beats 98.66%: DP
        dp = [0] * (n+1)
        dp[1] = 1        
        def DFS(n):            
            if dp[n] == 0:       
                for m in xrange(1,n//2+1):                    
                    dp[n] = max(dp[n], m * max(DFS(n-m),n-m))            
            return dp[n]                
        return DFS(n)
        
        