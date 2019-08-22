# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:29:27 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # Solution 1 beats 99.27%: iteration
        if not root:
            return []        
        ans, s, p = [], [root], [str(root.val)]    
        while s:
            ss = s.pop()
            pp = p.pop()
            if (not ss.left) and (not ss.right):
                ans.append(pp)
            else:
                if ss.left:
                    s.append(ss.left)
                    p.append(pp + '->' + str(ss.left.val))
                if ss.right:
                    s.append(ss.right)                   
                    p.append(pp + '->' + str(ss.right.val))
        return ans
        
#        # Solution 2 beats 32.71%: recursion
#        if not root:
#            return []    
#        temp = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)        
#        if not temp:
#            return [str(root.val)]
#        else:
#            c = str(root.val)
#            return [c +'->'+s for s in temp]     