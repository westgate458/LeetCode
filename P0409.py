# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:53:56 2020

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """        
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        res = mid = 0        
        for c in d:
            res += d[c]//2 *2
            mid = mid or d[c]%2
        return res+mid
            