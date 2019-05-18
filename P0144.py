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
        
        # answer list and traverse stack
        ans, s = [], []
        # start traversal from root
        p = root
        # continue traversal if still nodes to visit
        while p or s:
            # if current pointer points to a node or leaf
            if p:     
                # place current node into stack for future right branch
                s.append(p)
                # preorder: add value of current node to answer list
                ans.append(s[-1].val)                
                # continue to left branch
                p = p.left
            # if current pointer points to none
            else:    
                # revisit the right branch of the most-recent node in stack
                p = s[-1].right
                # remove the most-recent node from stack
                s.pop()               
        
        # return the preorder traversal
        return ans
            
            