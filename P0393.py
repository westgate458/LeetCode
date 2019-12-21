# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:30:40 2019

@author: Tianqi Guo
"""

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """        
        mask1, mask2, bits = 1 << 7, 1 << 6, 0               
        for num in data:    
            if num >= 248:
                return False
            b1, b2 = num & mask1, num & mask2
            if bits == 0:                
                if b1: 
                    if not b2:
                        return False
                    mask = mask1
                    while mask & num:
                        bits += 1
                        mask = mask >> 1    
                    bits -= 1            
            elif b1 and not b2:
                bits -= 1
            else:
                return False        
        return bits == 0
            