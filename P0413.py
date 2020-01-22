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
        # length of the list
        l = len(A)
        # dp: number of all arithmetic sequences ending at current position
        dp = [0] * l
        # check each number
        for i in xrange(2,l):          
            # see if current number is an extension of previous arithmetic sequence
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                # if yes, number of all arithmetic sequences ending at current position
                # includes all previous ones + current number
                # and one more (excluding the first number of previous sequence of length 3)
                dp[i] = dp[i-1] + 1
        # total number is the summation
        return(sum(dp))
