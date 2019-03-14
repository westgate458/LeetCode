# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:06:19 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        l = [root]
        bounds = [(-float('Inf'),float('Inf'))]
        
        while l:
            
            node = l.pop(0)
            low, high = bounds.pop(0)
            
            if node.left:
                if low < node.left.val < node.val:
                    l.append(node.left)
                    bounds.append((low, node.val))
                else:
                    return False
                
            if node.right:
                if node.val < node.right.val < high:
                    l.append(node.right)
                    bounds.append((node.val, high))
                else:
                    return False 
        
        return True