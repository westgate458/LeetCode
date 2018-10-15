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
        m = 0
        left = 0
        right = l - 1
        while left != right:
            a = (right - left) * min(height[right],height[left])
            m = max(m,a)
            if height[right] > height[left]:
                left = left + 1
            else:
                right = right - 1
        return m    
        
height = [1,8,6,2,5,4,8,3,7]
test = Solution()
print(test.maxArea(height))