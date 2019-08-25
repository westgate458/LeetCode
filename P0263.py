# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:26:56 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num < 1:
            return False
        
        while num%2 == 0:
            num /= 2
            
        while num%3 == 0:
            num /= 3
            
        while num%5 == 0:
            num /= 5
        
        return num == 1