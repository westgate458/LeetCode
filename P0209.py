# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:01:57 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """        
        # l: minimal length of a contiguous subarray
        # h: position of the first number for the minimal subarray found
        # s_now: the contiguous sum for the minimal subarray
        l, h, s_now = float('inf'), 0, 0    
        # try to use each number in the array as the last element in the minimal subarray
        for t in xrange(len(nums)):
            # update sum
            s_now += nums[t]
            # if current sum is larger than the required sum
            while s_now >= s:
                # update the length
                l = min(l, t - h + 1)
                # try to include one fewer element from the head
                s_now -= nums[h]
                # update head pointer
                h += 1
                # then go on to check if current sum is still larger
        # if the length is still the initialzed inf
        # the s_now was never larger than s, so no such subarray was found
        # otherwise return the minimal length found
        return 0 if l == float('inf') else l 

s = 7
nums = [2,3,1,2,4,3]
test = Solution()
print test.minSubArrayLen(s, nums)
            