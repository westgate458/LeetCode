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
        
        # sort the numbers to avoid duplicates
        nums.sort()
        
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
                    # check if the current number is different than the previous number
                    # this avoids duplicates
                    if (i == 0) or (nums[i] != nums[i-1]):
                        # next dfs with updated remaining numbers and permutation 
                        dfs(nums[:i]+nums[i+1:],permutation+[nums[i]])
                    
        # answer list stores all permutations           
        ans = []
        # start DFS with all available numbers and empty permutation
        dfs(nums,[])  
        
        # return answer list
        return(ans)

nums = [3,3,0,3]
test = Solution()
print(test.permuteUnique(nums))
