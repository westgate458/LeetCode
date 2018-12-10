# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:57:23 2018

@author: Tianqi Guo
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        # relative position within the 3x3 submatrix
        inc_j = [0,1,2,0,1,2,0,1,2]
        inc_i = [0,0,0,1,1,1,2,2,2]
        
        # positions lists of dots
        ii = []
        jj = []
        
        # look for all dots and record positions
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    ii.append(i)
                    jj.append(j)
        
        # number of dots
        num_of_dots = len(ii)
        
        # steps stores [current dot number, current digit to try, available digits]
        steps = [[-1]]
        # n is current dot to fill
        n = 0        
        # continue DFS until all dots are filled
        while n <= num_of_dots - 1:
            
            # position of current dot
            i = ii[n]
            j = jj[n]  
            
            # if in last step, the current dot was already filled (but then failed in later dots)
            if steps[-1][0] == n:                
                # this time round, fill current dot with next available digit
                char_n = steps[-1][1] + 1
                # if still available digits left
                if char_n + 1 <= len(steps[-1][2]):
                    # update 'current digit to try' in this step
                    steps[-1][1] = char_n
                    # fill board with the digit
                    board[i][j] = steps[-1][2][char_n]
                    # proceed to next dot
                    n = n + 1
                # if no available digits left
                else:
                    # reverse the filling to '.'
                    board[i][j] = '.'
                    # current step failed, remove from steps
                    steps.pop(-1)
                    # trace back to previous dot
                    n = n - 1                
            # if last step was a different dot
            else:
                # first identify what digits are available for current dot
                # coordinates of the top left element of the matrix current dot resides in
                r = i/3 * 3
                c = j/3 * 3
                # all legal digits
                available = '123456789'
                # check all elements in the row, column, and matrix that current dot resides in
                for m in range(9):
                    # exclude the digits already in board from available digits
                    available = available.replace(board[i][m],'') 
                    available = available.replace(board[m][j],'') 
                    available = available.replace(board[r+inc_i[m]][c+inc_j[m]],'')
                # if still available digits left for current dot to try
                if len(available) > 0:
                    # record current step
                    steps.append([n,0,available])
                    # fill the board with the first available digit
                    board[i][j] = available[0]
                    # proceed to next dot
                    n = n + 1
                # if no available digits left
                else:
                    # rollback to previous step (dot)
                    n = n - 1                
                          
        print(board)
                              
                
            
        
        
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

test = Solution()
print(test.solveSudoku(board))