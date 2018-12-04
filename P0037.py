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
      
        inc_j = [0,1,2,0,1,2,0,1,2]
        inc_i = [0,0,0,1,1,1,2,2,2]
        
        ii = []
        jj = []
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    ii.append(i)
                    jj.append(j)
        
        num_of_dots = len(ii)
                    
        steps = [[-1]]
        n = 0        
        while n <= num_of_dots - 1:
            
            i = ii[n]
            j = jj[n]  
            
            if steps[-1][0] == n:                
                char_n = steps[-1][1] + 1
                if char_n + 1 <= len(steps[-1][2]):
                    steps[-1][1] = char_n
                    board[i][j] = steps[-1][2][char_n]
                    n = n + 1
                else:
                    board[i][j] = '.'
                    steps.pop(-1)
                    n = n - 1                
            else:
                r = i/3 * 3
                c = j/3 * 3
                available = '123456789'
                for m in range(9):
                    available = available.replace(board[i][m],'') 
                    available = available.replace(board[m][j],'') 
                    available = available.replace(board[r+inc_i[m]][c+inc_j[m]],'')
                    
                if len(available) > 0:
                    steps.append([n,0,available])
                    board[i][j] = available[0]
                    n = n + 1
                else:
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