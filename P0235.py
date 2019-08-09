# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 21:36:01 2019

@author: westg
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
        
        # Solution 1 beats 96.48%: recursion 
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        
        # Solution 2 beats 8.5%: BFS
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
        