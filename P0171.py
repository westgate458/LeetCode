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
        # the column number          
        ans = 0
        # check each digit of the column title string
        for c in s:
            # each time multiply results of preceeding digits by 26
            # then add result of current digit to the column number
            ans = ans * 26 + ord(c) - 64
        # return the final column number
        return ans    

s = 'ZY'
test = Solution()
print test.titleToNumber(s)
        