# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:16:04 2019

@author: Tianqi Guo
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # size of the board
        m, n = len(board), len(board[0])
        # Step 1: record number of living cells around each cell
        for i in range(m):
            for j in range(n): 
                # check the neighboring cells after this one
                for ii, jj in [(i, j+1), (i+1, j), (i+1, j-1), (i+1, j+1)]:
                    # if the neighbor is within board
                    if 0 <= ii <= m-1 and 0 <= jj <= n-1:                        
                        # update two cells with the number of their living neighbors as the tens 
                        # i.e. 61 means current cell is alive, and there are 6 living neighbors
                        board[i][j] += 10 * (board[ii][jj]%10)
                        board[ii][jj] += 10 * (board[i][j]%10)
        # Step 2: update next state                
        for i in range(m):
            for j in range(n):     
                # current cell is alive at next time step if
                # 1) it is alive now, and it has 2 or 3 live neighbors
                # 2) it is dead now, and it has 3 live neighbors
                board[i][j] = int(board[i][j]//10 == 3 or (board[i][j]%10 == 1 and board[i][j]//10 == 2))