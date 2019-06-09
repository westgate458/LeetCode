# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:50:17 2019

@author: Tianqi Guo
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # pad nums with -Inf so peaks on ends can be picked up
        nums = [-float('inf')] + nums + [-float('inf')]  
        
        # check each number
        for i in xrange(1,len(nums)-1):
            # validate local peak
            if nums[i-1] < nums[i] > nums[i+1]:
                # return peak location
                return i-1
            

nums = [1,3,2,1]
nums = [3,4,3,2,1]
nums = [2,1]
nums = [3,2,1]
test = Solution()
print test.findPeakElement(nums)