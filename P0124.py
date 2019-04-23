# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:11:20 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # dfs function traverse the whole tree only once
        def dfs(node):        
            
            # all sum candidates
            # 0 corresponds to if two subtrees return negative sum
            # we do not include either of them in current level
            sums = [0]
            
            # if left is not empty
            if node.left:
                # consider max sum path in left subtree that contains left child node
                sums += [dfs(node.left)]
            # if right is not empty
            if node.right:
                # consider max sum path in right subtree that contains right child node
                sums += [dfs(node.right)]                               
            
            # first scenario: path that links out to parent node thru current node
            # we choose to include one of left\right sub path, or neither of them
            # second scenario: path that links left-right subtrees thru current node
            # we calculate the total sum include current node
            sum_linked_out = max(sums) + node.val            
            sum_with_in = sum(sums) + node.val
            
            # update the max sum if a larger sum is found
            self.ans = max(self.ans, sum_linked_out, sum_with_in)          
            
            # only return the path that links out to parent node
            # since paths within already compared with the max sum
            # and parent node can not be included in the path within
            return sum_linked_out
        
        # start with trivial path
        self.ans = root.val
        # search for paths from root
        dfs(root)
        
        # return found max sum
        return self.ans