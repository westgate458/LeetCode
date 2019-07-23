# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:45:32 2019

@author: Tianqi Guo
"""

# Solution 1: dict(set) beats 100%
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        # use dictionary to record words of each length
        self.d = defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        # add current word to key of its length
        self.d[len(word)].add(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # search word among all of its length
        words_left = self.d[len(word)]
        
        # if there was no word of its length
        if not words_left:
            # simply does not exist
            return False
        
        # if current word does not contain '.' and it exists
        if word in words_left:
            # return found
            return True
        
        # deal with '.' case
        for i in xrange(len(word)):
            # if current character is not '.'
            if word[i] != '.':
                # filter words by current character, only keep matching words
                words_left = [w for w in words_left if w[i] == word[i]]
                # if not word left after filtering
                if not words_left:
                    # current word does not exist
                    return False
        
        # if there are still words left after filtering by the last character
        # the word exists
        return True


## Solution 2: Trie + DFS beats 21.7%
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