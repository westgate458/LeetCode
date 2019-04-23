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
        
        # deal with trivial cases
        if not board or not board[0]:
            return 
        
        # size of the board
        rows = len(board)
        cols = len(board[0])
        
        # the queue for flood fill
        q = collections.deque()
        
        # check all marks on the borders
        # place the coordinates of 'O's in the queue, and flip them to 'V's
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

        # continue flood fill until all connected 'O's have been flipped
        while q:            
            # pop the coodinates of one of the 'O's
            r, c = q.popleft() 
            # check the connected components in the 4-neighborhood
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                # coordinates of the neighbor
                rr, cc = r + dr, c + dc
                # if the neighbor is an 'O'
                if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc] == 'O':
                    # flip it to 'V', and place it into the queue
                    board[rr][cc] = 'V'
                    q.append((rr,cc))
        
        # check all elements on the board
        for row in board:
            for c in range(cols):
                # flip the 'O's not visited to 'X's
                if row[c] == 'O':
                    row[c] = 'X'
                # restore the 'O's visited
                elif row[c] == 'V':
                    row[c] = 'O'         

board = [["X","X","X","X"],
         ["X","O","O","O"],
         ["O","X","O","X"],
         ["X","O","X","X"]]
        
test = Solution()
test.solve(board)
print board
        