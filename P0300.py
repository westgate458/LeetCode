# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:07:53 2019

@author: Tianqi Guo
"""
import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1 beats 98.22%: dynamic programing + binary search     
        # dp is the list of increasing numbers currently found
        dp = []
        # check each number
        for num in nums:
            # using binary search, find its insertion place in the dp array
            idx = bisect.bisect_left(dp, num)
            # if it needs to be inserted at the end of the list
            # i.e. it is larger than all numbers in LIS
            if idx == len(dp):
                # then the number of LIS increases by 1
                dp.append(num)
            # if it will replace one number in LIS
            else:
                # if a longer LIS is to be found later, because current number is smaller
                # then it will be better to have current number than previous dp[idx]
                # at idx position in LIS
                dp[idx] = num
        # return the length of the LIS
        # however, now dp is not necessarily the longest LIS found
        return len(dp)
        
        # Solution 2 beats 62.61%: dynamic programing
        if not nums:
            return 0
        ls = [1] * len(nums)
        for i, n1 in enumerate(nums):            
            for j, n2 in enumerate(nums[:i]):
                if n2 < n1 and ls[j] + 1 > ls[i]:
                    ls[i] = ls[j] + 1           
        return max(ls)
                
                
        