# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:06:04 2019

@author: Tianqi Guo
"""

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # adaptation from P0315
        
        # sub-function that merge sort sums array in the range (i,j)
        # and count for each sum[m] in first half
        # what is the range in the second half for sum[n]
        # that satisfies the lower and upper bound of sums
        # i.e. summation from m to n is lower <= sums[n] - sums[m] <= upper
        def merge(i, j):            
            # if we have reached a single number
            if i >= j:
                # there is no range that satisfies the limits
                return 0            
            # take the mid
            m = (i + j)//2
            # first sort the two halves
            # and get the number of ranges that satisfy the limits in each half
            ans = merge(i, m) + merge(m+1, j)            
            # then we deal with the two halves at current level
            # k1 and k2 corresponds to the range for lower <= sums[n] - sums[m] <= upper
            # start from the first number in second half
            k1 = k2 = m + 1
            # for each number in first half, find its range in second half
            for sum_i in sums[i:m+1]:             
                # moving k1 until we meet the lower limit
                while k1 <= j and sums[k1] - sum_i < lower:                    
                    k1 += 1                
                # moving k2 until we meet the upper limit
                while k2 <= j and sums[k2] - sum_i <= upper:                                
                    k2 += 1             
                # all sums in the range [k1, k2] satisfy the limits
                # update ans
                ans += k2 - k1 
                # here we do not need to restart k1, k2 from m + 1
                # since both halves are sorted, k1 and k2 for new num are definitely after current ones
            # then we sort two halves altogether
            sums[i:j+1] = sorted(sums[i:j+1])
            return ans
        
        l = len(nums)
        # first we obtain the accumulative sums
        # then summation from nums[i] to nums[j] is just sums[j] - sums[i]
        sums = [0] * (l+1)        
        for i in xrange(1,l+1):
            sums[i] = sums[i-1] + nums[i-1]   
        # merge sort the whole accumulative sum array
        return merge(0, l)
                    
                    