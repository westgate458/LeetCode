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
        
        # pad heights to avoid conditional statements
        heights = [0] + heights + [0]
        # number of elements
        l = len(heights)
        
        # indices of the 'increasing height list'
        ps = [0]
        # maximum area so far
        area = 0
        
        # traverse the height list
        for p in range(1,l):
            
            # if the current height smaller than 
            # previous height in the 'increasing height list'
            while heights[p] < heights[ps[-1]]:
                # previous height in the 'increasing height list'
                # can not be contained in an area starting from current p
                # remove its index from the 'increasing height list'
                pp = ps.pop()    
                # the area forms with its height
                # spans between two heights just lower than it
                # the left limit is the current last index in the 'increasing height list'
                # the right limit is the current p
                # calculate the area
                area_pp = (p - ps[-1] - 1) * heights[pp]
                # update the maximum area so far
                if area_pp > area:
                    area = area_pp 
            
            # place current index into the increasing height list
            # after all previous heights higher than current one
            # have been removed from the list
            ps.append(p)
        
        # return the maximum area
        return area
      
heights = [1]
test = Solution()
print test.largestRectangleArea(heights)