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
        
        # Solution 1: recursive approach
        
        # deal with trivial case
        if not root:
            return
        
        # flatten the two child braches first
        self.flatten(root.left)
        self.flatten(root.right)
        
        # make a copy pointer to the flattened original right list
        original_right = root.right
        
        # make the flattened left list the new right branch
        root.right = root.left    
        # now left branch should be empty
        root.left = None
        
        # find the last node in the flattened left (now right) list
        while root.right:
            root = root.right
        # put flattened original right list at the tail of the flattened current right branch
        root.right = original_right
        
        
        # Solution 2: via in order trasversal
#        if not root:
#            return
#        def in_order_trasversal(root):            
#            if not root:
#                return            
#            self.s.append(root)
#            in_order_trasversal(root.left)
#            in_order_trasversal(root.right)            
#        self.s = []
#        in_order_trasversal(root)
#        for i in range(len(self.s)-1):
#            self.s[i].left = None
#            self.s[i].right = self.s[i+1]            
#        self.s[-1].left = None   
        
        