# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:48:40 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
               
        if not root:
            return []            
        ans = []        
        s = [root]            
        while s:
            node = s.pop()
            ans.append(node.val)            
            if node.left:
                s.append(node.left)                
            if node.right:
                s.append(node.right)        
        
        return ans[::-1]