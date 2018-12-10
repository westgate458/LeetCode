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
        
        # all legal digits
        digits = "123456789"
        
        # relative position within the 3x3 submatrix
        inc_i = [0,1,2,0,1,2,0,1,2]
        inc_j = [0,0,0,1,1,1,2,2,2]
        
        # check each column, each row, and submatrix
        for i in range(9):
            # already checked digits for row, column, matrix
            checked_row = ""
            checked_clm = ""
            checked_sub = ""
            # coordinates of the top left element of each matrix
            r = i/3 * 3
            c = i%3 * 3
            # each element if the row, column, matrix
            for j in range(9):
                
                # current character from current row
                cha = board[i][j]
                # if character is a number
                if digits.find(cha) > -1:
                    # if not already exists
                    if checked_row.find(cha) == -1:
                        # add current char to the checked digits
                        checked_row = checked_row + cha
                    else:
                        # if already exists, Sudoku not valid
                        return False
                    
                # current character from current column
                cha = board[j][i]
                # if character is a number
                if digits.find(cha) > -1:
                    # if not already exists
                    if checked_clm.find(cha) == -1:
                        # add current char to the checked digits
                        checked_clm = checked_clm + cha
                    else:
                        # if already exists, Sudoku not valid
                        return False  
                    
                # current character from current matirx
                cha = board[r+inc_j[j]][c+inc_i[j]]   
                # if character is a number
                if digits.find(cha) > -1:
                    # if not already exists
                    if checked_sub.find(cha) == -1:
                        # add current char to the checked digits
                        checked_sub = checked_sub + cha
                    else:
                        # if already exists, Sudoku not valid
                        return False 
        
        # if no conflicts found, Sudoku is valid                    
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
            