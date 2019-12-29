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
        # set of remaining points
        points = set()
        # the total area of all tiles
        areas = 0
        # check each tile
        for a, b, c, d in rectangles:
            # update area
            areas += (c-a)*(d-b)
            # for each of the cornor points            
            if (a,b) in points:
                # remove it from set if it already exists
                # i.e. two tiles share this cornor point
                points.remove((a,b))
            else:
                # add it to the set if not seen                
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
        # if all tiles perfectly line up
        # each internal cornor point should show up for 4 times
        # so they all cancel out except for the 4 most outside ones
        if len(points) != 4:
            return False
        # find the 4 most outside ones, and calculate the largest possible area
        xs, ys = [p[0] for p in points], [p[1] for p in points]
        area = (max(xs) - min(xs)) * (max(ys) - min(ys))
        # if all tiles perfectly line up
        # the sum of all tile areas shoule equal to the largest possible area
        if areas == area:
            return True
        else:
            return False      