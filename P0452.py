# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:27:18 2020

@author: westg
"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Solution 1 beats 95.30%: only tracks endpoints
        if not points: return 0
        points.sort(key=lambda x:x[1])        
        r, res = points[0][1], 1        
        for c, d in points[1:]:
            if c > r: res, r = res + 1, d                
        return res
        
        # Solution 2 beats 86.21%: keep track of intervals
        if not points: return 0
        points.sort()        
        a, b = points[0]
        res = 1
        for c, d in points[1:]:
            if c <= b:
                a = c
                if d < b: b = d
            else:
                res += 1
                a, b = c, d
        return res