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
        if not num:
            return '0'
        elif num<0:
            num += 2**32        
        res = ''        
        while num:
            num, byte = divmod(num, 16)            
            res += '0123456789abcdef'[byte]
        return(res[::-1])