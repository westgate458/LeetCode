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
        return (n > 0) and (1162261467 % n == 0)