# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:05:24 2019

@author: Tianqi Guo
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # dfs subfunction to form the subsets
        def dfs(nums,sets):            
            # nums: remaining available numbers
            # sets: current set
            
            # append current set to the answer list
            ans.append(sets)            
            # if still numbers left
            if nums:
                # for each number available
                for i in range(len(nums)): 
                    # continue dfs with
                    # reduced number list, and augmented set
                    if i == 0 or nums[i] > nums[i-1]:
                        dfs(nums[i+1:],sets+[nums[i]])        
        
        # answer list for all subsets
        ans = []               
        # start dfs with all available numbers and an empty set
        dfs(sorted(nums),[])  
        
        # return the answer list
        return ans       
    
nums = [4,1,0]
test = Solution()
print test.subsetsWithDup(nums)