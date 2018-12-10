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
        
        # length of string
        l = len(s)
        # stack that stores the left paretheses
        p = []
        # list that stores breakpoints where pairing fails 
        # and from where next string starts
        # initialize with -1 to deal with the scenario where entire string is valid
        b = [-1]
        
        # iterate over all parentheses in s
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
                    # pairing failed, record this position
                    b.append(i)
                else:             
                    # stack is not empty, there is left parenthese to match
                    # pop the last parenthese because its matched
                    p.pop(-1)         
                    b.pop(-1)
        
        # initialize answer as the length from last breakpoint to the end of s
        ans = (l - 1) - b[-1]
        # check all breakpoints and see if there is a longer valid string
        for i in range(1,len(b)):
            # the length of each valid string
            # is the distance between adjacent breakpoints
            if b[i] - b[i-1] - 1 > ans:
                # update answer if a longer one is found
                ans = b[i] - b[i-1] - 1
        
        return ans
          
        
s = ")()())"
test = Solution()
print(test.longestValidParentheses(s))
    
                