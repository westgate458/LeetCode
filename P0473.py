# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 22:37:17 2020

@author: Tianqi Guo
"""

class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """     
        # Solution 1 beats 99.07%: enforce the usage of each number one by one
        s, l = sum(nums), len(nums)
        t = s//4
        if (not nums) or (s%4 != 0) or max(nums) > t:
            return False
        
        nums.sort(reverse=True)        
        used = [False] * l
        
        def DFS(i, target):            
            if target == 0: return True
            for j, num in enumerate(nums[i+1:], i+1):                
                if used[j]: continue
                if num <= target:
                    used[j] = True
                    if DFS(j, target-num): return True
                    used[j] = False
            return False
          
        for i, num in enumerate(nums):            
            if used[i]: continue
            used[i] = True            
            if not DFS(i, t-num): return False
        return True
        
        # Solution 2 beats 7.48%: brute force
        if sum(nums) %4 != 0: return False
        l = sum(nums)//4
        nums.sort(reverse=True)        
        def DFS(p,s1,s2,s3,s4):            
            if p == len(nums): return s1 == s2 == s3 == s4 != 0
            elif s1 > l or s2 > l or s3 > l or s4 > l: return False
            else: return DFS(p+1,s1+nums[p],s2,s3,s4) or DFS(p+1,s1,s2+nums[p],s3,s4) or DFS(p+1,s1,s2,s3+nums[p],s4) or DFS(p+1,s1,s2,s3,s4+nums[p])
        return DFS(0,0,0,0,0)