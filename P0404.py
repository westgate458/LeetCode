# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:53:54 2020

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        s = [(root,False)]
        res = 0
        while s:
            n, isLeft = s.pop()
            if not n.left and not n.right:
                if isLeft:
                    res += n.val
            if n.left:
                s.append((n.left,True))
            if n.right:
                s.append((n.right,False))
        return res