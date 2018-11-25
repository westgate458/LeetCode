# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:52:15 2018

@author: Tianqi Guo
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        l = len(s)
        # set of left parentheses        
        p = []
        # iterate over all parentheses in s
        b = [-1]
        for i in range(l):
            # the current parentheses
            c = s[i]
            # if the current parentheses is a left one
            if c == '(':
                # place it in the stack
                p.append(c)
                b.append(i)
            # if the current parentheses is a right one
            else:                
                # if stack is empty
                if not p:
                    # pairing failed
                    b.append(i)
                else:             
                    if p[-1] == '(':
                        p.pop(-1)         
                        b.pop(-1)
           
        ans = (l - 1) - b[-1]
        for i in range(1,len(b)):
            if b[i] - b[i-1] - 1 > ans:
                ans = b[i] - b[i-1] - 1
        
        return ans
          
        
s = ")()())"
test = Solution()
print(test.longestValidParentheses(s))
    
                