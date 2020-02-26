# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:34:00 2020

@author: Tianqi Guo
"""

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1 beats 82.05%: stack with reversed sequence
        two, s = float('-inf'), []        
        for num in nums[::-1]:
            if num < two: return True
            while s and s[-1] < num: two = s.pop()
            s.append(num)
        return False
    
        # Solution 2 beats 57.27%: stack with pre-calculated mins
        if not nums: return False
        mins = [nums[0]]
        for num in nums[1:]:
            mins.append(min(mins[-1],num))
        s = []
        for i in xrange(len(nums)-1,-1,-1):
            while s and s[-1] < nums[i]:
                if mins[i] < s[-1]: return True
                s.pop()
            s.append(nums[i])
        return False
        
        # Solution 3 beats 5.41%: brute force
        l, m = len(nums), float('inf')        
        for i in xrange(l):
            if nums[i] > m:
                for num in nums[i+1:]:
                    if m < num < nums[i]: return True
            elif nums[i] < m: m = nums[i]
        return False