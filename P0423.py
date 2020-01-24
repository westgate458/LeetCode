# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:46:50 2020

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """        
        d = defaultdict(int)
        for c in s:
            d[c] += 1            
        n, chrs, nums = [0]*10, 'zwuxghfvin', ['zero','two','four','six','eight','three','five','seven','nine','one']      
        for i, num in enumerate([0,2,4,6,8,3,5,7,9,1]):
            n[num] = d[chrs[i]]
            for c in nums[i]:
                d[c] -= n[num] 
        return(''.join([a*b for a,b in zip('0123456789',n)]))
        