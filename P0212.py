# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 21:11:09 2019

@author: Tianqi Guo
"""

class Solution(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """      
        # tree is to be expressed as nested dictionary
        self.d = {}
        # the extra state element to be included in the dictionary if current node is a word
        self.isWord = True
        # results contain all the words found
        self.res = set([])        

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
    
    def DFS(self, i, j, node, word):    
        
        # if current node corresponds to a word
        if self.isWord in node:
            # add it to the results
            self.res.add(word)       
        
        # mark current position on the board so we don't go backwards
        self.board[i][j] = ''
        # check its 4 neighbors, see if its character is in the child nodes
        # if true continue DFS in that direction with updated current word
        if i > 0 and self.board[i-1][j] in node:
            self.DFS(i-1,j,node[self.board[i-1][j]],word+self.board[i-1][j])
        if i < self.r-1 and self.board[i+1][j] in node:
            self.DFS(i+1,j,node[self.board[i+1][j]],word+self.board[i+1][j])
        if j > 0 and self.board[i][j-1] in node:
            self.DFS(i,j-1,node[self.board[i][j-1]],word+self.board[i][j-1])
        if j < self.c-1 and self.board[i][j+1] in node:
            self.DFS(i,j+1,node[self.board[i][j+1]],word+self.board[i][j+1])       
        # restore current character on the board
        self.board[i][j] = word[-1]    
                
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """     
        # create global variables for the board and its sizes
        self.board, self.r, self.c = board, len(board), len(board[0])
        # add each word to the Trie
        for word in words:
            self.insert(word)
        # try to start DFS from each character on the board
        for i in xrange(self.r):
            for j in xrange(self.c):
                # check if current character is on the first level of Trie
                if self.board[i][j] in self.d:
                    # start DFS from current position with current character as the word
                    self.DFS(i, j, self.d[self.board[i][j]], self.board[i][j])                
        # return all found words
        return list(self.res)

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]        
test = Solution()
print test.findWords(board, words)

        