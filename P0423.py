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
        # occurances of each character
        d = defaultdict(int)
        # count the occurances
        for c in s:
            d[c] += 1         
        # we decide the occurances of each number in this order [0,2,4,6,8,3,5,7,9,1]
        # by the remaining of characters 'zwuxghfvin'        
        n, chrs, nums = [0]*10, 'zwuxghfvin', ['zero','two','four','six','eight','three','five','seven','nine','one']      
        # determine the numbers one by one
        for i, num in enumerate([0,2,4,6,8,3,5,7,9,1]):
            # the occurances of num is determined from the remaining occurances of character chrs[i]
            n[num] = d[chrs[i]]
            # update the remaining occurances of each character after all nums removed
            for c in nums[i]:
                d[c] -= n[num] 
        # construct the answer string
        return(''.join([a*b for a,b in zip('0123456789',n)]))
        