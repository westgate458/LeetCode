# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:55:05 2020

@author: Tianqi Guo
"""

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """           
        c = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if (board[i][j] == 'X') and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):                     
                    c += 1                    
        return c