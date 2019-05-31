# -*- coding: utf-8 -*-
"""
Created on Sun May 19 14:55:17 2019

@author: Tianqi Guo
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """        
        
        # Solution 1: using split function
        return ' '.join(s.split()[::-1])
        
#        # Solution 2: straight-up string operation
#        ans = ''
#        word = ''
#        for ch in s[::-1] + ' ':
#            if ch != ' ':
#                word += ch 
#            elif word != '':
#                ans += word[::-1] + ' '
#                word = ''                
#        return ans[:-1]

s = "  hello world!  "
s = "a good   example"
s = "the sky is blue"

test = Solution()
print test.reverseWords(s)