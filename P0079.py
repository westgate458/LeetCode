# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:13:20 2019

@author: Tianqi Guo
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def dfs(i, j, board, word):
            
            di = [0, 1, 0, -1]
            dj = [1, 0, -1, 0]
            
            if word == '':
                return True
            else:
                c = board[i][j]
                board[i][j] = ''
                for k in range(4):
                    ii = i + di[k]
                    jj = j + dj[k]
                    if (word[0] == board[ii][jj]) and (dfs(ii, jj, board, word[1:])):
                        return True
                board[i][j] = c
                return False
        
        m = len(board)
        n = len(board[0])
        
        board = [['.'] + row + ['.'] for row in board]
        board = [['.'] * (n+2)] + board + [['.'] * (n+2)]
        
        for i in range(m+2):
            for j in range(n+2):                
                if board[i][j] == word[0]:
                    c = board[i][j]                
                    board[i][j] = ''
                    if dfs(i, j, board, word[1:]):
                        return True
                    board[i][j] = c
        return False

        
board =[['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']]

word = "ABCCED"
        
test = Solution()
print test.exist(board, word)
      