# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 21:11:42 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # if current nodes in both trees are None        
        if not p and not q:
            # current nodes match
            return True        
        
        # if one node is None while the other is not
        if not p or not q:
            # current nodes do not match
            return False
        
        # current BSTs are the same if
        # 1) values of current nodes are the same
        # 2) left children BSTs are the same
        # 3) right children BSTs are the same
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)    