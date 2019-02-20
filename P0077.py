# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:00:37 2019

@author: Tianqi Guo
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        # dfs subfunction for combination
        def dfs(nums,k,combination):
            # nums: remaining available number list
            # k: how many more numbers are required
            # combination: current combination
            
            # if no more nums are needed
            if k == 0: 
                # append current combination to answer list
                ans.append(combination)            
            # if need to add more nums to combination
            else:                
                # for each number in the nums list
                # note: the last number to try should ensure
                #       there are at least (k-1) numbers after it
                for i in range(len(nums)-k+1):    
                    # continue dfs with updated 
                    # number list, required numbers, and combination
                    dfs(nums[i+1:],k-1,combination+[nums[i]])        
        
        # answer list of all combinations
        ans = []
        # available number list
        nums = range(1,n + 1)  
        # start dfs with all available numbers and empty combination
        dfs(nums,k,[])  
        
        # return answer list
        return(ans)       

n = 4
k = 2

test = Solution()
print(test.combine(n, k))
 
    