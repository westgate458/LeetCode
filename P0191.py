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
        return len([c for c in str(bin(n)[2:]) if c == '1'])