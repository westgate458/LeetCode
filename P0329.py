# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:31:36 2019

@author: Tianqi Guo
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # sub function for DFS
        def DFS(i, j):        
            # if current grid has not been visited before
            # i.e. the subproblem has not been solved
            if not dp[i][j]: 
                # subscripts for its neighbors
                neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                # the lengths for four subproblems from neighbors
                ls = [0] * 4
                # solve for subproblems
                for idx, (ii, jj) in enumerate(neighbors):                   
                    # if neighbor is within board, and it satisfies the increasing path
                    if (0 <= ii < m) and (0 <= jj < n) and matrix[ii][jj] > matrix[i][j]:
                        # solve the subproblem and record length
                        ls[idx] = DFS(ii, jj)
                # solution to current problem from best subproblem
                dp[i][j] = max(ls) + 1
            # return current solution to previous grid
            return dp[i][j]
        # deal with trivial case        
        if not matrix:
            return 0        
        # size of the board
        m, n = len(matrix), len(matrix[0])
        # solution to each subproblems
        dp = [[0] * n for _ in xrange(m)]        
        # the final result is the max from all subproblems
        return max(DFS(i,j) for i in xrange(m) for j in xrange(n))