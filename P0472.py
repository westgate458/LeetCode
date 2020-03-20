# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:36:47 2020

@author: Tianqi Guo
"""

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """ 
        # Solution 1 beats 99.18%: magic
        words = set(words)
        def check(word):
            for i in xrange(1,len(word)):
                if (word[:i] in words) and ((word[i:] in words) or check(word[i:])): return True
            return False
        return [w for w in words if check(w)]
        
        # Solution 2 beats 48.50%: Trie + DFS + memorization
        self.trie = {}
        self.isWord = True
        self.seen = collections.defaultdict(bool)
        def DFS(word): 
            if word and (word not in self.seen):                
                node = self.trie
                for p, c in enumerate(word):                
                    if c not in node: return False                
                    node = node[c]  
                    if (self.isWord in node) and DFS(word[p+1:]):
                        self.seen[word] = True
                        break
                self.seen[word] = (self.isWord in node)
            return self.seen[word]        
        res = []
        for word in sorted(words,key=lambda x:len(x)):
            if DFS(word): res.append(word)
            node = self.trie
            for c in word:
                if c not in node: node[c] = {}              
                node = node[c]
            node[self.isWord] = True 
            self.seen[word] = True
        return res