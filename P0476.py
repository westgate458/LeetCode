# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:21:41 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bits, res = [], 0
        while num:            
            bits.append(1 - (num&1))
            num >>= 1 
        for bit in bits[::-1]: 
            res = (res<<1) + bit 
        return res