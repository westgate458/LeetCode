# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:47:59 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        # subfunction that solves subproblems recursively
        def DFS(node):
            # for each node return the max profit if
            # (rob current house, skip current house)
            # first deal with trivial case            
            if not node: return (0,0)     
            # solve two sub problems first
            l, r = DFS(node.left), DFS(node.right)                      
            # there are the following options
            # 1) rob current house, skip its two children houses
            # 2) skip current hosue, rob left house, and rob right house
            # 3) skip current house, rob left house, and skip right house
            # 4) skip current hosue, skip left hosue, and rob right hosue
            # 5) skip current hosue, skip left house, and skip right house
            # return 1) and max from 2)~5)
            return (l[1] + r[1] + node.val, max(l) + max(r))        
        # for the root, return the larger profit from its two options
        return max(DFS(root))