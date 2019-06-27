# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 21:39:54 2019

@author: westg
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """    
        # steps:
        # 1) convert number to binary
        # 2) convert to string
        # 3) only keep '1's
        # 4) count the number of 1 bits
        return len([c for c in str(bin(n)) if c == '1'])