# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 22:21:46 2019

@author: Tianqi Guo
"""

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # deal with trivial case
        if not root:            
            return 0
        
        s = [root]
        l = [1]    
       
        while s:
            n = s.pop(0)
            c = l.pop(0)
            if n.left:
                s.append(n.left)
                l.append(c+1)
            if n.right:
                s.append(n.right)     
                l.append(c+1)
            if not n.left and not n.right:
                return c            
       
        return c