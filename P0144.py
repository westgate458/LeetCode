# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:06:12 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ans, s = [], []
        p = root
        
        while p or s:
            if p:     
                s.append(p)
                ans.append(s[-1].val)                
                p = p.left
            else:    
                p = s[-1].right
                s.pop()               
            
        return ans
            
            