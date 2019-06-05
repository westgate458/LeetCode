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
        
        l = len(numbers)
        
        for i in xrange(l):
            num1 = numbers[i]
            num2 = target - num1
            print num1
            
            h, t = i + 1, l
            while h < t :
                
                m = (h+t)//2
                print h,m,t
                if numbers[m] == num2:
                    return [i+1,m+1]
                if numbers[m] > num2:
                    t = m - 1
                else:
                    h = m + 1



numbers = [5,25,75]
target = 100         

numbers = [2,7,11,15]
target = 9         
test = Solution()
print test.twoSum(numbers, target)
                
            
            