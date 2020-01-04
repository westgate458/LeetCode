# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:33:59 2020

@author: Tianqi Guo
"""

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """       
        # Solution 1 beats 99.74%: check edge test cases + DFS
        for i in range(3, len(stones)):            
            if stones[i] > (stones[i-1]*2):
                return False  
        status = [(0,0)]    
        stones_set = set(stones)
        while status:            
            stone, jump = status.pop()                       
            for next_jump in [jump-1,jump,jump+1]:
                if next_jump <= 0:
                    continue
                next_stone = next_jump + stone
                if next_stone == stones[-1]:
                    return True
                if next_stone in stones_set:
                    status.append((next_stone,next_jump))
        return False
    
        # Solution 2 beats 11.49%: DP
        from collections import defaultdict
        d = defaultdict(set)
        d[0] = set([0])     
        l = len(stones)
        for i in xrange(l):            
            if i in d:
                for j in xrange(i+1,l):                    
                    jump = stones[j] - stones[i]
                    if jump in d[i] or jump+1 in d[i] or jump-1 in d[i]:
                        d[j].add(jump)                         
        return l-1 in d