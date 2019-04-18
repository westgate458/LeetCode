# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:51:58 2019

@author: westg_000
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """     
        
        s = s.lower()
        h, t = 0, len(s) - 1

        while h <= t:
        
            if not ('a' <= s[h] <= 'z' or '0' <= s[h] <= '9'):
                h += 1
                continue
                
            if not ('a' <= s[t] <= 'z' or '0' <= s[t] <= '9'):
                t -= 1
                continue
            
            if s[h] == s[t]:
                h += 1
                t -= 1
            else:
                return False
             
        return True

s = "race a car"
test = Solution()
print test.isPalindrome(s)
            
        
        
        
            