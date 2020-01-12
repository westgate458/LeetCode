# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:53:56 2020

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """        
        # dictionary for number of occurances
        d = defaultdict(int)
        # for each character check its occurances
        for c in s:
            d[c] += 1
        # res: length of the palindrome without the mid character
        # mid: if we have a spare one to fit in the middle
        res = mid = 0        
        # check all characters 
        for c in d:
            # place the largest even part of it into the palindrome, evenly on both ends
            res += d[c]//2 *2
            # if occurance is odd, we mark we have a spare one
            mid = mid or d[c]%2
        # finally we place one spare character in the middle if available
        return res+mid
            