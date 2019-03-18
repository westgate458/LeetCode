# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 20:39:47 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # if current node is None
        if not root:
            # return empty list
            return []
        # if current node has value
        else:
            # current inoder trasversal is composed by
            # [inoder trasversal of left subtree] + [current node value] + [inoder trasversal of right subtree]
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
