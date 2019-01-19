# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 22:07:42 2019

@author: Tianqi Guo
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        # sub function filling each queen
        def fill_board(rows,sums,diffs):
            # each queen is maked by its
            # row, column, row + column, row - column
    
            # rows: position of queen in each row
            # length of rows: current row
            row = len(rows)
            
            # if all n rows have queen
            if row == n:
                # generate string representation of the board
                board = ['.'*c+'Q'+'.'*(n-1-c) for c in rows]
                # record current board
                ans.append(board)
                return 
            
            # if rows without queen remains
            # try each column
            for clm in range(n):
                # place queen if
                # 1) current column isn't taken
                # 2) current / diagonal isn't taken
                # 3) current \ diagonal isn't taken
                if (not (clm in rows)) and (not ((clm + row) in sums)) and (not ((clm - row) in diffs)):
                    # mark current queen by column number, sum, diff
                    # and move on to next row
                    fill_board(rows + [clm],sums + [clm + row],diffs + [clm - row]) 
        
        # initial answer set is empty
        ans = []
        # start filling board with no queen placed
        fill_board([],[],[])   
        # return answer set
        return ans
    
n = 9
test = Solution()
print(test.solveNQueens(n))