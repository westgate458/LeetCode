# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:23:47 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        r, c, res = len(matrix), len(matrix[0]), float('-inf')

        for L in xrange(c):
            sums = [0] * r
            for R in xrange(L, c):
                
                for rr in xrange(r):
                    sums[rr] += matrix[rr][R]                

                cur_sum, temp = 0, [0]

                for rrr, sm in enumerate(sums):                    

                    cur_sum += sm

                    idx = bisect.bisect_left(temp, cur_sum - k)
                    
                    if idx == len(temp):
                        range_sum = cur_sum
                    else:
                        range_sum = cur_sum - temp[idx]
                   
                    if range_sum == k:
                        return k
                    
                    if res < range_sum < k:
                        res = range_sum
                    bisect.insort(temp, cur_sum)

        return res