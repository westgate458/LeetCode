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
        
        # make all characters lowercase
        s = s.lower()
        # head and tail pointers
        h, t = 0, len(s) - 1
        
        # continue comparing until pointers meet in the middle
        while h <= t:
            
            # head pointer moves on to next if trivial characters encountered
            if not ('a' <= s[h] <= 'z' or '0' <= s[h] <= '9'):
                h += 1
                continue
            # tail pointer moves on to next if trivial characters encountered    
            if not ('a' <= s[t] <= 'z' or '0' <= s[t] <= '9'):
                t -= 1
                continue
            
            # if two characters of interest are the same, move on to next ones
            if s[h] == s[t]:
                h += 1
                t -= 1
            # if they do not match, current string is not Palindrome
            else:
                return False
        
        # current string is Palindrome after all characters are validated
        return True

s = "race a car"
test = Solution()
print test.isPalindrome(s)
            
        
        
        
            