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
        # deal with trivial case
        if not intervals: return 0
        # c: number of intervals we decide to keep
        # e: the end point of previous interval
        c, e = 0, float('-inf')
        # we sort intervals based on their end points
        for a, b in sorted(intervals, key=lambda x: x[1]):
            # if start point of current interval is after previous end point
            # we simply keep this interval and update the end point
            if a >= e: c, e = c+1, b
            # greedy: e.g. 1-4, 3-6, 5-7, we would like to keep 1-4, and 5-7
            # so 3-6 is discarded because 3 is before 4
        # difference between total intervals and number of remaining intervals
        # is the number needs to be removed
        return len(intervals) - c