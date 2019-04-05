# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:58:33 2019

@author: Tianqi Guo
"""

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """     
        
        # Solution 1 
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        original_right = root.right
        
        root.right = root.left    
        root.left = None
        
        while root.right:
            root = root.right
        root.right = original_right
        
        
        # Solution 2
        if not root:
            return
        def in_order_trasversal(root):            
            if not root:
                return            
            self.s.append(root)
            in_order_trasversal(root.left)
            in_order_trasversal(root.right)            
        self.s = []
        in_order_trasversal(root)
        for i in range(len(self.s)-1):
            self.s[i].left = None
            self.s[i].right = self.s[i+1]            
        self.s[-1].left = None   
        
        