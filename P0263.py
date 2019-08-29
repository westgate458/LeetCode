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
        
        # deal with trivial cases
        if num < 1:
            return False
        
        # remove all prime factors: 2 
        while num%2 == 0:
            num /= 2
        # remove all prime factors: 3    
        while num%3 == 0:
            num /= 3
        # remove all prime factors: 5     
        while num%5 == 0:
            num /= 5
        # if the remaining is not 1, it means num has other prime factors
        # then it is not ungly
        return num == 1