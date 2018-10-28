# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:35:22 2018

@author: Tianqi Guo
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = len(nums)
        # sort the list in ascending order for faster searching
        nums.sort()        
        # set initial closest sum to infinity
        closestSum = float('Inf')
        # set previous 1st number to NaN
        num_1 = float('nan')
        
        # try the first (l-2) numbers as the 1st number in summation
        # since the list is sorted, the numbers in the summation triplet
        # satisfy num_1 <= num_2 <= num_3
        for i in range(l-2):
            # to avoid duplicate triplets
            # if the current number is equal to the previous 1st number
            # do not take the current number as the 1st number
            if num_1 == nums[i]:
                continue
            # take the current number as the 1st number
            num_1 = nums[i]
            # set searching end points
            # try taking the next number as 2nd number
            # and the last number in the list as the 3rd number
            j = i + 1
            k = l - 1
            # shrink the search range until the endpoints meet
            while j < k:
                # take the current endpoints as the 2nd and 3rd numbers
                # and calculate the summation
                num_2 = nums[j]
                num_3 = nums[k]          
                threeSum =  num_1 + num_2 + num_3    
                # if the current summation is closer to target
                # update the closest sum
                if abs(threeSum - target) < abs(closestSum - target):
                    closestSum = threeSum
                # if the current summation is equal to target
                # return target  
                if threeSum == target:                    
                    return target
                else:
                    # if the current sum is larger than target
                    if num_1 + num_2 + num_3 > target:
                        # the 3rd number is too large
                        # try the smaller one before the current one
                        k = k - 1
                    # if the current sum is smaller than target  
                    else:
                        # the 2nd number is too small
                        # try the larger one after the current one
                        j = j + 1               
                    
        return closestSum    
    
nums = [-1, 2, 1, -4]
target = 1
test = Solution()
print(test.threeSumClosest(nums,target)) 