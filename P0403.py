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
        # first deal with edge test cases
        # see if there is gap too large to jump across
        for i in range(3, len(stones)):            
            # if current stone is twice the previous one
            # we can make to the next one only if previous jump is from 0 to stones[i-1] itself
            # but the first jump is 1
            if stones[i] > (stones[i-1]*2):
                return False  
        # start from first stone
        status = [(0,0)]    
        # all stones in a set for fast check
        stones_set = set(stones)
        # loop for DFS
        while status:            
            # previous stone and jump
            stone, jump = status.pop()
            # try next jump
            for next_jump in [jump-1,jump,jump+1]:
                # since we can't jump back, only proceed if next jump is positive
                if next_jump <= 0:
                    continue
                # position of the next stone
                next_stone = next_jump + stone
                # check if we have reached the destination
                if next_stone == stones[-1]:
                    return True                
                # if next position is a stone
                if next_stone in stones_set:
                    # push current status to the stack
                    status.append((next_stone,next_jump))
        # if all possible jumps are tried but we never reached the destination
        # then we can not make it
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