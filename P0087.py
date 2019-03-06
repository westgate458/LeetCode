# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:18:35 2019

@author: Tianqi Guo
"""
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        # length of the string
        l = len(s1)
        # if the two strings match
        if s1 == s2:
            # return it is a matching
            return True    
        
        # if the two strings do not match
        # and they are longer than 1 so scrambles possible
        elif l > 1:
            
            # if the letters are not the same
            if sorted(s1) != sorted(s2):
                # scrambles won't match
                return False
            
            # try all the scrambles
            # change the order of all possible substrings
            # iterate over the length of the first substring
            for i in range(l-1):
                # see if the substrings match without scramble
                if self.isScramble(s1[0:i+1], s2[0:i+1]) and self.isScramble(s1[i+1:], s2[i+1:]):
                    return True
                # see if the substrings match after order reversed
                if self.isScramble(s1[0:i+1], s2[-(i+1):]) and self.isScramble(s1[i+1:], s2[:l-(i+1)]):
                    return True
        
        # if all possible scrambles do not match
        # then they are not scrambled strings
        return False
        
s1 = "great"
s2 = "raget"

test = Solution()
print test.isScramble(s1,s2)
        
        
        
        
        
    
