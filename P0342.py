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
        if (num <= 0):
            return False
        while (num != 1):
            if (num % 4 != 0):
                return False
            num = num // 4
        return True
        
        # Solution 2 beats 78.94%: cheat
        import math
        if num <= 0:
            return False
        num = math.log(float(num),4)        
        return abs(num - round(num)) < 1e-10