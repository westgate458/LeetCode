# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:52:30 2019

@author: Tianqi Guo
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        heights = [0] + heights + [0]
        l = len(heights)
        
        ps = [0]
        area = 0

        for p in range(1,l):
            
            while heights[p] < heights[ps[-1]]:
                pp = ps.pop()            
                area_pp = (p - ps[-1] - 1) * heights[pp]
                if area_pp > area:
                    area = area_pp 

            ps.append(p)
        
        return area
      
heights = [1]
test = Solution()
print test.largestRectangleArea(heights)