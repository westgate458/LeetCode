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
        ans = []
        s = [root] if root else []
        
        while s:
            ans.append(s[-1].val)
            s = [c for n in s for c in [n.left,n.right] if c]           
        return ans

