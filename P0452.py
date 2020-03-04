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
        # deal with trivial case
        if not points: return 0
        # sort all intervals (balloons) by the endpoints
        points.sort(key=lambda x:x[1])        
        # r: current right-most position for current arrow to shoot
        # res: number of arrows to shoot
        r, res = points[0][1], 1        
        # check each balloon
        for c, d in points[1:]:
            # if the left point is smaller than r
            # now we shoot the previous arrow in the range [c, r]
            # we can still burst all previous balloons
            # if the left point is larger than r
            # the previous arrow can not burst current balloon
            # we shoot a new arrow in the range [c, d]
            # update res and r
            if c > r: res, r = res + 1, d                
        # return the number of arrows
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