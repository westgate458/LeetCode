# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:19:11 2019

@author: Tianqi Guo
"""

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1 beats 71.03%: greedy
        # deal with trivial case
        if not nums:
            return 0        
        # longest lengths for first difference positive or negative
        p = q = 1
        # check each number
        for i in xrange(1,len(nums)):
            # simply switching between the two sequences
            # based on the greedy idea:
            # if current difference is positive
            # then append this to previous longest sequence with negative difference
            if nums[i] > nums[i-1]:
                p = q + 1
            # similar for the other sequence
            elif nums[i] < nums[i-1]:
                q = p + 1
        # choose the longer one
        return(max(q,p))
        
        # Solution 2 beats 5.52%: DP
        if not nums:
            return 0
        l = len(nums)
        dp_1, dp_2 = [1] * l, [1] * l
        for i in xrange(l):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    if dp_1[j]%2 == 1:
                        dp_1[i] = max(dp_1[i], dp_1[j]+1)
                    if dp_2[j]%2 == 0:
                        dp_2[i] = max(dp_2[i], dp_2[j]+1)
                elif nums[i] < nums[j]:
                    if dp_1[j]%2 == 0:
                        dp_1[i] = max(dp_1[i], dp_1[j]+1)
                    if dp_2[j]%2 == 1:
                        dp_2[i] = max(dp_2[i], dp_2[j]+1)        
        return max(dp_1+dp_2)