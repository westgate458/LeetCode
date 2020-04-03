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
        # res: medians of each window
        # win: current window, maintained in sorted order
        # i: indice of the mid in the window
        # odd: if the window length is odd
        res, win, i, odd = [], sorted(nums[:k]), k//2, (k % 2 != 0)          
        # deal with first window
        res.append(win[i] if odd else (win[i]+win[i-1])/2.)        
        # shift the window towards right
        for p in xrange(k,len(nums)):
            # if new number is different from the one to remove
            if nums[p-k] != nums[p]:
                # find where nums[p-k] is in the sorted window, and remove it
                win.pop(bisect.bisect_left(win, nums[p-k]))
                # insert the new number into the window
                bisect.insort_left(win, nums[p]) 
            # find the median and record it
            res.append(win[i] if odd else (win[i]+win[i-1])/2.)                     
        # return all medians
        return res
                
            