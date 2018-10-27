# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:47:38 2018

@author: Tianqi Guo
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """ 
        
        l = len(height) 
        # initial maximum area set to 0
        m = 0        
        # start searching from both end points
        left = 0
        right = l - 1
        # continue searching until all points are visited
        # each time shorten the bottom span by one and update search range
        while left != right:
            # the area formed by current end points 
            a = (right - left) * min(height[right],height[left])
            # update maximum area
            m = max(m,a)
            # if a larger area is to exist with a shorter bottom span
            # it must occur with the higher end point between left&right
            # update end point and search range accordingly
            if height[right] > height[left]:
                left = left + 1
            else:
                right = right - 1
        return m    
        
height = [1,8,6,2,5,4,8,3,7]
test = Solution()
print(test.maxArea(height))