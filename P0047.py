# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:16:30 2018

@author: Tianqi Guo
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def dfs(nums,permutation):            
            if (len(nums) == 0):
                ans.append(permutation)
            else:
                for i in range(len(nums)): 
                    if (i == 0) or (nums[i] != nums[i-1]):
                        dfs(nums[:i]+nums[i+1:],permutation+[nums[i]])
                    
        ans = []
        dfs(nums,[])  
        
        return(ans)

nums = [3,3,0,3]
test = Solution()
print(test.permuteUnique(nums))
