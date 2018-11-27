# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:14:37 2018

@author: Tianqi Guo
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        
        if l == 0:
            return -1
        else:
            if (l == 1):
                if (nums[0] == target):
                    return 0
                else:
                    return -1
        
        h = 0
        t = l - 1        
        
        while h < t:
            
            m = (h + t)/2        
            
            if nums[m] > nums[m+1]:
                break    
            
            if nums[m] > nums[t]:
                h = m
                continue
            
            if nums[m] < nums[h]:
                t = m
                continue
            
            m = h - 1
            break
        
        inds = range(l)
        nums = list(nums[m+1:]+nums[:m+1])
        inds = list(inds[m+1:]+inds[:m+1])
        
        h = 0
        t = l - 1 
        
        while h <= t:
            
            m = (h + t)/2        
            
            if nums[m] == target:
                return inds[m]
                break    
            
            if nums[m] > target:
                t = m - 1
                continue
            
            if nums[m] < target:
                h = m + 1
                continue
        
        return -1
        
        
nums = [5,1,3]
target = 5

test = Solution()
print(test.search(nums,target))

  
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    