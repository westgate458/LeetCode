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
        
        # steps
        # 1) reverse the string
        # 2) get rid of preceeding whitespaces
        # 3) put a whitespace at the end in case of a single word
        # 4) find the position of the first whitespace
        # 5) this position indicates the length of the last word
        
        return ''.join([s[::-1].lstrip(),' ']).find(' ')
    

s = "Hello World"
test = Solution()
print(test.lengthOfLastWord(s))