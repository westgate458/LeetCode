# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:53:50 2019

@author: Tianqi Guo
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # run P0198 twice
        # one with first house robbed, one with last house robbed
        
        l = len(nums)
        
        if l == 1:
            return nums[0]
        
        max_pre1, max_cur1 = 0, 0      
        max_pre2, max_cur2 = 0, 0
        
        for i in xrange(l-1):
            max_pre1, max_cur1 = max_cur1, max(max_pre1 + nums[i], max_cur1) 
            max_pre2, max_cur2 = max_cur2, max(max_pre2 + nums[i+1], max_cur2) 
            
        return max(max_cur1, max_cur2)
