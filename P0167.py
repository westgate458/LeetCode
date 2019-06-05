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
        d = {}        
        for i, num in enumerate(numbers):
            num2 = target - num
            if num2 in d:
                return [d[num2]+1, i+1]
            else:
                d[num] = i   

numbers = [5,25,75]
target = 100         

numbers = [2,7,11,15]
target = 9         
test = Solution()
print test.twoSum(numbers, target)
                
            
            