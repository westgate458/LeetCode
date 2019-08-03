# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:59:13 2019

@author: Tianqi Guo
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # deal with trivial case
        if not nums:
            return []
        # result list for all ranges
        res = []
        # start from first number
        start = nums[0]
        # pointer for current number
        p = 1
        # put an inf at the end so the loop deals with all numbers
        nums += [float('inf')]
        # check each number
        while p < len(nums):            
            # if there is a gap between current number and previous number
            if nums[p-1] + 1 != nums[p]:
                # a new range is found, place the start in res first
                res.append(str(start))
                # if the end is not the same as the start
                if nums[p-1] != start:
                    # place the end in the res as well
                    res[-1] += '->'+str(nums[p-1])
                # current number is then the new start
                start = nums[p]            
            # move on to next number
            p += 1                
        # return all ranges
        return res