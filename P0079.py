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
        
        # dfs subfunction to search the board for the word
        def dfs(i, j, board, word):
            
            # subscript changes to access 4 neighbors
            di = [0, 1, 0, -1]
            dj = [1, 0, -1, 0]
            
            # if remaining word is empty
            if word == '':
                # means all characters have been found                
                return True
            # if still more characters need to be found
            else:
                # temporarily replace current character on board with ''
                # to avoid moving backwards
                c = board[i][j]
                board[i][j] = ''
                # for each neighor
                for k in range(4):
                    # the neighbor's subscripts on board
                    ii = i + di[k]
                    jj = j + dj[k]
                    # the neighbor's character matchs 
                    # the first character in the remaining word
                    # then continue dfs at this neighbor position
                    if (word[0] == board[ii][jj]) and (dfs(ii, jj, board, word[1:])):
                        # if all remaining word could be matched on board
                        # toward this neighbor direction
                        return True
                # restore the character back to current position on board
                board[i][j] = c
                # if dead ends are met via all neighbor paths
                # word can't be matched via current point on board
                return False
        
        # size of the board
        m = len(board)
        n = len(board[0])
        
        # pad board to avoid subscripts beyond boundaries
        board = [['.'] + row + ['.'] for row in board]
        board = [['.'] * (n+2)] + board + [['.'] * (n+2)]
        
        # try to start the word search from every point on board
        for i in range(m+2):
            for j in range(n+2):                
                # if the current character on board 
                # matches the first character in the word
                if board[i][j] == word[0]:
                    # temporarily replace current character on board with ''
                    # to avoid moving backwards
                    c = board[i][j]                
                    board[i][j] = ''
                    # start dfs from current position
                    if dfs(i, j, board, word[1:]):
                        # if a matching could be achieved by dfs
                        return True
                    # restore the character back to current position on board
                    board[i][j] = c
        
        # if a matching could be found 
        # the function should have already returned True
        # so at this point it means no matching has been found
        return False

        
board =[['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']]

word = "ABCCED"
        
test = Solution()
print test.exist(board, word)
      