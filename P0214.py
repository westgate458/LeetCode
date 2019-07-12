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
        
        for i in range(len(s)):  
            ss = s[len(s)-i:][::-1] + s            
            if ss == ss[::-1]:
                return ss
        return ''
        
#        if s == s[::-1]:
#            return s
#        
#        ans = float('inf')
#        ss = ''
#        
#        for i in range(int(round(len(s)/2.0))):   
#            
#            l = 1
#            while i-l>=0 and s[i-l] == s[i+l]:
#                l += 1                  
#                
#            if l == i+1 and len(s)-(2*l+1) < ans:
#                ans = len(s)-(2*l+1)
#                ss = s[i+1:][::-1] + s[i:]
#            
#            l = 1
#            while i-l+1>=0 and i+l < len(s) and s[i-l+1] == s[i+l]:
#                
#                l += 1                  
#            if l == i+2 and len(s)-2*l < ans:                
#                ans = len(s)-2*l
#                ss = s[i+1:][::-1] + s[i+1:]
#            
#        return ss







s = "ab"
s = "aba"
s = "abb"
s = "abcd" 
s = "aacecaaa" 
s = "aacd" 
s = ""
test = Solution()
print test.shortestPalindrome(s)











