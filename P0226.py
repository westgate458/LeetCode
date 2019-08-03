# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 22:07:39 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # deal with the trivial case or the final level
        if not root:
            return None
        
        # recursively invert the left and right child trees
        # then switch their positions at current level
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)        
        
        # return the inverted tree
        return root