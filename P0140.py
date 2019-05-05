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
        
        # length of string
        l = len(s)       
        # word lengths
        wl = [len(word) for word in wordDict]
        # set of word lengths
        wl_set = set(wl)
        
        # dictionary stores all previous points that lead to current position
        f = defaultdict(list)
        # arbitrary value for empty substring
        f[0].append(0)
        # check each substring
        for p in xrange(l):
            # if current position can be accessed from starting point
            # i.e. current substring can be segmented
            if p in f:
                # check all possible word lengths
                for w in wl_set:
                    # end of next substring
                    pp = p + w     
                    # if a matching is found
                    if (pp <= l) and (s[p:pp] in wordDict):
                        # add current position to the dictionary entry of next position
                        f[pp].append(p)
        
        # answer of all possible segmentations
        self.ans = []
        # dfs reconstructs the paths\segmentations from end
        def dfs(p,combo):            
            # if have reached the starting point
            if p == 0:                
                # current combo is a valid segmentation
                self.ans.append(combo)                
            # if have not reached the starting point 
            else:
                # for all points that lead to current point from the starting point
                for pp in f[p]:
                    # continue dfs with updated word combo
                    dfs(pp, ' ' + s[pp:p] + combo)        
        
        # if the endpoint has previous points
        # i.e. whole string is segmented
        if f[l]:
            # start dfs from the endpoint
            dfs(l, '')
            # return the segmentations
            return [ans[1:] for ans in self.ans] 

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

test = Solution()
print test.wordBreak(s, wordDict)