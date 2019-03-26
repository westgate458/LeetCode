# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:35:06 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []        
        
        s = [root]
        ans = []
        
        while s:         
            
            ans.append([n.val for n in s])   
            s = [child for n in s for child in [n.left, n.right] if child]              
            
        return ans[::-1]