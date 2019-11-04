#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:47:00 2019

@author: Tianqi Guo
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        # Solution 1 beats 99.30%: simple while loop
        # deal with trivial case
        if (num <= 0):
            return False
        # terminate loop when remaining number is just 1
        while (num != 1):
            # if current number is not a power of 4
            if (num % 4 != 0):
                # then the original number is not a power of 4
                return False
            # move on
            num = num // 4
        # if final number is 1 then the original number is a power of 4
        return True
        
        # Solution 2 beats 78.94%: cheat
        import math
        if num <= 0:
            return False
        num = math.log(float(num),4)        
        return abs(num - round(num)) < 1e-10