# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:50:27 2019

@author: Administrator
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """     
        def max_sum(l,r):

            if l == r:
                return nums[l]

            m = (l + r)/2

            sum1 = max_sum(l, m)
            sum2 = max_sum(m+1, r)

            sm_l = 0
            sm_max_l = -float('Inf')
            for i in range(m,l-1,-1):
                sm_l = sm_l + nums[i]
                if sm_l > sm_max_l:
                    sm_max_l = sm_l

            sm_r = 0
            sm_max_r = -float('Inf')
            for i in range(m+1,r+1,1):
                sm_r = sm_r + nums[i]
                if sm_r > sm_max_r:
                    sm_max_r = sm_r

            sum3 = sm_max_l + sm_max_r

            return max(sum1,sum2,sum3)

        return max_sum(0,len(nums)-1)
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
test = Solution()
print(test.maxSubArray(nums))    