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
        # 2D kadane's algorithm
        
        # size of the matrix, and current max sum
        r, c, res = len(matrix), len(matrix[0]), float('-inf')
        
        # L and R: left-most and right-most of the rectangle
        for L in xrange(c):
            # current row-wise accumalative sums
            sums = [0] * r
            for R in xrange(L, c):
                # update the accumalative sums
                for rr in xrange(r):
                    sums[rr] += matrix[rr][R]                
                # cur_sum: accumulative sum from top to bottom in the sums
                # temp: accumulative sums already seen in sorted order
                cur_sum, temp = 0, [0]
                # check each accumulative sum 
                for rrr, sm in enumerate(sums):                    
                    # update accumulative sum
                    cur_sum += sm
                    # for summation in the range r1 to r2
                    # if sum_r1_to_r2 <= k
                    # then cur_sum_s2 - cur_sum_s1 <= k
                    # then cur_sum_s1 >= cur_sum_s2 - k
                    # we need to find in the sorted temp of previous cur_sums
                    # where is the smallest cur_sum larger than cur_sum - k
                    idx = bisect.bisect_left(temp, cur_sum - k)
                                        
                    # if there is no previous sum that satisfy a range sum smaller than k
                    if idx == len(temp):
                        # just try current sum
                        range_sum = cur_sum
                    # calculate the range sum
                    else:
                        range_sum = cur_sum - temp[idx]
                    
                    # if the range sum is just the target
                    if range_sum == k:
                        # we are done
                        return k
                    
                    # otherwise update the result
                    if res < range_sum < k:
                        res = range_sum
                    
                    # insert the new current sum
                    bisect.insort(temp, cur_sum)
        # return the max sum <= k
        return res