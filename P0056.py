# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:49:15 2019

@author: Tianqi Guo
"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e        
        
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        if not intervals:
            return []
        
        intervals = sorted(intervals, key = lambda x:x.start)

        i = 1
        while i <= len(intervals) - 1:
            if intervals[i].start <= intervals[i-1].end:
                num = intervals.pop(i)        
                if num.end > intervals[i-1].end:
                    intervals[i-1].end = num.end
            else:
                i = i + 1

        return intervals

intervals_nums = [[8,10],[1,3],[2,6],[15,18]]
intervals = [Interval(num[0],num[1]) for num in intervals_nums]

test = Solution()
print [[num.start,num.end] for num in test.merge(intervals)]


