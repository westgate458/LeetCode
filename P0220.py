# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:54:38 2019

@author: Tianqi Guo
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        # Solution 1: cheat
        if k == 0:
            return False
        
        l = len(nums)
        
        nums_sorted = sorted(nums)
        flag = False
        for i in range(1,l):
            if nums_sorted[i] - nums_sorted[i-1] <= t:
                flag = True
                break
        if not flag:
            return False
        
        for i in range(l):
            for j in range(i+1, min(i+1+k, l)):
                if abs(nums[j] - nums[i]) <= t:
                    return True
                
        return False
    
        
        # Solution 2: binary search\insertion
        
        if k == 0:
            return False
        
        l = len(nums)        
        k = min(k, l-1)
         
        temp = sorted(zip(nums[:k+1], range(k+1)))
        for j in range(1,k+1):
            if temp[j][0] - temp[j-1][0] <= t:
                return True       
       
        i = k + 1
        
        while i < l:   
            
            h, p = 0, k            
            while h <= p: 
                m = (h + p)/2
                if temp[m][0] == nums[i-k-1]:
                    break                
                elif temp[m][0] > nums[i-k-1]:
                    p = m - 1
                else:
                    h = m + 1
            
            j = m                
            while temp[j][0] == nums[i-k-1] and temp[j][1] != i-k-1:
                j -= 1                
            if temp[j][0] != nums[i-k-1]:            
                j = m
                while temp[j][0] == nums[i-k-1] and temp[j][1] != i-k-1:
                    j += 1
            temp.pop(j) 
            
            h, p = 0, k - 1            
            while h <= p: 
                m = (h + p)/2             
                if abs(temp[m][0] - nums[i]) <= t:
                    return True                
                elif temp[m][0] > nums[i]:
                    p = m - 1
                else:
                    h = m + 1
            
            if temp[m][0] > nums[i]:
                temp.insert(m, (nums[i], i))
            else:
                temp.insert(m+1, (nums[i], i))            
            
            i += 1
            
        return False

nums = [1,2,3,1]
k = 3
t = 0

nums = [1,0,1,1]
k = 1
t = 2


nums = [1,2]
k = 0
t = 1

nums = [3,6,0,4]
k = 2
t = 2


nums = [1,5,9,1,5,9]
k = 2
t = 3

nums = [0,10,22,15,0,5,22,12,1,5]
k = 3
t = 3

test = Solution()
print test.containsNearbyAlmostDuplicate(nums, k, t)