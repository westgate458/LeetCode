# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:27:55 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        s = [root]
        
        while s:
                        
            vals = [n.val if n else None for n in s]
                        
            l = len(vals)/2
            for i in range(l):
                if vals[i] != vals[-i-1]:
                    return False
            
            s = [[n.left, n.right] if n else [] for n in s]  
            s = [j for sub in s for j in sub]
            
        return True