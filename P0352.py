# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:42:17 2019

@author: Tianqi Guo
"""

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # sorted intervals
        self.intervals = [[float('-inf'),float('-inf')],[float('inf'),float('inf')]]
        # already seen elements
        self.added = set([])
        # number of the intervals so far
        self.l = 2
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        # do not need to deal with already seen elements
        if val in self.added:
            return        
        # update seen elements
        self.added.add(val)        
        
        # find insertion position based on the first element in each interval
        i = bisect.bisect(self.intervals,[val,val])
        
        # four scenarios 
        # 1) current element can connect two already seen intervals
        if val == self.intervals[i-1][1]+1 and val == self.intervals[i][0]-1:
            # connect the two intervals
            self.intervals[i-1] = [self.intervals[i-1][0],self.intervals[i][1]]
            # remove the second interval
            del self.intervals[i]
            # update number of intervals
            self.l -= 1
        # 2) if we can extend one interval by 1 at the end
        elif val == self.intervals[i-1][1]+1:
            self.intervals[i-1][1] = val
        # 3) if we can extend one interval by 1 in the front
        elif val == self.intervals[i][0]-1:
            self.intervals[i][0] = val
        # 4) otherwise we have a new interval of only one element
        else:
            self.intervals = self.intervals[:i] + [[val,val]] + self.intervals[i:]    
            self.l += 1

        
    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """        
        # return current intervals
        return self.intervals[1:-1]
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()