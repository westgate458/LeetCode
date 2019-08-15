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
        # number of nums
        l = len(nums) 
        # now ans[i] stores the product from nums[0] to nums[i-1]
        ans = [1] * l            
        # calculate the products from left first
        for i in range(1, l):
            ans[i] = ans[i-1] * nums[i-1]      
        # product from the right
        r = 1
        # calculate producs from the right, and update left*right
        for i in range(l-2, -1, -1):
            # producs from the right
            r *= nums[i+1]
            # product of all others except current num
            ans[i] *= r
        # return the answer list
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