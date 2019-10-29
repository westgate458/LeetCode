# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 19:08:36 2019

@author: Tianqi Guo
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """        
        ss, vowels, i, j = list(s), set('aeiouAEIOU'), 0, len(s)-1        
        while True:
            while i < j and ss[i] not in vowels: i += 1
            while i < j and ss[j] not in vowels: j -= 1
            if i >= j : break            
            ss[i], ss[j] = ss[j], ss[i]
            i, j = i + 1, j - 1           
        return ''.join(ss)