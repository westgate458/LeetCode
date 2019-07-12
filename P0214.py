# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:55:07 2019

@author: Tianqi Guo
"""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """        
        
        # Solution 1: beats 99%
        i = 0
        for c in s[::-1]:
            if c == s[i]:
                i += 1       
        if i == len(s):
            return s
        else:        
            return s[i:][::-1] + self.shortestPalindrome(s[:i]) + s[i:]
        
        # Solution 2: KMP beats 78%
        ss = s + '#' + s[::-1]        
        ls = [0] * len(ss)        
        ll, p = 0, 1  
        while p < len(ss):            
            if ss[ll] == ss[p]:
                ll += 1
                ls[p] = ll                
                p += 1                
            elif ll > 0:                
                ll = ls[ll-1]   
            else:                
                p += 1
        return s[ls[-1]:][::-1] + s

s = "aacd" 
s = ""
s = "aba"
s = "ab"
s = "abb"
s = "abcd" 
s = "aacecaaa" 
s = "babbbabbaba"

test = Solution()
print test.shortestPalindrome(s)











