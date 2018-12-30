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
        
        # sub DFS function for n numeration 
        def dfs(nums,permutation):          
            # if no number is left, has reached n-th numeration 
            if len(nums) == 0:
                # record the current permutation
                ans.append(permutation)
            # if still numbers remain, perform numeration for current position
            else:
                # add each remaining number to permutation
                for i in range(len(nums)):     
                    # next dfs with updated remaining numbers and permutation
                    dfs(nums[:i]+nums[i+1:],permutation+[nums[i]])
        
        # answer list stores all permutations           
        ans = []
        # start DFS with all available numbers and empty permutation
        dfs(nums,[])  
        
        # return answer list
        return(ans)

nums = [1,2,3]
test = Solution()
print(test.permute(nums))
 
    