# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:21:23 2019

@author: Tianqi Guo
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Solution 1        
        ans = 0
        for num in nums:
            ans ^= num            
        return ans
        
        # Solution 2
        num_set = set()
        
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)
                
        return num_set.pop()
    
nums = [4,1,2,1,2]
test = Solution()
print test.singleNumber(nums)