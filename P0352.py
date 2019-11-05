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
        self.intervals = [[float('-inf'),float('-inf')],[float('inf'),float('inf')]]
        self.added = set([])
        self.l = 2
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.added:
            return        
        
        self.added.add(val)        
 
        i = bisect.bisect(self.intervals,[val,val])
        
        # now val < self.intervals[i][0]
        if val == self.intervals[i-1][1]+1 and val == self.intervals[i][0]-1:
            self.intervals[i-1] = [self.intervals[i-1][0],self.intervals[i][1]]
            del self.intervals[i]
            self.l -= 1
        elif val == self.intervals[i-1][1]+1:
            self.intervals[i-1][1] = val
        elif val == self.intervals[i][0]-1:
            self.intervals[i][0] = val
        else:
            self.intervals = self.intervals[:i] + [[val,val]] + self.intervals[i:]    
            self.l += 1

        
    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """        
        return self.intervals[1:-1]
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()