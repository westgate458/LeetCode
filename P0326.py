# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:46:30 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # cheat by checking
        # 1) negative values are not power of three
        # 2) any power of three should be a factor of the max test case
        return (n > 0) and (1162261467 % n == 0)