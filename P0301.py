# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:22:59 2019

@author: Tianqi Guo
"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # answer list that contains all valid results
        ans = set([])
        # subfunction for checking string character by character
        def DFS(p, combo, c, l, r):
            # p: current position in the string
            # combo: combination of valid parentheses so far
            # c: stack for checking pairing
            # l: number of mismatching '(' left to remove
            # r: number of mismatching ')' left to remove
            
            # if we have reached the end of the string
            if p == len(s):               
                # if stack is empty, i.e. all parentheses are paired
                if c == '':
                    # current combo is valied
                    ans.add(combo)
            # if current parentheses is a '('
            elif s[p] == '(':
                # we have two options
                # 1) keep this '(', update state and continue DFS
                DFS(p+1, combo + '(', c + '(', l, r)
                # 2) if we can still remove '('
                if l > 0:
                    # remove this '(' and continue DFS
                    DFS(p+1, combo, c, l-1, r)
            # if current parentheses is a ')'
            elif s[p] == ')':
                # again we have two options
                # 1) if we have unpaired '(' in stack
                if c and c[-1] == '(':
                    # keep this ')', pair those two and continue DFS
                    DFS(p+1, combo + ')',c[:-1], l, r)                
                # 2) if we can still remove ')'
                if r > 0:
                    # remove this '）' and continue DFS
                    DFS(p+1, combo, c, l, r-1)
            # if current character is not a parentheses
            else:
                # simply add it to combo and continue DFS
                DFS(p+1, combo + s[p], c, l, r)
        
        # pre-processing to identify number of parentheses to remove
        l, r = 0, 0      
        # check each character in string
        for char in s:
            # if we meet a '('
            if char == '(' :
                # update counter
                l += 1
            # if we meet a ')'
            elif char == ')':
                # two scenarios
                # 1) if we have unpaired '(' before current position
                if l > 0:
                    # we can keep one of previous '(' to pair current ')'
                    l -= 1                    
                # 2) if all previous '(' have been paired 
                else:
                    # this ')' need to be removed
                    r += 1
        # start DFS from first character
        DFS(0, '', '', l, r)
        return(ans)