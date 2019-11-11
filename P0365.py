# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:51:02 2019

@author: Tianqi Guo
"""

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        
        if x + y < z:
            return False
        elif z == 0:
            return True
        
        while y:           
            x, y = y, x % y  
            
        return (x > 0) and (z % x == 0)
  