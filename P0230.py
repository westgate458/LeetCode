# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 20:51:01 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        # Solution 1: iteratively        
        s, node, c = [], root, 0 
        while True:            
            while node:
                s.append(node)
                node = node.left            
            node = s.pop()
            c += 1            
            if c == k:
                return node.val            
            node = node.right
        
        
        # Solution 2: recursively    
        def helper(root, k):            
            if not root:
                return (0, None)
            nodes_left, res = helper(root.left, k)   
            if res != None:
                return (None, res)
            elif k == nodes_left + 1:
                return (None, root.val)
            else:
                nodes_right, res = helper(root.right, k - (nodes_left + 1))
                if res:
                    return (None, res)
                else:
                    return (nodes_left + nodes_right + 1, None)                
        _, res = helper(root, k)  
        return res
                