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
        # Solution 1 beats 98.13%: using dictionary
        d = {}
        for i,num in enumerate(nums):
            if target-num in d:
                return([d[target-num],i])
            else:
                d[num] = i
        
        # Solution 2 beats 27.00%: brute force search
        N_num = len(nums)        
        # brute force search
        for i in range(N_num-1):
            for j in range(i+1,N_num):
                # return indices when two number sums equal target
                if nums[i] + nums[j] == target:
                    return([i,j])
                    
test = Solution()
print(test.twoSum([2, 7, 11, 15],9))