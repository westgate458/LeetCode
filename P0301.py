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
        ans = set([])
        def DFS(p, combo, c, l, r):
            if p == len(s):               
                if c == '':
                    ans.add(combo)
            elif s[p] == '(':
                DFS(p+1, combo + '(', c + '(', l, r)
                if l > 0:
                    DFS(p+1, combo, c, l-1, r)
            elif s[p] == ')':
                if c and c[-1] == '(':
                    DFS(p+1, combo + ')',c[:-1], l, r)                
                if r > 0:
                    DFS(p+1, combo, c, l, r-1)
            else:
                DFS(p+1, combo + s[p], c, l, r)
        
        l, r = 0, 0      
        for char in s:
            if char == '(' :
                l += 1
            elif char == ')':
                if l > 0:
                    l -= 1                    
                else:
                    r += 1
        
        DFS(0, '', '', l, r)
        return(ans)