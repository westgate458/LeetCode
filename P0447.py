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
        res = 0
        for i, (x1,y1) in enumerate(points):
            ds = defaultdict(int)
            for j, (x2,y2) in enumerate(points):
                if i == j:
                    continue
                x, y = x2-x1, y2-y1
                d = x*x + y*y
                ds[d] += 1
            for d in ds:
                res +=  ds[d] * (ds[d]-1)
        return(res)