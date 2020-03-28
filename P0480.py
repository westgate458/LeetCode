# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:31:01 2020

@author: Tianqi Guo
"""

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        res, win, i, odd = [], sorted(nums[:k]), k//2, (k % 2 != 0)          
        res.append(win[i] if odd else (win[i]+win[i-1])/2.)        
        for p in xrange(k,len(nums)):
            if nums[p-k] != nums[p]:
                win.pop(bisect.bisect_left(win, nums[p-k]))
                bisect.insort_left(win, nums[p]) 
            res.append(win[i] if odd else (win[i]+win[i-1])/2.)                     
        return res
                
            