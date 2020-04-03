# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:20:12 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """ 
        # we sort both heaters and houses from left to right
        heaters = [float('-inf')] + sorted(heaters) + [float('inf')]
        # res: max radius
        # idx: current heater under consideration
        res, idx = 0, 0        
        # we try to cover each house
        for house in sorted(houses):
            # we look for the first heater that is on the right of current house
            while house > heaters[idx]: idx += 1            
            # first, for two heaters adjacent to current house, we find the closer one
            # then, this distance is the smallest radius to get current house covered
            # finally, update res if this radius is larger
            res = max(res, min(house-heaters[idx-1],heaters[idx]-house))            
        # minimum radius to get all houses covered
        return res