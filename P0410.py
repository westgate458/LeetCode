# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:38:24 2020

@author: Tianqi Guo
"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """          
        # Solution 1 beats 95.52%: binary search
        l, r = max(nums), sum(nums)        
        while l < r:
            mid = (l+r)//2            
            group_num, group_sum = 1, 0                        
            for num in nums:
                group_sum += num
                if group_sum > mid:
                    group_sum = num
                    group_num += 1            
            if group_num > m:
                l = mid + 1                
            else:
                r = mid
        return l
    
        # Solution 2 beats 37.65%: DFS + memorization
        l = len(nums)      
        d = [[0]*(m+1) for _ in xrange(l)]        
        sums = [0]*(l+1) 
        for i in xrange(l):
            sums[i+1] = sums[i] + nums[i]        
        def DFS(i, m):            
            if m == 1:                
                d[i][m] = sums[-1]-sums[i]                         
            elif d[i][m] == 0:
                d[i][m] = float('inf')    
                for k in xrange(i,l-m+1):    
                    left = sums[k+1]-sums[i]
                    if left < d[i][m]:
                        right = DFS(k+1,m-1)
                        d[i][m] = min(d[i][m], max(left, right))      
                    else:
                        break   
            return d[i][m]
        return(DFS(0,m))    