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
        # head and tail pointers for binary search
        h, t = 0, n - 1        
        # continue searching till two pointers meet  
        # thats when head is the first bad version
        while h <= t:
            # the middle point
            m = (h + t)/2    
            # if the middle point is bad, then all versions after middle is bad
            if isBadVersion(m):
                # search the first half
                t = m - 1
            # if the middle point is good, then all versions before middle is good
            else:
                # search the second half
                h = m + 1
        # return the first bad version
        return h
                    
        