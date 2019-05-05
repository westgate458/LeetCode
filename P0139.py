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
        
        # length of string
        l = len(s)
        # number of words
        ll = len(wordDict)
        # word lengths
        wl = [len(word) for word in wordDict]
        
        # state function: if current substring can be segmented
        f = [False for x in xrange(l+1)]      
        # empty substring can be segmented
        f[0] = True        
        # check each substring
        for p in xrange(l):
            # if current substring can be segmented
            if f[p]:
                # try each word in the dictionary
                for w in xrange(ll):
                    # end of next substring
                    pp = p + wl[w]       
                    # if a matching is found
                    if (pp <= l) and (wordDict[w] == s[p:pp]):
                        # the substring ending at pp can be segmented
                        f[pp] = True
        
        # the final state function for the entire string
        return f[-1]
        
        
        
s = "applepenapple"
wordDict = ["apple", "pen"]
s = "leetcode"
wordDict = ["leet", "code"]
test = Solution()
print test.wordBreak(s, wordDict)