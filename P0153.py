# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:13:35 2019

@author: Tianqi Guo
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        # head and tail pointers for binary search
        h, t = 0, len(nums) - 1        
        # continue searching until two pointers meet
        while h <= t:
            # if head no larger than tail
            if nums[h] <= nums[t]:
                # current searching segment is sorted
                # return the minimum number, which is the head
                return nums[h]            
            # take the midpoint
            m = (h + t)//2     
            # if head is larger than midpoint
            if nums[h] > nums[m]:                
                # the 2nd half is sorted, search the 1st half
                t = m
            # if head is smaller than midpoint
            else:          
                # the 1st half is sorted, search the 2nd half
                h = m + 1

nums = [3,4,5,1,2]  
nums = [4,5,6,7,0,1,2]       
nums = [2, 1]
nums = [3, 1, 2]
test = Solution()
print test.findMin(nums)
                
                
                
            