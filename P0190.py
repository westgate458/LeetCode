# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:16:16 2019

@author: Tianqi Guo
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):       
        return int(str(bin(n))[2:].zfill(32)[::-1] ,2)