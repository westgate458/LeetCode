# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:37:25 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
        # last value of each layer
        ans = []
        # stack for BFS, start with root
        s = [root] if root else []
        # do BFS layer by layer
        while s:
            # add the value of the last node in this layer to the answer            
            ans.append(s[-1].val)
            # for each node add its non-empty child to the BFS stack
            s = [c for n in s for c in [n.left,n.right] if c]       
        # return the side view
        return ans

