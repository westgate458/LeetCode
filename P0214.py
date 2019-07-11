# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:55:07 2019

@author: Tianqi Guo
"""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = float('inf')
        for i in range(len(s)/2): 
            l = 1
            while l <= i:           
                print s[i-l], s[i], s[i+l]
                l += 1
            


s = "aacecaaa"            
test = Solution()
test.shortestPalindrome(s)