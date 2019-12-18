# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:00:25 2019

@author: Tianqi Guo
"""

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        # each time after elimination, gap between adjacent numbers double
        # we only keep track of the smallest number
        # l2r tracks the order
        step, l, l2r = 1, 1, True
        
        # continue elimination until only one number is left
        while n > 1:                        
            # if from left to right, first number is eliminated
            # if from right to left, first number is eliminated when there are odd numbers left
            if l2r or (n % 2 == 1):                
                # update the smallest number
                l += step                   
            # double the gap, reverse the order, and remaining numbers halved
            step, l2r, n = 2*step, not l2r, n//2
        # return the final one left
        return l