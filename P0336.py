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
        
        d = {word:idx for idx, word in enumerate(words)}
        
        ans = []
        for w in words:
            if w == w[::-1]:
                if w and '' in d:      
                    ans += [d[''], d[w]], [d[w], d['']]
            elif w[::-1] in d:                
                ans.append([d[w], d[w[::-1]]])
            for i in xrange(1,len(w)):                
                l, r = w[:i], w[i:]  
                if l == l[::-1] and r[::-1] in d:
                    ans.append([d[r[::-1]], d[w]])
                if r == r[::-1] and l[::-1] in d:
                    ans.append([d[w], d[l[::-1]]])                 
        return ans
                    
            