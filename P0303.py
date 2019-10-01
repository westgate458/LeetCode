# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:09:09 2019

@author: Tianqi Guo
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # length of list
        l = len(nums)
        # accumulative sum
        self.temp = [0] * (l+1)        
        # calculate the accumulative, self.temp[i] contains sum of numbers from 0 to i-1
        for i in xrange(1,l+1):
            self.temp[i] = self.temp[i-1] + nums[i-1]        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # sum of the range is simply the difference of the two accumulative sums
        return self.temp[j+1] - self.temp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)