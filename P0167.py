# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:05:39 2019

@author: Tianqi Guo
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """        
        # dictionary to record the indices of encountered numbers
        d = {}        
        # check each number in the list
        for i, num in enumerate(numbers):
            # the complementary number to look for
            num2 = target - num
            # if we have already seen this number
            if num2 in d:
                # return the indices
                return [d[num2]+1, i+1]
            # if the complementary number is unseen
            else:
                # record the index of current number in the dictionary
                d[num] = i   

numbers = [5,25,75]
target = 100         

numbers = [2,7,11,15]
target = 9         
test = Solution()
print test.twoSum(numbers, target)
                
            
            