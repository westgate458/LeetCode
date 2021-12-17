"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
       
        n = 0        
        pre = -1
        res = []
        for t, a in sorted([(i.start,-1) for p in schedule for i in p] + [(i.end,+1) for p in schedule for i in p]):
            n -= a 
            if n == 0:
                pre = t
            elif pre != -1:
                res.append(Interval(pre,t))
                pre = -1
         
        return res