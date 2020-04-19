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
        # steps:
        # 1) join the list to form a string
        # 2) split the string by 0
        # 3) check length of each segments of 1's
        # 4) find the max length
        return(max(map(len,''.join(map(str,nums)).split('0'))))    