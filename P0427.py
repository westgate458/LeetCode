# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:32:31 2020

@author: Tianqi Guo
"""

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """    
        # check each tile
        for row in grid:
            for n in row:
                # if current tile is not the same as the first tile
                # we need to split current grid
                if n != grid[0][0]:
                    # take the half length
                    ll = len(grid)/2  
                    # deal with the four quadrants, and add them as child nodes to current node
                    return Node(None, False, 
                                self.construct([row[:ll] for row in grid[:ll]]), 
                                self.construct([row[ll:] for row in grid[:ll]]), 
                                self.construct([row[:ll] for row in grid[ll:]]), 
                                self.construct([row[ll:] for row in grid[ll:]]))
                    
        # build the tree from top to bottom
        return Node(grid[0][0]==1 , True, None, None, None, None)