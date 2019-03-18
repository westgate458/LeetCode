# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:39:22 2019

@author: Tianqi Guo
"""



class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """        
#        def construct(begin, end): 
#            if (begin, end) in self.dict:
#                return self.dict[(begin, end)]
#            elif begin >= end:
#                return 1           
#            else:
#                tree_nums = 0
#                for mid in range(begin,end+1):
#                    tree_nums = tree_nums + construct(begin, mid-1) * construct(mid+1, end)                     
#                self.dict[(begin, end)] = tree_nums
#            return tree_nums
#        
#        if n == 0:
#            return 0
#        else:
#            self.dict = {} 
#            return construct(1,n)
        
        # f[n]: number of BST for n                
        f = [0] * (n+1)        
        # one BST for n = 0
        f[0] = 1
        # f[n] is constructed from all previous f[0..n-1]
        for num in range(1,n+1):
            # try all numbers as the mid number
            for mid in range(1,num+1):
                # add the number of all combinations formed by one BST from left and one BST from right 
                # to number of BST for current n
                f[num] += f[mid-1] * f[num-mid]
        # the number of BSTs for current n
        return f[n] 
n = 9
test = Solution()
print test.numTrees(n)

        