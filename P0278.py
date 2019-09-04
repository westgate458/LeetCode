# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:37:25 2019

@author: Tianqi Guo
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        h, t = 0, n - 1        
        while h <= t:
            m = (h + t)/2            
            if isBadVersion(m):
                t = m - 1
            else:
                h = m + 1
        return h
                    
        