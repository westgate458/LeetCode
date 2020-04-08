# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:43:38 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        return(max(map(len,''.join(map(str,nums)).split('0'))))    