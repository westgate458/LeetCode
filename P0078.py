# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:56:24 2019

@author: Tianqi Guo
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,sets):            
            ans.append(sets)            
            if nums:
                for i in range(len(nums)):                    
                    dfs(nums[i+1:],sets+[nums[i]])        
            
        ans = []               
        dfs(nums,[])  
        
        return ans       
    
nums = [1,2,3]
test = Solution()
print test.subsets(nums)