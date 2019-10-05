# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:41:24 2019

@author: Tianqi Guo
"""

import string
d = {c: 1<<i for (i, c) in enumerate(string.ascii_lowercase)}
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """        
        word_coded, word_ls, ans, l = [], [], 0, len(words)
        
        for word in words:
            n = 0
            for c in word:
                n |= d[c]
            word_coded.append(n)
            word_ls.append(len(word))

        for i in range(l-1):
            for j in range(i+1,l):
                if not (word_coded[i] & word_coded[j]) and (word_ls[i] * word_ls[j] > ans):
                    ans = word_ls[i] * word_ls[j]                
        
        return ans