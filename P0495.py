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
        # t0: start of current intoxication
        # t1: end of current intoxication
        # res: total duration of intoxication
        t0, t1, res = -1, -1, 0       
        # check each attack time point, add inf at end so the last intoxication definitely ends
        for t in timeSeries + [float('inf')]:
            # if current time is before the end of current intoxication
            if t < t1:
                # current attack simply extend current intoxication
                t1 = t + duration
            # if current time is before the end of previous intoxication
            else:
                # previous intoxication has ended, start a new one
                # update total duration
                res += t1 - t0
                # update start and end time
                t0, t1 = t, t + duration                
        # total duration of intoxication
        return res
    
        # Solution 2 beats 89.13%: one-liner
        return 0 if not timeSeries else sum(map(lambda x:min(duration,x[0]-x[1]), zip(timeSeries[1:],timeSeries[:-1])))+duration