# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:45:32 2019

@author: Tianqi Guo
"""

# Solution 1: dict(set)
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.d = defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.d[len(word)].add(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        words_left = self.d[len(word)]
        
        if not words_left:
            return False
        
        if word in words_left:
            return True
        
        for i in xrange(len(word)):
            if word[i] != '.':
                words_left = [w for w in words_left if w[i] == word[i]]
                if not words_left:
                    return False
                
        return True


## Solution 2: Trie + DFS
#class WordDictionary(object):
#
#    def __init__(self):
#        """
#        Initialize your data structure here.
#        """
#        self.d = {}
#        self.isWord = True
#
#    def addWord(self, word):
#        """
#        Adds a word into the data structure.
#        :type word: str
#        :rtype: None
#        """
#        node = self.d
#        for c in word:
#            if c not in node:                
#                node[c] = {}              
#            node = node[c]
#        node[self.isWord] = True
#        
#
#    def search(self, word):
#        """
#        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#        :type word: str
#        :rtype: bool
#        """
#
#        def dfs(node, word):
#            
#            if not word:
#                return node.get(self.isWord, False)
#            else:
#                c = word[0]           
#                if c == '.':
#                    for key in node:                        
#                        if (key != self.isWord) and dfs(node[key], word[1:]):
#                            return True
#                elif c in node:
#                    return dfs(node[c], word[1:])
#                else:
#                    return False  
#            
#        return dfs(self.d, word)