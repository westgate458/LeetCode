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
        
        # carry and result
        c, res = 0, 1        
        
        # max test case is 8-bit
        for _ in xrange(8):
            
            # take the right-most digits
            x, y = a & 1, b & 1
            
            # move on to next digits by moving two number -> 1
            # record current result in the left-most digit of res
            a, b, res = a >> 1, b >> 1, (res >> 1) | (x ^ y ^ c) * 0x80        
            # update the carry
            c = (x & y) | (x & c) | (y & c)        
        # deal with negative cases
        if res & 0x80:
            res |= - (1 << 8)
        # return result
        return res
        