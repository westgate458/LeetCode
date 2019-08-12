# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 23:21:45 2019

@author: Tianqi Guo
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        
        # Solution 1: O(1) space
        l = len(nums) 
        ans = [1] * l            
        for i in range(1, l):
            ans[i] = ans[i-1] * nums[i-1]      
        r = 1
        for i in range(l-2, -1, -1):
            r *= nums[i+1]
            ans[i] *= r
        return ans
        
        # Solution 2: O(n) space
        pre, aft, l = [1], [1], len(nums)        
        for i in range(l-1):
            pre.append(pre[-1]*nums[i])
            aft.append(aft[-1]*nums[l-1-i])
        return [m*n for m,n in zip(pre,aft[::-1])]
            
            


nums = [1,2,3,4]        
test = Solution()
print(test.productExceptSelf(nums))