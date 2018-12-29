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
        
        # remove excessive *'s when they appear together
        i = 1
        while i < len(p):
            # look for back to back *'s
            if (p[i] == '*') and (p[i-1] == '*'):
                # remove the 2nd *
                p = p[0:i] + p[i+1:]
            else:
                # move on to next character
                i = i + 1  
                
        # length of two strings
        ls = len(s)
        lp = len(p)        
        
        # status array, match[i][j] marks if s[0:i] matches p[0:j]
        match = [[False] * (lp+1) for x in range(ls+1)]
        # empty string matches itself
        match[0][0] = True
        # if any character in p is *
        # it can be neglected to match empty string of s
        for j in range(1,lp+1):            
            if p[j-1] == '*':
                match[0][j] = match[0][j-1] 
        
        # determine if the substrings match
        for i in range(1,ls+1):
            for j in range(1,lp+1):        
                # if current characters match                                
                if (p[j-1] == '?') or (s[i-1] == p[j-1]):    
                    # whethter the entire substring matches depends on the preceeding substrings
                    match[i][j] = match[i-1][j-1]         
                # if the current character in p is *                
                elif p[j-1] == '*':
                    # current substrings match under two circumstrances
                    # 1) s[0:i-1] matches p[0:j], i.e. * can match one more character in s
                    # 2) s[0:i] matches p[0:j-1], i.e. * can match an empty string and be neglected
                    match[i][j] = (match[i-1][j] or match[i][j-1]) 
        
        # whether two strings match is indicated in the last element of the mactch array
        return match[-1][-1]

s = "adceb"
p = "*a*b"

test = Solution()
print(test.isMatch(s,p))    