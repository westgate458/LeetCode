# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:16:30 2020

@author: westg
"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """     
        # Solution 1 beats 100%: fewer additions
        t0, t1, res = -1, -1, 0       
        for t in timeSeries + [float('inf')]:
            if t < t1:
                t1 = t + duration
            else:
                res += t1 - t0
                t0, t1 = t, t + duration                
        return res
    
        # Solution 2 beats 89.13%: one-liner
        return 0 if not timeSeries else sum(map(lambda x:min(duration,x[0]-x[1]), zip(timeSeries[1:],timeSeries[:-1])))+duration