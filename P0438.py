# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:26:21 2020

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """         
        def checkZeros(d):
            for key in ps:
                if d[key] != 0:
                    return False
            return True        
        ls, lp, res, d, ps = len(s), len(p), [], defaultdict(int), set(p)
        for c in p:
            d[c] += 1
        for c in s[:lp]:            
            d[c] -= 1
        if checkZeros(d):
            res.append(0)            
        for i in xrange(1,ls-lp+1):            
            d[s[i-1]] += 1
            d[s[i+lp-1]] -= 1                        
            if checkZeros(d):
                res.append(i)                 
        return(res)