# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 18:02:06 2020

@author: Tianqi Guo
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """        
        if not intervals: return 0
        c, e = 0, float('-inf')
        for a, b in sorted(intervals, key=lambda x: x[1]):
            if a >= e: c, e = c+1, b
        return len(intervals) - c