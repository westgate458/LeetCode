# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:46:45 2020

@author: Tianqi Guo
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """       
        # Solution 1 beats 100%: sort + DFS
        # get the sum of all numbers
        total_sum = sum(nums)
        # can be partitioned by 2 only if the total sum is even
        if total_sum%2 != 0:
            return False
        # sort the array first for later pruning
        nums.sort(reverse=True)   
        # function for the partition
        def DFS(target, nums):
            # target: remaining sum to achieve
            # nums: remaining candidate numbers
            # check each number in the candidate list
            for p, num in enumerate(nums):           
                # if current number is larger than the target
                if num > target:
                    # we can not achieve the target sum since all later numbers are even larger
                    return False
                # if we happen to get the target from current number
                elif num == target:
                    # we just got a partition
                    return True
                # if current number is smaller than target sum
                # we try add current number into partition, and try remaining smaller numbers
                elif DFS(target-num, nums[p+1:]):
                    # if we get a partition in deeper search
                    return True
                # if later search didn't yield desired partition when current number is used
                # we do nothing and do not use current number in the partition
                # and move on to consider later numbers 
        # we start search by setting target to be half of the total sum
        # and use all numbers as candidates
        return DFS(total_sum//2, nums)
    
        # Solution 2 beats 25.64%: naive DP
        l, total_sum = len(nums), sum(nums)                
        if total_sum%2 != 0:
            return False                
        dp = [[False] * (l+1)  for _ in xrange(total_sum+1)]        
        for idx, num in enumerate(nums):
            dp[num][idx+1] = True        
        for i in xrange(total_sum//2):
            for j in xrange(l):                
                if dp[i][j]:
                    dp[i+nums[j]][j+1] = True
                    dp[i][j+1] = True
        return(sum(dp[total_sum//2])>0)