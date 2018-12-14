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
        l = len(height)

        pre = [0 for x in range(l)]
        pst = [0 for x in range(l)]

        h_l = 0
        h_r = 0

        for i in range(l):    
            pre[i] = h_l
            pst[l-1-i] = h_r
            if height[i] > h_l:
                h_l = height[i]  
            if height[l-1-i] > h_r:
                h_r = height[l-1-i]  

        ans = 0        

        for i in range(l):
            if pre[i] <= pst[i]:
                h = pre[i]
            else:
                h = pst[i]        

            if height[i] < h:
                ans = ans + h - height[i]
        
        return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]    
test = Solution()
print(test.trap(height))    