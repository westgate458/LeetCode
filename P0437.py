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
        # the dictionary to memorize all the accumulative sums from root until now
        self.d = defaultdict(int)
        # base case is one sum of 0
        self.d[0] = 1
        # sub function to check all sums along the way
        def DFS(node, cur_sum):            
            # node: current node
            # sum: accumulative sum from root until now
            if node:
                # res: how many paths found
                res = 0
                # update the sum
                cur_sum += node.val                
                # in the past, if we have already seen sum from root to node_pre that equal to (cur_sum - sum)
                # then the sum from node_pre to current node is then cur_sum - (cur_sum - sum) = sum
                # each of those node_pre gives a path of desired sum
                res += self.d[cur_sum - sum]               
                # we update the counts for current sum
                self.d[cur_sum] += 1                  
                # try each child node, and update the number of paths from those 
                res += DFS(node.left, cur_sum) + DFS(node.right, cur_sum)                
                # before we go back to the parent node, we restore the previous count of current sum
                self.d[cur_sum] -= 1    
                # return all results from child nodes and current node to parent
                return res
            # if current node is none
            else:
                # simply return 0
                return 0
        # start from the root, find all paths top-down, and collect results bottom-up
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