# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:14:44 2019

@author: Tianqi Guo
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        l = len(s)
        ll = len(wordDict)
        wl = [len(word) for word in wordDict]
        
        f = [False for x in xrange(l+1)]        
        f[0] = True        
        for p in xrange(l):
            if f[p]:
                for w in xrange(ll):
                    pp = p + wl[w]                    
                    if (pp <= l) and (wordDict[w] == s[p:pp]):
                        f[pp] = True
        return f[-1]
        
        
        
s = "applepenapple"
wordDict = ["apple", "pen"]
s = "leetcode"
wordDict = ["leet", "code"]
test = Solution()
print test.wordBreak(s, wordDict)