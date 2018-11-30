# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:56:59 2018

@author: Tianqi Guo
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        digits = "123456789"
        
        inc_i = [0,1,2,0,1,2,0,1,2]
        inc_j = [0,0,0,1,1,1,2,2,2]
        
        for i in range(9):
            checked_row = ""
            checked_clm = ""
            checked_sub = ""
            r = i/3 * 3
            c = i%3 * 3
            for j in range(9):
                cha = board[i][j]
                if digits.find(cha) > -1:
                    if checked_row.find(cha) == -1:
                        checked_row = checked_row + cha
                    else:
                        return False
                    
                cha = board[j][i]
                if digits.find(cha) > -1:
                    if checked_clm.find(cha) == -1:
                        checked_clm = checked_clm + cha
                    else:
                        return False  
                
                cha = board[r+inc_j[j]][c+inc_i[j]]        
                if digits.find(cha) > -1:
                    if checked_sub.find(cha) == -1:
                        checked_sub = checked_sub + cha
                    else:
                        return False 
                    
        return True            
            
        
board = [["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]]

test = Solution()
print(test.isValidSudoku(board))
            