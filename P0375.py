# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:45:53 2019

@author: Tianqi Guo
"""

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Solution 1 beats 59.00%: DP
        dp = [[0] * n for _ in xrange(n)]
        # length of interval
        for s in xrange(1,n):
            # left number
            for l in xrange(n-s):
                # right number
                r = l + s 
                dp[l][r] = min(l+dp[l+1][r],dp[l][r-1]+r) + 1
                # break point 
                for m in xrange(l+1,r):
                    dp[l][r] = min(dp[l][r], max(dp[l][m-1],dp[m+1][r])+m+1)
        return dp[0][-1]
    
        # Solution 2 beats 5.11%: DFS
        self.d = {}
        def DFS(l,r):
            if l >= r:
                return 0
            elif (l,r) in self.d:
                return self.d[(l,r)] 
            self.d[(l,r)] = float('inf')
            for m in xrange(l,r+1):
                self.d[(l,r)] = min(self.d[(l,r)], max(DFS(l,m-1),DFS(m+1,r)) + m)
            return self.d[(l,r)]
        return DFS(1,n)