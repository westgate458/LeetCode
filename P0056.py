# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:49:15 2019

@author: Tianqi Guo
"""

# definition of the interval
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
        
        # deal with trivial case
        if not intervals:
            return []
        
        # sort the intervals according to the start point in ascending order
        intervals = sorted(intervals, key = lambda x:x.start)
        
        # start from the 2nd interval
        i = 1
        # merge until the last interval
        while i <= len(intervals) - 1:
            # if the start point of the current interval
            # is before the end point of the previous interval
            if intervals[i].start <= intervals[i-1].end:
                # current interval need to be merged
                num = intervals.pop(i)        
                # if the end point of the current interval
                # is after the end point of the previous interval
                if num.end > intervals[i-1].end:
                    # update the end point of previous inverval
                    intervals[i-1].end = num.end
            # if there is no overlap
            else:
                # do not merge and move on to next interval
                i = i + 1
        
        # return the merged intervals
        return intervals

intervals_nums = [[8,10],[1,3],[2,6],[15,18]]
intervals = [Interval(num[0],num[1]) for num in intervals_nums]

test = Solution()
print [[num.start,num.end] for num in test.merge(intervals)]


