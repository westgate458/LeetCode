# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:30:25 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0      
        
        # Solution 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1            
        
        # Solution 2
        s = [root]
        c = 0
        while s:         
            c = c + 1
            s = [child for n in s for child in [n.left, n.right] if child] 
        return c