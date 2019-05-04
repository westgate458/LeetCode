# -*- coding: utf-8 -*-
"""
Created on Fri May  3 23:02:25 2019

@author: Tianqi Guo
"""
from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        l = len(s)        
        wl = [len(word) for word in wordDict]
        wl_set = set(wl)
        
        f = defaultdict(list)  
        f[0].append(0)
        for p in xrange(l):
            if p in f:
                for w in wl_set:
                    pp = p + w                    
                    if (pp <= l) and (s[p:pp] in wordDict):
                        f[pp].append(p)
        
        self.ans = []
        
        def dfs(p,combo):            
            if p == 0:                
                self.ans.append(combo)                
            else:
                for pp in f[p]:
                    dfs(pp, ' ' + s[pp:p] + combo)        
        
        if f[l]:
            dfs(l, '')
            return [ans[1:] for ans in self.ans] 

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

test = Solution()
print test.wordBreak(s, wordDict)