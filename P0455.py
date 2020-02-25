# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:29:30 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort() 
        res, idx, ls = 0, 0, len(s)             
        for child in g:
            while idx < ls and child > s[idx]:
                idx += 1
            if idx < len(s):
                res += 1
                idx += 1
            else:
                break         
        return res
            