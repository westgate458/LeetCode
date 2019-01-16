# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:07:08 2019

@author: Tianqi Guo
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        return ''.join([s[::-1].lstrip(),' ']).find(' ')
    

s = "Hello World"
test = Solution()
print(test.lengthOfLastWord(s))