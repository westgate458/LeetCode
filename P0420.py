# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:26:18 2020

@author: Tianqi Guo
"""

class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)        
        has_upper = has_lower = has_digit = 0            
        repeats, repeat, pre = [], 0, ''     
        for c in s+'.':
            if c == pre:
                repeat += 1
            else:
                if repeat > 2:
                    repeats.append(repeat)
                pre, repeat = c, 1                   
            if c.isupper():
                has_upper = 1
            elif c.islower():
                has_lower = 1
            elif c.isdigit():
                has_digit = 1                
        has_types = has_upper + has_lower + has_digit     
        heap = [(repeat%3,repeat) for repeat in repeats]     
        delete_count = 0        
        if l < 6:               
            if repeats and repeats[-1] == 5:
                return 2
            else:
                return max(6-l, 3-has_types)
        elif l > 20:            
            heapq.heapify(heap)   
            delete_count = l-20
            while heap and l > 20:
                m, r = heapq.heappop(heap)
                l_change = min(m+1, l-20)
                l -= l_change                
                heapq.heappush(heap, (2, r-l_change))   
        change_count = max(sum([r//3 for _, r in heap]), 3-has_types)        
        return change_count + delete_count
                
            