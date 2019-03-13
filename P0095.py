# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:34:56 2019

@author: Tianqi Guo
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def construct(begin, end): 
            if (begin, end) in self.dict:
                return self.dict[(begin, end)]
            elif begin > end:
                return [None]
            elif begin == end:
                return [TreeNode(begin)]
            else:
                root_list = []
                for mid in range(begin,end+1):   
                    for left in construct(begin, mid-1):
                        for right in construct(mid+1, end):
                            root = TreeNode(mid)
                            root.left = left
                            root.right = right
                            root_list.append(root) 
                self.dict[(begin, end)] = root_list
            return root_list
        
        if n == 0:
            return []
        else:
            self.dict = {} 
            return construct(1,n)
    

n = 3
test = Solution()
root_list = test.generateTrees(n)  