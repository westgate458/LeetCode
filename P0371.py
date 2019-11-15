# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:52:39 2019

@author: Tianqi Guo
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        c, res = 0, 1        
        
        for _ in xrange(8):
            
            x, y = a & 1, b & 1
            
            a, b, res = a >> 1, b >> 1, (res >> 1) | (x ^ y ^ c) * 0x80        
                
            c = (x & y) | (x & c) | (y & c)        
        
        if res & 0x80:
            res |= - (1 << 8)
           
        return res
        