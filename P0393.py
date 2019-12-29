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
        # mask1, mask2: to obtain the highest two bits
        # bits: number of 1 bits remaining to check
        mask1, mask2, bits = 1 << 7, 1 << 6, 0     
        # check each number          
        for num in data:   
            # valid number should be smaller than 11111000
            if num >= 248:
                return False
            # the highest two bits
            b1, b2 = num & mask1, num & mask2
            # if current byte should be a new character
            if bits == 0:                
                # if highest bit is 1
                if b1: 
                    # since (10) marks a continued number
                    if not b2:
                        # not valid expression
                        return False
                    # then check each bit
                    # number of 1's in current number
                    # is the number of all bytes for current character
                    mask = mask1
                    # stop when 0 is found
                    while mask & num:
                        # update bit counter                        
                        bits += 1
                        # move the masked bit
                        mask = mask >> 1    
                    # remaining bytes afterwards
                    bits -= 1        
            # if current byte starts with (10)
            # then it is continued from last one 
            elif b1 and not b2:
                # update byte count
                bits -= 1
            # all other situations will be invalid expression
            else:
                return False     
        # a valid expression should end with no remaining bytes to expect aftewards
        return bits == 0
            