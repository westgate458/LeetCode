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
        # deal with trivial case
        if not root:
            return []        
        # initialize
        # 1) ans: all paths
        # 2) s: DFS stack
        # 3) p: path for each element in s
        ans, s, p = [], [root], [str(root.val)]    
        # continue DFS until all nodes are visited
        while s:
            # retrieve last node and its path
            ss = s.pop()
            pp = p.pop()
            # if current node is a leaf
            if (not ss.left) and (not ss.right):
                # add its path to answer
                ans.append(pp)
            # if it has children
            else:
                # check left and right sub tree
                # and append them into DFS stack s
                if ss.left:
                    s.append(ss.left)
                    p.append(pp + '->' + str(ss.left.val))
                if ss.right:
                    s.append(ss.right)                   
                    p.append(pp + '->' + str(ss.right.val))
        # return all the paths
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