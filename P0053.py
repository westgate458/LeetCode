# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:50:27 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """     
        
        # Solution 1: divide and conquer
        # find maximum of each segment and merge from bottom up
        def max_sum(l,r):
            
            # if only one number in current segment
            if l == r:
                # max sum is the number itself
                return nums[l]
            
            # mid point of the segment
            m = (l + r)/2
            
            # find the max sum of the left and right segments
            # not neccesarily including the midpoint
            sum1 = max_sum(l, m)
            sum2 = max_sum(m+1, r)
            
            # find the left segment of max sum including the mid point
            sm_l = 0
            sm_max_l = -float('Inf')
            # start from mid point towards left
            for i in range(m,l-1,-1):
                # calculate accumulative sum and update the max sum
                sm_l = sm_l + nums[i]
                if sm_l > sm_max_l:
                    sm_max_l = sm_l
            # find the right segment of max sum including the mid point
            sm_r = 0
            sm_max_r = -float('Inf')
            # start from mid point towards right
            for i in range(m+1,r+1,1):
                # calculate accumulative sum and update the max sum
                sm_r = sm_r + nums[i]
                if sm_r > sm_max_r:
                    sm_max_r = sm_r
            
            # max sum that must include the midpoint
            sum3 = sm_max_l + sm_max_r
            
            # max sum of the current segment is the largest among the three
            return max(sum1,sum2,sum3)      
        
        # call sub function with the entire segment
        maxsum = max_sum(0,len(nums)-1)
        
        # Solution 2: Greedy approach
        # initialize max sum as the first number
        maxsum = nums[0]
        # initialize accumulative sum as 0
        sm = 0
        
        # calculate accumulative sum from left to right
        for num in nums:
            # update accumulative sum 
            sm = sm + num
            # update max sum
            if sm > maxsum:
                maxsum = sm 
            # if current accumulative sum is negative
            if sm < 0:
                # make it 0 and restart accumulative sum from next number
                sm = 0
                
        # return the maximum contiguous sum
        return maxsum
    
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
test = Solution()
print(test.maxSubArray(nums))    