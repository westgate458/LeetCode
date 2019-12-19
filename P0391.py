# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 22:50:17 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        points = set()
        areas = 0
        for a, b, c, d in rectangles:
            areas += (c-a)*(d-b)
            if (a,b) in points:
                points.remove((a,b))
            else:
                points.add((a,b))
            if (c,d) in points:
                points.remove((c,d))
            else:
                points.add((c,d))
            if (a,d) in points:
                points.remove((a,d))
            else:
                points.add((a,d))
            if (c,b) in points:
                points.remove((c,b))
            else:
                points.add((c,b))
        if len(points) != 4:
            return False
        xs, ys = [p[0] for p in points], [p[1] for p in points]
        area = (max(xs) - min(xs)) * (max(ys) - min(ys))
        if areas == area:
            return True
        else:
            return False      