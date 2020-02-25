# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:30:24 2020

@author: Tianqi Guo
"""

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """        
        res, s = 0, collections.defaultdict(int)        
        for a in A:
            for b in B:
                s[a+b] += 1
        for c in C:
            for d in D:
                if -(c+d) in s:
                    res += s[-c-d]
        return res