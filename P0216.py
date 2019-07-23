# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:20:55 2019

@author: Tianqi Guo
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """               
        
        # DFS for all combinations
        # k: remaining numbers to be added
        # n: remaining sum to be achieved
        # combo: current combination so far
        def dfs(k, n, combo):     
            # check if reaching endpoint
            if k * n == 0:
                # if both k and n are zeros, i.e. all numbers are used and remaining sum is zero
                if k + n == 0:
                    # add current combination to the result
                    self.res.append(combo[1:])
            # if there are more numbers to be added
            else:
                # try all numbers that are larger than the previous one
                # and smaller than 10
                for num in range(combo[-1]+1,min(n+1,10)):
                    # continue DFS with updated k, n, and combo
                    dfs(k-1, n-num, combo + [num])
        
        # results for all combinations
        self.res = []            
        # start dfs with no number added and original target sum
        dfs(k, n, [0])
        # return all combinations found
        return self.res

k = 3
n = 9 
test = Solution()
print(test.combinationSum3(k, n))