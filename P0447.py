# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:53:50 2020

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # total number of Boomerangs
        res = 0
        # take each point as the first in the trio
        for i, (x1,y1) in enumerate(points):
            # its distance to all others
            ds = defaultdict(int)
            # calculate distance to all others
            for j, (x2,y2) in enumerate(points):
                # skip itself
                if i == j: continue
                # distance in x and y directions 
                x, y = x2-x1, y2-y1
                # total distance
                d = x*x + y*y
                # update distance counts
                ds[d] += 1
            # for each distance, the number of Boomerangs
            # is the arrangement of two
            for d in ds: res +=  ds[d] * (ds[d]-1)
        # return total number of Boomerangs 
        return(res)