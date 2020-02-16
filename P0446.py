# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:54:50 2020

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        dp, res = [defaultdict(int) for _ in xrange(l)], 0
        for j in xrange(1,l): 
            for i in xrange(j):
                d = A[j] - A[i]
                dp[j][d] += 1                
                if d in dp[i]:
                    res += dp[i][d]
                    dp[j][d] += dp[i][d]
        return res