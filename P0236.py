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
        # Case 1: if root is either p or q, then it is the LCA
        if root == p or root == q:
            return root        
        # check left and right subtrees separately
        left = right = None        
        # if left tree exists
        if root.left:
            # look for p and q in left tree
            left = self.lowestCommonAncestor(root.left, p, q)        
        # if right tree exists
        if root.right:
            # look for p and q in right tree
            right =  self.lowestCommonAncestor(root.right, p, q)        
        # if p and q are found separately in left and right subtrees
        if left and right:
            # then current node is teh LCA
            return root        
        # if both of them are still none: p and q not found, return none
        # if one of them is still none, it means two of the following
        # 1) one of p or q is not found
        # 2) LCA is already found in one of the subtrees
        else:
            # in the case of 
            # 1) return the found non-none value of p or q
            # 2) return the found non-none value of LCA
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