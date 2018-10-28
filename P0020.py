# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:52:25 2018

@author: Tianqi Guo
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l = len(s)
        # set of left parentheses
        left_p = "([{"        
        # stack that stores all unpaired parentheses       
        p = []
        # iterate over all parentheses in s
        for i in range(l):
            # the current parentheses
            c = s[i]
            # if the current parentheses is a left one
            if left_p.find(c) != -1:
                # place it in the stack
                p.append(c)
            # if the current parentheses is a right one
            else:                
                # if stack is empty
                if not p:
                    # pairing failed
                    return False
                # check if the top element in stack pairs with current parentheses
                # if pairing successful remove the top element
                # if pairing failed return invalid 
                if c == ')':
                    if p[-1] == '(':
                        p.pop(-1)
                    else:
                        return False
                if c == ']':
                    if p[-1] == '[':
                        p.pop(-1)
                    else:
                        return False
                if c == '}':
                    if p[-1] == '{':
                        p.pop(-1)
                    else:
                        return False
        # if stack empty after all parentheses in s are visited
        if not p:
            # all parentheses are paired, return valid 
            return True
        # if stack not empty
        else:
            # remaining parentheses in stack are not paired, return invalid
            return False
        
s = "]"
test = Solution()
print(test.isValid(s))
    
                