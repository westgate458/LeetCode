# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:56:30 2019

@author: Tianqi Guo
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i <= j:
            m = (i + j)//2
            g = guess(m)       
            if g == 0:
                return m
            elif g == 1:
                i = m + 1
            else:
                j = m - 1