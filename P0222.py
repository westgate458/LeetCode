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
        # level-wise tree traversal
        # start traversal from root
        s = [root] 
        # counter for complete levels
        count = 0        
        # if the last node of this level is not None
        # current level is not the last level
        while s[-1]: 
            # update level counter
            count += 1 
            # update nodes in level to move on
            s = [child for n in s for child in [n.left, n.right]]        
        # total number of nodes is the sum of
        # 1) number of nodes in complete levels
        # 2) number of nodes in last in-complete level
        return 2**count - 1 + len([n for n in s if n])