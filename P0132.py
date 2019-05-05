# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:40:13 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        # cheat #1: check if entire string is a palindrome 
        if s == s[::-1]:
            # no need to cut
            return 0
        
        # length of string
        sl = len(s)
        
        # cheat #2: check if one cut is enough
        for c in xrange(sl):           
            # see if two parts are both palindromes 
            if s[:c+1] == s[:c+1][::-1] and s[c+1:] == s[c+1:][::-1]:
                # one cut is enough
                return 1
        
        # state function
        # minimum cut to generate palindromes for the substring ending at current position
        # initialize with its own position index, i.e. worst case one cut per character
        cuts = [x for x in xrange(-1,sl)]
        
        # check all substrings centered at current position        
        for c in xrange(sl):     
            
            # palindromes of odd lengths
            # half length of palindromes
            l = 0  
            # starting from current position, try to validate symmetry on both sides
            while 0 <= c - l and c + l < sl and s[c - l] == s[c + l]:
                # if a palindrome is found, update the minimum cut number for the ending position                
                cuts[c+l+1] = min(cuts[c+l+1], cuts[c-l] + 1)
                # increase half length and check next characters
                l += 1
            
            # palindromes of even lengths
            # half length of palindromes
            l = 0
            # starting from current position, try to validate symmetry on both sides
            while 0 <= c - l and c + l + 1 < sl and s[c - l] == s[c + l + 1]:
                # if a palindrome is found, update the minimum cut number for the ending position 
                cuts[c+l+2] = min(cuts[c+l+2], cuts[c-l] + 1)     
                # increase half length and check next characters
                l += 1             
        
        # the minimum cut for the entire string
        return cuts[-1]          

s = 'aabb'        
test = Solution()
print test.minCut(s)