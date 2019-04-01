# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:18:44 2019

@author: Tianqi Guo
"""

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # deal with trivial case
        if not root:
            return []      
        
        # stack storing nodes at each level
        s = [root]
        # answer list storing values from each level
        ans = []
        
        # counter to mark the zigzag direction at each level
        c = 0
        # continue traversing while still nodes left
        while s:         
            # update level counter
            c = c + 1
            # if odd level
            if c%2 == 1:
                # traverse from left to right
                ans.append([n.val for n in s])  
            # if even level
            else:
                # traverse from right to left
                ans.append([n.val for n in s[::-1]])
                
            # continue to next level
            # update s and place children into s if not none    
            s = [child for n in s for child in [n.left, n.right] if child]              
        
        # return the zigzag values at each level    
        return ans