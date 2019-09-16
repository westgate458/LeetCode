# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:03:58 2019

@author: Tianqi Guo
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n % 4 != 0)