# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:48:02 2020

@author: Tianqi Guo
"""

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 9
        s = 2
        while True:            
            R = int(str(10**n-s)[::-1])
            if s**2-4*R >= 0:
                x = (s + (s**2-4*R)**0.5)/2
                if x.is_integer(): return (10**(2*n) - s*10**n + R)%1337
            s += 1
        