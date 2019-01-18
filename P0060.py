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
        nums = range(1,n+1)
        permutation = ''

        k = k - 1
        while n > 0:
            n = n - 1
            index, k = divmod(k,math.factorial(n))
            permutation = permutation + str(nums[index])
            nums.pop(index)

        return permutation


n = 4
k = 9

test = Solution()
print test.getPermutation(n,k)


