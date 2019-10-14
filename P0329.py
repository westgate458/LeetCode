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
        def DFS(i, j):            
            if not dp[i][j]: 
                neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                ls = [0] * 4
                for idx, (ii, jj) in enumerate(neighbors):                   
                    if (0 <= ii < m) and (0 <= jj < n) and matrix[ii][jj] > matrix[i][j]:
                        ls[idx] = DFS(ii, jj)
                dp[i][j] = max(ls) + 1
            return dp[i][j]
                
        if not matrix:
            return 0        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in xrange(m)]        
        return max(DFS(i,j) for i in xrange(m) for j in xrange(n))