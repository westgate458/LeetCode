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
        
        # Solution 1: recursion beats 99%
        # head pointer
        i = 0
        # start from the tail
        for c in s[::-1]:
            # if current character from tail matches current character from head
            if c == s[i]:
                # move head pointer towards tail
                i += 1       
        # if by the time tail pointer reaches head
        # the head pointer also reaches the tail
        if i == len(s):
            # it means all characters match, current s is a palindrome
            # return itself
            return s
        # if the head pointer has not reached the tail
        # it means it was stuck somewhere along the way
        # and a copy of the substring from current i position till end
        # must be reversed and added in front of s to make s a palindrome
        else:        
            # add tail substring to the front, and recursively check the substring in the middle
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











