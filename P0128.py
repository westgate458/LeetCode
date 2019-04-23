# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:09:33 2019

@author: Tianqi Guo
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # convert list of nums to set
        nums_set = set(nums)         
        # answer length
        ans = 0
        
        # check each word in the set
        for num in nums:
            # if it is the smallest in the consecutive sequence it belongs to
            if num - 1 not in nums_set:     
                # next number in the consecutive sequence
                next_num = num + 1
                # if next number exists in the set
                while next_num in nums_set:
                    # check next one
                    next_num += 1
                # update the length of the longest consecutive sequence
                ans = max(ans, next_num - num)
        
        # return the length
        return ans
        
        
nums = [-3,-1,-2]
test = Solution()
print test.longestConsecutive(nums)
