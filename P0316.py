# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:52:26 2019

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """        
        d, v = defaultdict(int), defaultdict(bool)

        for idx, c in enumerate(s):
            d[c] += 1
            v[c] = False        

        res = '0'
        for c in s:
            d[c] -= 1
            if v[c]:
                continue
            v[c] = True                
            while c < res[-1] and d[res[-1]] > 0:                
                v[res[-1]] = False
                res = res[:-1]
            res += c
        
        return(res[1:])