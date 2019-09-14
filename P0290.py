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
        # split string into words
        words = str.split(' ')
        # check if one to one mapping is possible
        if (len(words) != len(pattern)) or (len(set(words)) != len(set(pattern))):
            return False
        # mapping dictionary of d[a] = 'dog'
        d = {}
        # check each character in pattern
        for i in range(len(pattern)):
            # if we have seen this pattern and it is mapped to another word
            if (pattern[i] in d) and (d[pattern[i]] != words[i]):
                # word is not following pattern
                return False
            # if we have not seen this or it agrees with pervious mapping
            else:
                # assign the mapping
                d[pattern[i]] = words[i]           
        # after checking all words and pattern, no conflict was found
        # words are following the given pattern
        return True
        