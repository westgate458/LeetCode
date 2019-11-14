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
        # from Bezout's Lemma
        # if z is to be formed by linear combinations of x and y
        # i.e. z = ax + by
        # then z must be a multiple of GCD(x, y)
        # i.e. z % GCD(x, y) == 0
        
        # deal with trivial case: impossible
        if x + y < z:
            return False
        # deal with trivial case: no need to measure
        elif z == 0:
            return True
        # get GCD(x, y)
        while y:           
            x, y = y, x % y  
        # the GCD exists and z is a multiple of the GCD            
        return (x > 0) and (z % x == 0)
  