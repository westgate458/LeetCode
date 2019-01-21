# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 20:14:30 2019

@author: Tianqi Guo
"""
import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # numbers in ascending order
        nums = range(1,n+1)
        # empty permutation
        permutation = ''
        
        # reduce initial k by one such that
        # k div factorial(n) gives the right number in remaining num list
        k = k - 1
        # continue construction until all numbers are used in permutation
        while n > 0:
            # reduce remaining number
            n = n - 1
            # factorial(n) gives the total number of permutations
            # after current digit is taken
            # index gives which number in remaining num list should be used for current digit
            # k gives the remaining number of permutations until target
            index, k = divmod(k,math.factorial(n))
            # add current digit to permutation and remove if from num list
            permutation = permutation + str(nums.pop(index))            
        
        # return the target permutation
        return permutation


n = 4
k = 9

test = Solution()
print test.getPermutation(n,k)


