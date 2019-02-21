# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:26:34 2019

@author: Tianqi Guo
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        h = 0
        t = len(nums) - 1
        
        while h <= t:
            
            m = (h + t)/2
            
            if nums[m] == target:
                return True
            
            while (h < m) and (nums[h] == nums[m]):
                h = h + 1
            while (m < t) and (nums[t] == nums[m]):
                t = t - 1
                
            if nums[h] <= nums[m]:
                if nums[h] <= target < nums[m]:
                    t = m - 1
                else:
                    h = m + 1
            else:
                if nums[m] < target <= nums[t]:
                    h = m + 1
                else:
                    t = m - 1
        
        return False
                
        
        
nums = [1,1,2,1]
target = 2

test = Solution()
print(test.search(nums,target))