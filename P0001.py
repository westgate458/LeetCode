# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 19:30:20 2018

@author: Tianqi Guo
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """    
        
        N_num = len(nums)        
        # brute force search
        for i in range(N_num-1):
            for j in range(i+1,N_num):
                # return indices when two number sums equal target
                if nums[i] + nums[j] == target:
                    return([i,j])
                    
test = Solution()
print(test.twoSum([2, 7, 11, 15],9))