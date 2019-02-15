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
               
        def dfs(nums,k,combination):
            if k == 0: 
                ans.append(combination)            
            else:                
                for i in range(len(nums)-k+1):                    
                    dfs(nums[i+1:],k-1,combination+[nums[i]])        
            
        ans = []
        nums = range(1,n + 1)       
        dfs(nums,k,[])  
        
        return(ans)       

n = 4
k = 2

test = Solution()
print(test.combine(n, k))
 
    