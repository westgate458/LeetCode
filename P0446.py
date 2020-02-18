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
        # dp[j][difference] is the number of slices ending at j that have the same difference 
        dp, res = [defaultdict(int) for _ in xrange(l)], 0
        # check sequences ending at each position
        for j in xrange(1,l): 
            # enumerate previous element
            for i in xrange(j):
                # calculate the difference
                d = A[j] - A[i]
                # update dp state: now we have one more slice that gives us current difference
                # but this can not be added to res yet because it only has two elements
                dp[j][d] += 1           
                # if current difference is also found in dp of previous element
                if d in dp[i]:
                    # now we extend all previous slices ending at i to current position j
                    # each of those extension is at east of length 3
                    # and ends up a new aithmetic slice of interest
                    res += dp[i][d]
                    # we also add those slices to dp[j] for later extension 
                    dp[j][d] += dp[i][d]
        # total number of Arithmetic Slices found
        return res