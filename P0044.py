# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 19:20:51 2018

@author: Tianqi Guo
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        i = 1
        while i < len(p):
            if (p[i] == '*') and (p[i-1] == '*'):
                p = p[0:i] + p[i+1:]
            else:
                i = i + 1  
                
        # length of two strings
        ls = len(s)
        lp = len(p)        
        
        match = [[False] * (lp+1) for x in range(ls+1)]
        # empty string matches itself
        match[0][0] = True
        
        for j in range(1,lp+1):            
            if p[j-1] == '*':
                match[0][j] = match[0][j-1] 

        for i in range(1,ls+1):
            for j in range(1,lp+1):                
                if (p[j-1] == '?') or (s[i-1] == p[j-1]):            
                    match[i][j] = match[i-1][j-1]         
                elif p[j-1] == '*':
                    match[i][j] = (match[i-1][j] or match[i][j-1]) 

        return match[-1][-1]

s = "adceb"
p = "*a*b"

test = Solution()
print(test.isMatch(s,p))    