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
        # number of ships
        c = 0
        # check each grid
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                # discover new ship by the two special grid
                # 1) top-most X in a vertical ship
                # 2) left-most X in a horizontal ship
                if (board[i][j] == 'X') and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):                     
                    c += 1      
        # number of discovered ships
        return c