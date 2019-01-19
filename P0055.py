# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:12:37 2019

@author: Tianqi Guo
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # number of elements
        l = len(nums)
        # max achievable position before jump
        max_i = 0
        
        # traverse all elements from left to right
        for i in range(l-1):
            
            # if current element is beyond max achievable position
            # from previous positions
            if max_i < i:
                # terminate searching since it could never make it here
                break
            # if we can jump further than the previous max achievable position
            # from the current position
            if i + nums[i] > max_i:
                # update the max achievable position
                max_i = i + nums[i]
        
        # if after traversing the max achievable position is beyond the last element
        if max_i >= l-1:
            # we can reach the last index
            return True
        # if the max achievable position is short
        else:
            # we can never reach the last index
            return False
        
nums = [3,2,1,0,4]
test = Solution()
print(test.canJump(nums))