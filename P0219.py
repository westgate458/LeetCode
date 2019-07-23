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
        
        # dictionary to record last occurance position of each number
        d = {}
        # check each number
        for i in range(len(nums)):
            # if it has not appeared before, or last occurance is too far
            if (nums[i] not in d) or (i - d[nums[i]] > k):
                # update with the new position
                d[nums[i]] = i
            # if it has appeared, and last appearance is within k
            else:
                # there exist such nearby duplicate
                return True  
        
        # if after checking all numbers, no such duplicates exist
        # return not found
        return False
                
nums = [1,0,1,1]
k = 1
        
nums = [1,2,3,1]
k = 3

nums = [1,2,3,1,2,3]
k = 2    

test = Solution()
print(test.containsNearbyDuplicate(nums, k))
        