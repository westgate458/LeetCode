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
        
        # length of the list
        l = len(nums)
        
        # initialize results with not found
        left = -1
        right = -1
            
        # first binary search
        # look for the start position of target
        hh = 0
        tt = l - 1
        # continue searching until endpoints meet
        while hh <= tt:
            # take median
            mm = hh + (tt - hh)/2        
            # if the median is the target
            # and the one before median is not target or median is the 0th number
            if (nums[mm] == target) and ((mm == 0) or (nums[mm - 1] != target)):
                # take the median position as starting position of target
                # terminate searching
                left = mm
                break    
            # if median larger than target                    
            if nums[mm] >= target:
                # target is in 1st half, update tail
                tt = mm - 1
                continue
            # if median smaller than target       
            if nums[mm] < target:
                # target is in 2nd half, update head
                hh = mm + 1
                continue        
            
        # second binary search
        # look for the end position of target
        hh = 0
        tt = l - 1
        # continue searching until endpoints meet
        while hh <= tt:
            # take median
            mm = hh + (tt - hh)/2   
            # if the median is the target
            # and the one after median is not target or median is the last number        
            if (nums[mm] == target) and ((mm == l - 1) or (nums[mm + 1] != target)):
                # take the median position as ending position of target
                # terminate searching
                right = mm
                break    
            # if median larger than target          
            if nums[mm] > target:
                # target is in 1st half, update tail
                tt = mm - 1
                continue
            # if median smaller than target           
            if nums[mm] <= target:
                # target is in 2nd half, update head
                hh = mm + 1
                continue
        
        # return results from the two binary searchings
        return([left,right])     

        
nums = [5,7,7,8,8,10]
target = 8       

test = Solution()
print(test.searchRange(nums,target))      