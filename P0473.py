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
        # total sum of nums, and number of nums
        s, l = sum(nums), len(nums)
        # target side length
        t = s//4
        # wont make a square if nums is empty, 
        # or target length is not integer, 
        # or some number is larger than the side length
        if (not nums) or (s%4 != 0) or max(nums) > t:
            return False
        
        # sort nums for faster searching
        nums.sort(reverse=True)        
        # mark if each number is used
        used = [False] * l
        
        # DFS for assign each number to the four sides
        def DFS(i, target):            
            # if the side length is met
            # current combinations of numbers can make a side
            if target == 0: return True
            # try each number
            for j, num in enumerate(nums[i+1:], i+1):                
                # we only deal with unused numbers now
                if used[j]: continue
                # current number can be used in current side if it is smaller than remaining target
                if num <= target:
                    # mark it used temporarily
                    used[j] = True
                    # move on to find next number
                    # if subfunction returns True, it means a combination for the target length is found
                    if DFS(j, target-num): return True
                    # if target can not be met, current number can not be used in current side
                    used[j] = False
            # if after all numbers are tried, target length is not met
            # if means we need to change previous picked numbers
            return False
        # check each number          
        for i, num in enumerate(nums):            
            # only assign used numbers to sides
            if used[i]: continue
            # mark it used temporarily
            used[i] = True        
            # if no combinations can make the side length with current number being used
            # we can not make the square
            if not DFS(i, t-num): return False
        # all numbers are assigned to a side, we have made the square!
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