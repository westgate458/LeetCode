# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:54:09 2019

@author: Tianqi Guo
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """               
        ans = 0
        for c in s:
            ans = ans * 26 + ord(c) - 64
        return ans    

s = 'ZY'
test = Solution()
print test.titleToNumber(s)
        