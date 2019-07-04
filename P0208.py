# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:24:51 2019

@author: Tianqi Guo
"""

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """        
        self.d = {}
        self.isWord = True
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """        
        node = self.d
        for c in word:
            if c not in node:                
                node[c] = {}              
            node = node[c]
        node[self.isWord] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.d
        for c in word:
            if c not in node:                
                return False
            node = node[c]             
        return node.get(self.isWord, False)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.d
        for c in prefix:
            if c not in node:                
                return False
            node = node[c]              
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)