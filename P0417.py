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
        # deal with trivial case
        if not matrix:
            return []
        # s1, s2: size of the matrix
        # q1, q2: achievable tiles from two oceans
        s1, s2, q1, q2 = len(matrix), len(matrix[0]), set([]), set([])
        # add border tiles to the two collections
        for i in xrange(s1):
            q1.add((i,0))           
            q2.add((i,s2-1))            
        for i in xrange(s2):
            q1.add((0,i))           
            q2.add((s1-1,i))
        # function to check if each tile is achievable from the collection ocean
        def DFS(ocean):                
            # convert the collection into a list for DFS
            q = list(ocean)     
            # continue DFS until all achievable tiles are checked
            while q:
                # position of current tile
                i, j = q.pop()            
                # check its neighbors
                for ii, jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    # if neighbor tile is within borders
                    # and it is higher than current tile
                    # and we have not visited it before
                    if 0 <= ii < s1 and 0 <= jj < s2 and matrix[ii][jj] >= matrix[i][j] and ((ii,jj) not in ocean):
                        # add it to the DFS stack
                        q.append((ii,jj))
                        # add it to the collection
                        ocean.add((ii,jj)) 
            # return the updated collection
            return(ocean)        
        # for each collection, perform DFS
        # and take the intersection of the two sets
        return(DFS(q1) & DFS(q2))