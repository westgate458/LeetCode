# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:38:31 2019

@author: Tianqi Guo
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        # traverse pointer starting from root
        p = root  
        # pointers for previous node, and the first mis-placed node
        pre_v = p1 = None
        # stack for in order trasverse
        s = []         
        
        # continue traversing while still more nodes to check
        while p or s:
            
            # while more left nodes exist
            while p:                
                # place current node in the stack
                s.append(p)
                # move on to its left child
                p = p.left             
            
            # pop the most recently visited node
            p = s.pop()                     
                        
            # if the first mis-placed node has not been found
            # and current node is not the smallest number
            # and previous value is larger than current value
            if (not p1) and pre_v and (pre_v.val > p.val):   
                # previous node is the first mis-placed node                     
                p1 = pre_v                        
            # if the first mis-placed node has already been found
            # and current node value is larger than the first mis-placed node value
            elif p1 and (p.val > p1.val):                        
                # previous node is the 2nd mis-placed node
                # terminate traversing
                break               
            # update previous node as current node
            pre_v = p
            
            # move on to the right child of current node
            p = p.right 
        
        # switch values between the two mis-placed nodes
        pre_v.val, p1.val = p1.val, pre_v.val         
        # return nothing since swapping is in-place
        return