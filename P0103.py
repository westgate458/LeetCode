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
        if not root:
            return []        
        
        s = [root]
        ans = []
        
        c = 0
        while s:         
            c = c + 1
            if c%2 == 1:
                ans.append([n.val for n in s])   
            else:
                ans.append([n.val for n in s[::-1]])
                
            s = [child for n in s for child in [n.left, n.right] if child]              
            
        return ans