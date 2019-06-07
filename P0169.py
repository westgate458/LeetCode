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
        
        # Solution 1: Cheating
        return sorted(nums)[len(nums)//2]
    
        # Solution 2: Using hash table
        d = defaultdict(int)
        l = len(nums)//2
        for num in nums:
            d[num] += 1
            if d[num] > l:
                return num

nums = [2,2,1,1,1,2,2]    
nums = [3,2,3]        
test = Solution()
print test.majorityElement(nums)
            
        