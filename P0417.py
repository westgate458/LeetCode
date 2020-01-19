# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:57:20 2020

@author: Tianqi Guo
"""

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        s1, s2, q1, q2 = len(matrix), len(matrix[0]), set([]), set([])
        for i in xrange(s1):
            q1.add((i,0))           
            q2.add((i,s2-1))            
        for i in xrange(s2):
            q1.add((0,i))           
            q2.add((s1-1,i))
        def BFS(ocean):    
            q = list(ocean)     
            while q:
                i, j = q.pop()            
                for ii, jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 <= ii < s1 and 0 <= jj < s2 and matrix[ii][jj] >= matrix[i][j] and ((ii,jj) not in ocean):
                        q.append((ii,jj))
                        ocean.add((ii,jj)) 
            return(ocean)        
        return(BFS(q1) & BFS(q2))