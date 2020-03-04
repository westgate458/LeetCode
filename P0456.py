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
        # two: current fount 2 in the 132 pattern
        # s: monotonically increasing stack, all numbers larger than current two, with current three as top
        two, s = float('-inf'), []        
        # check each number from back to front
        for num in nums[::-1]:
            # if current number is smaller than two, then we found the one
            # since we have threes in the stack, a 132 pattern is found            
            if num < two: return True
            # if the stack top (current 3) is smaller than current number
            # then we better use the stack top as the new 2, and current number as 3
            # since as long as we have 3 and 2 found, we want them as larget as possible
            # so we can find 1 easilier for the 132 pattern
            while s and s[-1] < num: two = s.pop()
            # now the stack top is larger than current number
            # so push current number to stack, and it is the new three
            s.append(num)
        # after all numbers are checked, no 132 pattern was found
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