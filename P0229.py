# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:16:05 2019

@author: Tianqi Guo
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Boyer–Moore majority vote algorithm
        # two majority numbers with their counters
        maj1, maj2 = None, None    
        counter1, counter2 = 0, 0
        
        # go through all numbers and do the voting
        for num in nums:            
            # if current number is one of the the two majority numbers
            # increase their counters
            if num == maj1:
                counter1 += 1
            elif num == maj2:
                counter2 += 1
            # if one of the counter is zero
            # set new majority candidate
            elif counter1 == 0:
                maj1 = num
                counter1 = 1
            elif counter2 == 0:
                maj2 = num
                counter2 = 1
            # if current number is not one of the candidates
            else:
                # decrease the counters for both by 1
                counter1 -= 1
                counter2 -= 1          
        # return the majority candidate if it occurs more than n/3 times
        return [num for num in (maj1,maj2) if nums.count(num) > (len(nums) / 3.0)]
        
nums = [3,2,3]
nums = [1,1,1,3,3,2,2,2]
nums = [6,6,6,7,7]
nums = [8,8,7,7,7]
nums = [1,2,2,3,2,1,1,3]

test = Solution()
print(test.majorityElement(nums))
                