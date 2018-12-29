# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:23:59 2018

@author: Tianqi Guo
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # number of elements
        l = len(height)
        
        # two predefined arrays that store
        # the highest elevation on the left of the current
        # the highest elevation on the right of the current
        pre = [0 for x in range(l)]
        pst = [0 for x in range(l)]
        
        # running highest elevations from left and from right
        # over the iteration
        h_l = 0
        h_r = 0
        
        # iterate over all elements
        # i-th from left, (l-1-i)-th from right
        for i in range(l):    
            # store the running highest elevations to the arrays           
            pre[i] = h_l
            pst[l-1-i] = h_r
            # update the running highest elevations
            # based on the current elevations
            if height[i] > h_l:
                h_l = height[i]  
            if height[l-1-i] > h_r:
                h_r = height[l-1-i]  
        
        # answer of the water volume
        ans = 0        
        # for all heights from left to right
        for i in range(l):
            
            # find the lower 'highest elevation' between on the left and right
            if pre[i] <= pst[i]:
                h = pre[i]
            else:
                h = pst[i]        
            
            # if the current elevation is lower 
            # than highest elevations on both sides
            if height[i] < h:
                # the amount of water trapped at current position
                # is the elevation difference x 1
                ans = ans + h - height[i]
        
        # return answer
        return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]    
test = Solution()
print(test.trap(height))    