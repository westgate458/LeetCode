# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:29:00 2019

@author: Tianqi Guo
"""

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        def DFS(n, r):            
            rr = r - n.val            
            if not n.left and not n.right:
                if rr == 0:
                    return True
                else:
                    return False
            else:
                return (n.left and DFS(n.left, rr)) or (n.right and DFS(n.right, rr))     
        
        if not root:            
            return False
        else:
            return DFS(root, sum)
        
#        s = [(root, sum - root.val)]   
#        while s:            
#            n, c = s.pop(0)                    
#            if n.left:
#                s.append((n.left, c - n.left.val))            
#            if n.right:
#                s.append((n.right, c - n.right.val))
#            if not n.left and not n.right and c == 0:
#                return True            
#        return False
            