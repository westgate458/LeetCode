# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:04:32 2020

@author: Tianqi Guo
"""

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # deal with trivial case
        if not num:
            return '0'
        # two’s complement method for negative numbers
        elif num<0:
            num += 2**32        
        # resulting hex representation
        res = ''        
        # continue until all digits are dealt with
        while num:
            # move on to next byte
            num, byte = divmod(num, 16)            
            # update result with current byte
            res += '0123456789abcdef'[byte]
        # res in reversed order is the hex representation
        return(res[::-1])