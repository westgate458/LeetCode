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
        # tree is to be expressed as nested dictionary
        self.d = {}
        # the extra state element to be included in the dictionary if current node is a word
        self.isWord = True
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """        
        # start traversal from the root        
        node = self.d
        # determine the position of current word
        # by checking each of its characters
        for c in word:
            # if current character has not appeared before at this tree level
            if c not in node:                
                # add a new branch to current node
                node[c] = {}              
            # continue traversal by moving on to next level
            node = node[c]
        # include this extra state element, so we know this node is a word
        node[self.isWord] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        # start traversal from the root   
        node = self.d
        # determine the position of current word
        # by checking each of its characters
        for c in word:
            # if current character has not appeared before at this tree level
            if c not in node:                
                # then it does not exist in this tree
                return False
            # continue traversal by moving on to next level
            node = node[c]             
        # the word exists only when current node has been marked as a word
        # i.e. when 'haha' was inserted in the tree, 'ha' was not marked as a word
        # so when searching for 'ha', it does not exist in the tree
        return node.get(self.isWord, False)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        # start traversal from the root   
        node = self.d
        # determine the position of current prefix
        # by checking each of its characters
        for c in prefix:
            # if current character has not appeared before at this tree level
            if c not in node:  
                # then it does not exist in this tree
                return False
            # continue traversal by moving on to next level
            node = node[c]              
        # if all characters have appeared at their corresponding levels
        # word with this prefix must exist
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)