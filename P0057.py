# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:01:43 2019

@author: Tianqi Guo
"""
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e        
        
class Solution(object):
    def insert(self, intervals,newInterval):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        s = newInterval.start
        e = newInterval.end
        
        l = []
        r = []
        
        for interval in intervals:
            if interval.end < s:
                l.append(interval)
            elif interval.start > e:
                r.append(interval)
            else:
                if interval.start < s:
                    s = interval.start
                if interval.end > e:
                    e = interval.end           

        return l + [Interval(s,e)] + r

intervals_nums = [[1,5]]

intervals = [Interval(num[0],num[1]) for num in intervals_nums]

newInterval_nums = [1,7]
newInterval = Interval(newInterval_nums[0],newInterval_nums[1])

test = Solution()
print [[num.start,num.end] for num in test.insert(intervals,newInterval)]
