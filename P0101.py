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
        
        # stack storing nodes at each level
        s = [root]
        
        # continue checking each level while still nodes left
        while s:
            
            # gather all values from each node at this level
            # keep nones for symmetry
            vals = [n.val if n else None for n in s]
            
            # number of nodes
            l = len(vals)/2
            # check corresponding values
            for i in range(l):
                # see if the values are symmetric
                if vals[i] != vals[-i-1]:
                    # if not identical then it is asymmetric
                    return False
            
            # if symmetric continue to next level
            # gather child nodes if current node is not a leaf
            s = [[n.left, n.right] if n else [] for n in s]  
            # flatten the 2D list to 1D
            s = [j for sub in s for j in sub]
        
        # after all levels are checked the tree is symmetric
        return True