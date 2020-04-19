# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:43:26 2020

@author: Tianqi Guo
"""

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        # start with first digit
        i, s = 0, [1]        
        # add more digits until desired length is met
        while len(s) < n:            
            # the last digit of the string is current number
            # it needs to appear s[i] times, so we append more
            s += [s[-1]] * (s[i]-1)                     
            # next digit to append is different from current last number
            s += [s[-1]^3] 
            # move on to next occurance counter
            i += 1       
        # first n digits are required, and see how many 1's are there
        return(s[:n].count(1))