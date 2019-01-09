# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:55:46 2019

@author: Tianqi Guo
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def fill_board(rows,sums,diffs):
    
            # rows: position of queen in each row
            # length of rows: current row

            row = len(rows)

            if row == n:
                self.ans = self.ans + 1
                return 
            
            for clm in range(n):
                if (not (clm in rows)) and (not ((clm + row) in sums)) and (not ((clm - row) in diffs)):
                    fill_board(rows + [clm],sums + [clm + row],diffs + [clm - row]) 
                    
        self.ans = 0
        fill_board([],[],[])   
        return self.ans
    
n = 9
test = Solution()
print(test.totalNQueens(n))