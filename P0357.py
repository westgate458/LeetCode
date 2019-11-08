# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:54:02 2019

@author: Tianqi Guo
"""

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """                
        if not n : return 1
        if n > 10: n = 10                
        f = [10] + [9] * (n-1)        
        for i in xrange(1, n):            
            c = 10 - i
            while c < 10:
                f[i] *= c
                c += 1
        return sum(f)