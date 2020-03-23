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
        heaters = [float('-inf')] + sorted(heaters) + [float('inf')]
        res, idx = 0, 0        
        for house in sorted(houses):
            while house > heaters[idx]: idx += 1            
            res = max(res, min(house-heaters[idx-1],heaters[idx]-house) )            
        return res