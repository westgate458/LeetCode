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
        def fill_board(rows,sums,diffs):
    
            # rows: position of queen in each row
            # length of rows: current row

            row = len(rows)

            if row == n:
                board = ['.'*c+'Q'+'.'*(n-1-c) for c in rows]
                ans.append(board)
                return 
            
            for clm in range(n):
                if (not (clm in rows)) and (not ((clm + row) in sums)) and (not ((clm - row) in diffs)):
                    fill_board(rows + [clm],sums + [clm + row],diffs + [clm - row]) 
                    
        ans = []
        fill_board([],[],[])   
        return ans
    
n = 9
test = Solution()
print(test.solveNQueens(n))