# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:36:35 2019

@author: Tianqi Guo
"""

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """                 
        # by trying n = 1000, it seems like all square numbers are the ones left on
        # the number of square numbers below n is now int(n**0.5)
        return int(n**0.5)