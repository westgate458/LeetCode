# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:03:56 2019

@author: Tianqi Guo
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Fibonacci sequence
        
        # first two terms of the sequence
        f = [1,1]
        # find the terms sequentially
        for i in range(2,n+1):
            # each term is the sum of the previous two terms
            f.append(f[i-2] + f[i-1])
        
        # return the last term
        return f[-1]


n = 4
test = Solution()
print test.climbStairs(n)