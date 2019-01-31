# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 20:57:16 2019

@author: Tianqi Guo
"""
import math

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # the number of unique paths
        # is the number of total permutations of
        # (m-1) right moves and (n-1) down moves
        # without considering the orders within each categary
        
        return math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))
        
m = 3
n = 3

test = Solution()
print(test.uniquePaths(m,n))




