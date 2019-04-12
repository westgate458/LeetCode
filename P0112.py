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
        
        # Solution 1: recursive DFS
        # subfunction does the DFS
        def DFS(n, r):            
            # n: current node
            # r: remaining sum to match
            
            # remaining sum after current level
            rr = r - n.val            
            # if current node is a leaf
            if not n.left and not n.right:
                # if remaining sum is zero
                # i.e. the current path leads to the sum given
                if rr == 0:
                    # return path found
                    return True
                else:
                    # current leaf doesn't give the path desired
                    return False
            # if still branches to visit
            else:
                # check if at least if one of the two branches gives the desired path                
                return (n.left and DFS(n.left, rr)) or (n.right and DFS(n.right, rr))     
        
        # deal with trivial case
        if not root:            
            return False        
        else:
            # start DFS from the root node
            return DFS(root, sum)
        
        # Solution 2: level order traversal
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
            