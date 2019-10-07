# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:41:24 2019

@author: Tianqi Guo
"""
# cheat by calculating this outside Solution class
import string
# look up table to convert each character to an unique binary representation
# a: 0x25+1 and z: 1+0x25
d = {c: 1<<i for (i, c) in enumerate(string.ascii_lowercase)}
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """        
        # word_coded: word after character-wise conversion
        # word_ls: length of each word
        # ans: max length product
        # l: number of words
        word_coded, word_ls, ans, l = [], [], 0, len(words)
        
        # convert each word to binary representation
        for word in words:
            # by taking bit-wise OR, if a word has a certain character, its c-th bit is 1
            n = 0
            for c in word:
                n |= d[c]
            word_coded.append(n)
            # also record its length
            word_ls.append(len(word))
        
        # then try all combinations of two words
        for i in range(l-1):
            for j in range(i+1,l):
                # checking common characters by bit-wise AND of the binary representations
                # and check if length product is larger than current answer
                if not (word_coded[i] & word_coded[j]) and (word_ls[i] * word_ls[j] > ans):
                    # update max length product
                    ans = word_ls[i] * word_ls[j]                
        # return max length product
        return ans