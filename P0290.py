# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:30:09 2019

@author: Tianqi Guo
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """        
        words = str.split(' ')
        
        if (len(words) != len(pattern)) or (len(set(words)) != len(set(pattern))):
            return False
       
        d = {}
        for i in range(len(pattern)):
            if (pattern[i] in d) and (d[pattern[i]] != words[i]):
                return False
            else:
                d[pattern[i]] = words[i]           
        return True
        