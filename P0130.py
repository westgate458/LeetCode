# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 23:39:29 2019

@author: Tianqi Guo
"""

import collections
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return 
        
        rows = len(board)
        cols = len(board[0])
        
        q = collections.deque()
        
        for c in range(cols):
            if board[0][c] == 'O':
                q.append((0,c))
                board[0][c] = 'V'
            if board[rows-1][c] == 'O':
                q.append((rows-1,c))
                board[rows-1][c] = 'V'
                
        for r in range(rows):
            if board[r][0] == 'O':
                q.append((r,0))
                board[r][0] = 'V'
            if board[r][cols-1] == 'O':
                q.append((r,cols-1))
                board[r][cols-1] = 'V'

        
        while q:            
            r, c = q.popleft()            
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc] == 'O':
                    board[rr][cc] = 'V'
                    q.append((rr,cc))
                
        for row in board:
            for c in range(cols):
                if row[c] == 'O':
                    row[c] = 'X'
                elif row[c] == 'V':
                    row[c] = 'O' 
        

board = [["X","X","X","X"],
         ["X","O","O","O"],
         ["O","X","O","X"],
         ["X","O","X","X"]]
        
test = Solution()
test.solve(board)
print board
        