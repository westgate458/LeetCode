# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:01:43 2019

@author: Tianqi Guo
"""
# definition of the interval
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
        # start and end points of the new interval
        s = newInterval.start
        e = newInterval.end
        
        # list that store the intervals on the left and right 
        # of the new interval
        l = []
        r = []
        
        # check each interval in the original list
        for interval in intervals:
            # if there is no overlap
            if interval.end < s:
                # add current interval to the left set
                l.append(interval)
            elif interval.start > e:
                # add current interval to the right set
                r.append(interval)
            # if there is overlap
            else:
                # merge the current interval with the new interval
                if interval.start < s:
                    # update the start point of the new interval
                    s = interval.start
                if interval.end > e:
                    # update the end point of the new interval
                    e = interval.end           
        
        # return the list after insertion
        return l + [Interval(s,e)] + r

intervals_nums = [[1,5]]

intervals = [Interval(num[0],num[1]) for num in intervals_nums]

newInterval_nums = [1,7]
newInterval = Interval(newInterval_nums[0],newInterval_nums[1])

test = Solution()
print [[num.start,num.end] for num in test.insert(intervals,newInterval)]
