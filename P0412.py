# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:10:45 2020

@author: Tianqi Guo
"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """        
        l = len(A)
        dp = [0] * l
        for i in xrange(2,l):          
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
        return(sum(dp))
