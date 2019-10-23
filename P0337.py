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
        def DFS(node):
            if not node: return (0,0)            
            l, r = DFS(node.left), DFS(node.right)                      
            return (l[1] + r[1] + node.val, max(l) + max(r))        
        return max(DFS(root))