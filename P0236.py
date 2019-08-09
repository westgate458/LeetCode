# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:40:42 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        # Solution 1 beats 98.76%: recursion 
        if root == p or root == q:
            return root        
        left = right = None        
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)        
        if root.right:
            right =  self.lowestCommonAncestor(root.right, p, q)        
        if left and right:
            return root        
        else:
            return left or right
        
        # Solution 2 beats 5.0%: BFS
        from collections import deque
        path = {}
        path[root] = [root]
        s = deque()
        s.append(root)
        while ((p not in path) or (q not in path)):
            node = s.popleft()              
            if node.left:
                s.append(node.left)
                path[node.left] = path[node] + [node.left]
            if node.right:
                s.append(node.right)
                path[node.right] = path[node] + [node.right]
        for node in path[q][::-1]:
            if node in path[p]:
                return node