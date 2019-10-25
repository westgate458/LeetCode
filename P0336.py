# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:33:54 2019

@author: Tianqi Guo
"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        # position of each word
        d = {word:idx for idx, word in enumerate(words)}
        
        # check if '' exists
        flag_empty = '' in d
        # ans list for all pairs
        ans = []
        # check each word
        for w in words:
            # if its a palindrome itself
            if w == w[::-1]:
                # then pair it with '' if it exists
                if w and flag_empty:      
                    ans += [d[''], d[w]], [d[w], d['']]
            # if its reversed version exists
            elif w[::-1] in d:              
                # pair the two
                ans.append([d[w], d[w[::-1]]])
            # split current word into two parts
            for i in xrange(1,len(w)):         
                # check if left and right parts are palindrome
                l, r = w[:i], w[i:]  
                # if yes and the reversed version of the other half exists
                # pair current word with the reversed word
                if l == l[::-1] and r[::-1] in d:
                    ans.append([d[r[::-1]], d[w]])
                if r == r[::-1] and l[::-1] in d:
                    ans.append([d[w], d[l[::-1]]])        
        # return all pairs
        return ans
                    
            