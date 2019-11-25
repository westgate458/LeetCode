# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 22:04:48 2019

@author: Tianqi Guo
"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        # Solution 1 beats 99.56%: binary search
        # current range [l,r], size of matrix
        l, r, n = matrix[0][0], matrix[-1][-1], len(matrix)        
        # stop when ends meet
        while l < r:         
            # current guess is the middle in the range
            # i, j start from the bottom-left, sweep through the matrix
            # row by row and column by column to count number of elements smaller than m
            m, i, j, c = (l+r)//2, n-1, 0, 0            
            # stop counting when get to the first row or last column
            while i >= 0 and j < n:                
                # if current number is smaller than m
                if matrix[i][j] <= m:
                    # then all previous number in current column is smaller than m
                    # update count
                    c += i+1
                    # move on to the element in the next column
                    # which is larger than current element
                    j += 1                    
                # if current number is no smaller than m
                else:
                    # move on the the element above, which is smaller than current element
                    i -= 1 
            # if number of elements smaller than m is smaller than k
            if c < k:
                # then next guess needs to be larger
                l = m + 1
            # or next guess needs to be smaller
            else:
                r = m
        # the left element is the corrent guess
        # for the k-th Smallest Element in a Sorted Matrix
        return l
        
        # Solution 2 beats 74.40%: 1-liner
        return sorted(n for a in matrix for n in a)[k-1]