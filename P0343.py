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
        if n==2: return 1
        if n==3: return 2        
        a, b = n//3, n%3        
        if b <= 1: return 3 ** (a-1) * (b+3)
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
        
        