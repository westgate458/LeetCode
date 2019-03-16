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
        
        
        p = root  
        pre_v = p1 = None
        s = []         
          
        while p or s:
            
            while p:                
                s.append(p)               
                p = p.left             
            
            p = s.pop()                     
                        
            if (not p1) and pre_v and (pre_v.val > p.val):                        
                p1 = pre_v                        
            elif p1 and (p.val > p1.val):                        
                break              
            pre_v = p
                    
            p = p.right 
            
        pre_v.val, p1.val = p1.val, pre_v.val         
        return