# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:35:22 2018

@author: Tianqi Guo
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = len(nums)
        nums.sort()        
        num_1 = float('nan')
        closestSum = float('Inf')
        for i in range(l-2):
            if num_1 == nums[i]:
                continue
            num_1 = nums[i]
            j = i + 1
            k = l - 1
            while j < k:
                num_2 = nums[j]
                num_3 = nums[k]          
                threeSum =  num_1 + num_2 + num_3    
                if abs(threeSum - target) < abs(closestSum - target):
                    closestSum = threeSum
                if threeSum == target:                    
                    return target
                else:
                    if num_1 + num_2 + num_3 > target:
                        k = k - 1
                    else:
                        j = j + 1               
                    
        return closestSum
nums = [-1, 2, 1, -4]
target = 1
test = Solution()
print(test.threeSumClosest(nums,target)) 