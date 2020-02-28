# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:58:20 2020

@author: Tianqi Guo
"""

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """        
        pigs, base = 0, 1+minutesToTest//minutesToDie        
        while (base**pigs < buckets): pigs += 1
        return pigs