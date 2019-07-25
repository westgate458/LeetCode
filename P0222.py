# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 20:55:19 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        s = [root] 
        count = 0        
        while s[-1]: 
            count += 1 
            s = [child for n in s for child in [n.left, n.right]]        
        return 2**count - 1 + len([n for n in s if n])