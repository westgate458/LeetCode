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
        # number of numbers
        l = len(nums)
        # visited marks: 0 - unvisited, 1 - visited in current search, 2 - checked in previous search
        seen = [0] * l
        # try to start seaching at each position
        for p in xrange(l): 
            # if we have already visited current number, it means it didn't leed to a loop
            # we do not need to start searching from here again
            if seen[p] > 0: continue
            # visited: all positions we visited during current search
            # d: if current loop is positive direction
            visited, d = [], nums[p]>0            
            # continue searching if current number has the same sign (direction)
            while (nums[p]>0) == d:                
                # if we have visited this number in current search, we have found a loop
                if seen[p] == 1: return True
                # if we have not visited this number
                else:
                    # record it to later mark it as 2
                    visited.append(p)
                    # mark we have visited this one
                    # and check next position
                    seen[p], pp = 1, (p + nums[p])%l                    
                    # we terminate searching under two circumstances:
                    # 1) pp == p: we have a 1-length loop, not desired
                    # 2) seen[pp] == 2: we have checked next position in previous searches
                    # both won't lead to a desired loop
                    if pp == p or seen[pp] == 2: break
                    # move on to next position
                    p = pp
            # we mark all positions visited in current search as 2
            for pp in visited: seen[pp] = 2
        # after all positions considered, no loop was found
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