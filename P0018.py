# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:49:27 2018

@author: Tianqi Guo
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(nums)
        nums.sort()
        ans = []
        num_1 = float('nan')
        for i in range(l-3):
            if num_1 == nums[i]:
                continue
            num_1 = nums[i]
            num_2 = float('nan')
            for ii in range(i+1,l-2):
                if num_2 == nums[ii]:
                    continue
                num_2 = nums[ii]
                j = ii + 1
                k = l - 1
                while j < k:
                    num_3 = nums[j]
                    num_4 = nums[k]                             
                    if num_1 + num_2 + num_3 + num_4 == target:                    
                        ans.append([num_1,num_2,num_3,num_4])  
                        while (j < k) and (nums[k] == num_4):
                            k = k - 1
                        while (j < k) and (nums[j] == num_3):
                            j = j + 1       
                    else:
                        if num_1 + num_2 + num_3 + num_4 > target:
                            k = k - 1
                        else:
                            j = j + 1               
                        
        return ans
    
nums = [1, 0, -1, 0, -2, 2]
target = 0
test = Solution()
print(test.fourSum(nums,target))   