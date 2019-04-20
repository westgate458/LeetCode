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
        
        nums_set = set(nums)            
        ans = 0
        
        for num in nums:
            if num - 1 not in nums_set:               
                next_num = num + 1
                while next_num in nums_set:
                    next_num += 1
                ans = max(ans, next_num - num)
            
        return ans
        
        
nums = [-3,-1,-2]
test = Solution()
print test.longestConsecutive(nums)
