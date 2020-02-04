# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:11:03 2020

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """         
        # Solution 1 beats 97.54%： with memorization
        self.d = defaultdict(int)
        self.d[0] = 1
        def DFS(node, cur_sum):            
            if node:
                res = 0
                cur_sum += node.val                
                res += self.d[cur_sum - sum]               
                self.d[cur_sum] += 1                    
                res += DFS(node.left, cur_sum) + DFS(node.right, cur_sum)                
                self.d[cur_sum] -= 1    
                return res
            else:
                return 0
        return DFS(root, 0)
    
        # Solution 2 beats 45.39%： naive DFS
#        def DFS(node, target, isNew):            
#            if node:
#                res = 0
#                if node.val == target:
#                    res += 1
#                res += DFS(node.left, target-node.val, False) + DFS(node.right, target-node.val, False)                
#                if isNew:
#                    res += DFS(node.left, sum, True) + DFS(node.right, sum, True)                    
#                return res
#            else:
#                return 0
#        return DFS(root, sum, True)