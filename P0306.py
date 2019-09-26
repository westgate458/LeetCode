# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:04:53 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        def DFS(a, b, s):
            n, l = 0, len(s) - 1
            for i, c in enumerate(s):
                n = n * 10 + int(c) 
                if a == None or b == None:
                    if i == l: 
                        return False
                    elif DFS(b, n, s[i+1:]):
                        return True
                elif a + b == n:                    
                    if i == l: 
                        return True
                    elif DFS(b, n, s[i+1:]):
                        return True
                if s[0] == '0':
                    break
       
        return DFS(None, None, num)