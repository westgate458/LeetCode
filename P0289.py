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
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n): 
                for ii, jj in [(i, j+1), (i+1, j), (i+1, j-1), (i+1, j+1)]:
                    if 0 <= ii <= m-1 and 0 <= jj <= n-1:                        
                        board[i][j] += 10 * (board[ii][jj]%10)
                        board[ii][jj] += 10 * (board[i][j]%10)
                        
        for i in range(m):
            for j in range(n):     
                board[i][j] = int(board[i][j]//10 == 3 or (board[i][j]%10 == 1 and board[i][j]//10 == 2))