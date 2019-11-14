# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:10:43 2019

@author: westg
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Solution 1 beats 98.98%: dp + dictionary
        # initial set is empty
        dp = {-1:set()}        
        # first sort the numbers
        # then check each number
        for x in sorted(nums):
            # among all previous numbers that current number is divisible by
            # find the one with the largest subset 
            dp[x] = max([dp[y] for y in dp if x%y == 0], key=len) | set([x])        
        # find the number with the largest subset
        return max(dp.values(), key=len)
            
#        # Solution 2 beats 88.52%: naive dp
#        if not nums:
#            return []
#        
#        l = len(nums)
#        dp, ps = [1] * l, [-1] * l         
#        nums.sort()        
#        for i in xrange(l-1):
#            for j in xrange(i+1,l):
#                if (nums[j] % nums[i] == 0) and (dp[i]+1 > dp[j]):                          
#                    dp[j], ps[j] = dp[i]+1, i                         
#
#        i = dp.index(max(dp)) 
#        ans = []
#        while i != -1:
#            ans.append(nums[i])
#            i = ps[i]
#                    
#        return ans[::-1]