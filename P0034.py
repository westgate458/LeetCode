# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:36:59 2018

@author: Tianqi Guo
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = len(nums)
        
        left = -1
        right = -1
            
        hh = 0
        tt = l - 1
        
        while hh <= tt:
            
            mm = hh + (tt - hh)/2        
                    
            if (nums[mm] == target) and ((mm == 0) or (nums[mm - 1] != target)):
                left = mm
                break    
                    
            if nums[mm] >= target:
                tt = mm - 1
                continue
                    
            if nums[mm] < target:
                hh = mm + 1
                continue
        
        hh = 0
        tt = l - 1
        
        while hh <= tt:
            
            mm = hh + (tt - hh)/2   
                    
            if (nums[mm] == target) and ((mm == l - 1) or (nums[mm + 1] != target)):
                right = mm
                break    
                    
            if nums[mm] > target:
                tt = mm - 1
                continue
                    
            if nums[mm] <= target:
                hh = mm + 1
                continue
        
        return([left,right])     

        
nums = [5,7,7,8,8,10]
target = 8       

test = Solution()
print(test.searchRange(nums,target))      