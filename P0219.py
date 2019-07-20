# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:31:41 2019

@author: Tianqi Guo
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        d = {}
        
        for i in range(len(nums)):
            
            if (nums[i] not in d) or (i - d[nums[i]] > k):
                d[nums[i]] = i
            else:
                return True  
            
        return False
                
nums = [1,0,1,1]
k = 1
        
nums = [1,2,3,1]
k = 3

nums = [1,2,3,1,2,3]
k = 2    

test = Solution()
print(test.containsNearbyDuplicate(nums, k))
        