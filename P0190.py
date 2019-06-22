# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:16:16 2019

@author: Tianqi Guo
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):  
        # steps:
        # 1) bin - convert to binary
        # 2) str - convert to string
        # 3) [2:] - remove preceeding '0b'
        # 4) zfill - pad string with 0's on the left
        # 5) [::-1] - reverse string
        # 6) int - convert back to 10-base
        return int(str(bin(n))[2:].zfill(32)[::-1] ,2)