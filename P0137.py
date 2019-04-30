# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:57:34 2019

@author: Tianqi Guo
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Solution 1
        return (3 * sum(set(nums)) - sum(nums))//2
        
        # Solution 2
#        num_dict = {}
#        for num in nums:
#            if num in num_dict:
#                if num_dict[num] == 2:
#                    num_dict.pop(num)
#                else:
#                    num_dict[num] += 1
#            else:
#                num_dict[num] = 1
#        
#        return num_dict.keys()[0]

nums = [0,1,0,1,0,1,99]  
test = Solution()
print test.singleNumber(nums)
                
        
        