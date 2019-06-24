# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 23:19:59 2019

@author: Tianqi Guo
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Solution 1
        max_pre, max_cur = 0, 0              
        for num in nums:           
            max_pre, max_cur = max_cur, max(max_pre + num, max_cur)  
        return max_cur
    
        # Solution 2
        l = len(nums)        
        rob = [0] * (l + 1)
        pas = [0] * (l + 1)        
        for i in xrange(1,l+1):           
            rob[i] = pas[i-1] + nums[i-1]
            pas[i] = max(rob[i-1], pas[i-1])            
        return max(rob[-1],pas[-1])
    
    
nums = [1000,1,1,1000]
nums = [1,2,3,1]
nums = [2,7,9,3,1]
test = Solution()
print test.rob(nums)
    