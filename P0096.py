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
                
        f = [0] * (n+1)        
        f[0] = 1
        for num in range(1,n+1):
            for mid in range(1,num+1):
                f[num] += f[mid-1] * f[num-mid]
        return f[n] 
n = 9
test = Solution()
print test.numTrees(n)

        