# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:27:35 2019

@author: Tianqi Guo
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # length of the reduced array
        l = 0
        
        # for each number in the original array
        for num in nums:
            # if the current reduced array has fewer than 2 numbers
            # or the 2nd last number in the reduced array is not the current number
            if l < 2 or nums[l-2] < num:
                # the current number has not appeared more than twice
                # place current number at the end of the reduce array
                nums[l] = num
                # and update the length of the reduced array
                l += 1
        
        # return the length of the reduced array
        return l
        
nums = [1,1,1,2,2,3]
test = Solution()
print test.removeDuplicates(nums)