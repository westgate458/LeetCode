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
        # convert to hash table for fast look-up
        words = set(words)
        # subfunction for checking if current word is a concatenated one
        def check(word):
            # start from the first character check each possible split
            for i in xrange(1,len(word)):
                # current word is a concatenated one if the following conditions are met
                # if the 1st part after splitting is in words
                # if the 2nd part after splitting is in words, or it is a concatenated one
                if (word[:i] in words) and ((word[i:] in words) or check(word[i:])): return True
            # if all splits are checked, current word is not a concatenated one
            return False
        # check each word, and collect the concatenated ones
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