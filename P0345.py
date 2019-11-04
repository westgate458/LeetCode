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
        # ss: list of the string
        # vowels: chars need to be swapped
        # i, j: pointers at both ends
        ss, vowels, i, j = list(s), set('aeiouAEIOU'), 0, len(s)-1        
        # continue swapping until terminated inside
        while True:
            # continue updating the pointers until vowels are found
            while i < j and ss[i] not in vowels: i += 1
            while i < j and ss[j] not in vowels: j -= 1
            # if pointers have met then terminate swapping
            if i >= j : break            
            # swap the two vowels
            ss[i], ss[j] = ss[j], ss[i]
            # update the pointers
            i, j = i + 1, j - 1  
        # convert list back to string
        return ''.join(ss)