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
        l = len(s1)
        if s1 == s2:
            return True        
        elif l > 1:
            if sorted(s1) != sorted(s2):
                return False
            for i in range(l-1):
                if self.isScramble(s1[0:i+1], s2[0:i+1]) and self.isScramble(s1[i+1:], s2[i+1:]):
                    return True
                if self.isScramble(s1[0:i+1], s2[-(i+1):]) and self.isScramble(s1[i+1:], s2[:l-(i+1)]):
                    return True
        return False
        
s1 = "great"
s2 = "raget"

test = Solution()
print test.isScramble(s1,s2)
        
        
        
        
        
    
