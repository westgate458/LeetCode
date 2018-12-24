# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:58:49 2018

@author: Tianqi Guo
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def dfs(nums,permutation):            
            if len(nums) == 0:
                ans.append(permutation)
            else:
                for i in range(len(nums)):            
                    dfs(nums[:i]+nums[i+1:],permutation+[nums[i]])
                    
        ans = []
        dfs(nums,[])  
        
        return(ans)

nums = [1,2,3]
test = Solution()
print(test.permute(nums))
 
    