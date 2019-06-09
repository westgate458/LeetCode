# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:31:28 2019

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Solution 1: Cheat by sorting
        return sorted(nums)[len(nums)//2]
    
        # Solution 2: Using hash table
        # dictionary storing the number of occurances for each number
        d = defaultdict(int)
        # required occurances for the majority element
        l = len(nums)//2
        # check each number
        for num in nums:
            # increase its occurance
            d[num] += 1
            # check if it has occurred enough times
            if d[num] > l:
                # return the majority element
                return num

nums = [2,2,1,1,1,2,2]    
nums = [3,2,3]        
test = Solution()
print test.majorityElement(nums)
            
        