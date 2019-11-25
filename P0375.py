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
        # dp[left number][right number]: the amount of money to guarantee a win in this interval
        dp = [[0] * n for _ in xrange(n)]
        # build dp from bot to top
        # length of interval
        for s in xrange(1,n):
            # left number
            for l in xrange(n-s):
                # right number
                r = l + s 
                # initialize from guessing l or r
                dp[l][r] = min(l+dp[l+1][r],dp[l][r-1]+r) + 1
                # break point: next number to guess
                for m in xrange(l+1,r):
                    # min-max problem
                    # if we guess m, then the money needed is m plus
                    # the larger from the money needed from
                    # guess in left interval or guess in right interval
                    # then compare with previous break point
                    # to choose a lower amount of money required 
                    dp[l][r] = min(dp[l][r], max(dp[l][m-1],dp[m+1][r])+m+1)
        # the money required for the entire range
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