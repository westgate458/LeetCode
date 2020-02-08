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
        # sub function to check if current window is an anagram
        def checkZeros(d):
            # check each character in p
            for key in ps:
                # if current window is an anagram, all counts should be zero
                if d[key] != 0:
                    # if non-zero found, it is not an anagram
                    return False
            # after all characters are checked, it is an anagram
            return True        
        # ls, lp: length of two strings
        # res: all starting positions of the anagrams
        # d: counts of all characters within current window
        # ps: unique characters in p
        ls, lp, res, d, ps = len(s), len(p), [], defaultdict(int), set(p)
        # count all characters in p
        for c in p:
            d[c] += 1
        # check first window in s
        for c in s[:lp]:            
            d[c] -= 1
        if checkZeros(d):
            res.append(0)        
        # check all following windowses
        for i in xrange(1,ls-lp+1):    
            # first remove the first character of previous window
            d[s[i-1]] += 1
            # then add the last character in current window
            d[s[i+lp-1]] -= 1                        
            # check if all counts are 0
            if checkZeros(d):
                # if yes we got an anagram
                res.append(i)             
        # return all the positions
        return(res)