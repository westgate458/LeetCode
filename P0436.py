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
        ll = xrange(len(intervals))
        t = sorted(zip([a[0] for a in intervals], ll))
        aa, ii = [a[0] for a in t], [a[1] for a in t] + [-1]
        return([ii[bisect.bisect_left(aa, intervals[idx][1])] for idx in ll])