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
        
        # Solution 1: cheat by pre-checking gaps beats 73.97%
        
        # deal with trivial case
        if k == 0:
            return False
        
        # number of elements
        l = len(nums)
        
        # numbers in sorted order
        nums_sorted = sorted(nums)
        # flag if there exists a gap smaller than t between consecutive numbers
        flag = False
        # check each number and its previous one
        for i in range(1,l):
            # see if the gap is smaller than t
            if nums_sorted[i] - nums_sorted[i-1] <= t:
                # if there exists such numbers, solution is possible
                flag = True
                # no need to check further
                break
        # if there are no such numbers that satisfy their absolute difference smaller than t
        if not flag:
            # no solution possible, return false
            return False
        
        # check each number in original order
        for i in range(l):
            # see the difference with its nearby numbers
            for j in range(i+1, min(i+1+k, l)):
                # see if their difference is within t
                if abs(nums[j] - nums[i]) <= t:
                    # a desired number pair has been found
                    return True
        # if after all numbers are checked, no such pair exists
        # return not found                
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