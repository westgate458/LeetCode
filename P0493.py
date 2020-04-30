# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:45:47 2020

@author: Tianqi Guo
"""

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        
        # subfunction to merge two already sorted intervals
        def merge(nums):            
            # length of current interval
            l = len(nums)
            # if we only have one number
            if l == 1:
                # it is already sorted
                return nums
            else:
                # first sort two halves separately
                left, right = merge(nums[:l//2]), merge(nums[l//2:])
                # lengths of the two halves
                l1, l2 = l//2, l - l//2    
                # pointers to traverse two halves
                i = j = 0
                # for each number in right half
                # find how many numbers in first half
                # that satisfies nums[i] > 2*nums[j]
                while i < l1 and j<l2:
                    # while the inequality is not satisfied
                    # move on to next i
                    while i < l1 and left[i] <= right[j]*2: i += 1
                    # since current number in left half satisfies nums[i] > 2*nums[j]
                    # then all numbers in left half after current number also satisfy this inequality
                    # update the counts
                    self.res += l1 - i
                    # and move on to next number in right half
                    j += 1                   
                    # here i doesn't need to be set to 0
                    # since next number in right half is larger than current one
                    # first i to satisfy nums[i] > 2*nums[j] will be after current i
                # merge the two halves by sorting
                return sorted(left+right)
        # deal with trivial case
        if not nums:
            return 0
        else:
            # count of pairs
            self.res = 0
            # merge sort the array
            merge(nums)        
            return self.res