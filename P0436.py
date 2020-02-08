# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:11:19 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # xrange for later iterations
        ll = xrange(len(intervals))        
        # sort intervals by the starting points, and record their original positions
        t = sorted(zip([a[0] for a in intervals], ll))
        # aa: the sorted starting points
        # ii: their original positions, plus [-1] at the end for the '-1' default result in case no 'right interval' is found
        aa, ii = [a[0] for a in t], [a[1] for a in t] + [-1]
        # steps:
        # 1) try to bisect each end points of the intervals into the sorted starting points
        # 2) find the position where it should be inserted, then the starting point on the right is the 'right interval'
        # 3) the original position of the 'right interval' is in ii
        return([ii[bisect.bisect_left(aa, intervals[idx][1])] for idx in ll])