# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:17:02 2020

@author: Tianqi Guo
"""

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1 beats 99.37%: two-stage visited marks
        l = len(nums)
        seen = [0] * l
        for p in xrange(l): 
            if seen[p] > 0: continue
            visited, d = [], nums[p]>0            
            while (nums[p]>0) == d:                
                if seen[p] == 1: return True
                else:
                    visited.append(p)
                    seen[p], pp = 1, (p + nums[p])%l                    
                    if pp == p or seen[pp] == 2: break
                    p = pp
            for pp in visited: seen[pp] = 2
        return False
    
        # Solution 2 beats 42.77%: terminate loop based on counts
        l = len(nums)
        for p0 in xrange(l):
            p, ll, d = (p0 + nums[p0] + l)%l, 1, nums[p0]>0       
            while (p != p0) and (ll <= l) and ((nums[p]>0) == d):
                ll += 1             
                p = (p + nums[p] + l)%l
            if (p == p0) and ll>1:                
                return True            
        return False