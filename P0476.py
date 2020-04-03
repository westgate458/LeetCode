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
        # bits: from binary representation
        # res: final complement
        bits, res = [], 0
        # take each bit from binary representation
        while num:    
            # take current lowest bit
            bits.append(1 - (num&1))
            # right shift by 1
            num >>= 1 
        # compose the complement in reversed order
        for bit in bits[::-1]: 
            res = (res<<1) + bit 
        return res