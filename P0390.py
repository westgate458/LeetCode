# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:00:25 2019

@author: Tianqi Guo
"""

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        step, l, l2r = 1, 1, True
                
        while n > 1:                        
            if l2r or (n % 2 == 1):                
                l += step                        
            step, l2r, n = 2*step, not l2r, n//2
        return l