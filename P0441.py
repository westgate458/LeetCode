# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 22:05:22 2020

@author: Tianqi Guo
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return(int((2*n+0.25)**0.5-0.5))