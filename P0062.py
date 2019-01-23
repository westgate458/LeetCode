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
        
        return math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))
        
m = 7
n = 3

test = Solution()
print(test.uniquePaths(m,n))




