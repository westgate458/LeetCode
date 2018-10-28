# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:49:27 2018

@author: Tianqi Guo
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        l = len(nums)
        # sort the list in ascending order for faster searching
        nums.sort()
        # set initial answer to empty
        ans = []
        # set previous 1st number to NaN
        num_1 = float('nan')
        
        # try the first (l-3) numbers as the 1st number in summation
        # since the list is sorted, the numbers in the summation triplet
        # satisfy num_1 <= num_2 <= num_3 <= num_4
        for i in range(l-3):
            # to avoid duplicates
            # if the current number is equal to the previous 1st number
            # do not take the current number as the 1st number
            if num_1 == nums[i]:
                continue
            # take the current number as the 1st number
            num_1 = nums[i]
            # set previous 2nd number to NaN
            num_2 = float('nan')
            # try the numbers after the 1st number as the 2nd number
            for ii in range(i+1,l-2):
                # if the current number is equal to the previous 2nd number
                # do not take the current number as the 2nd number
                if num_2 == nums[ii]:
                    continue
                # take the current number as the 2nd number
                num_2 = nums[ii]
                # set searching end points
                # try taking the next number as 3rd number
                # and the last number in the list as the 4th number
                j = ii + 1
                k = l - 1
                # shrink the search range until the endpoints meet
                while j < k:
                    # take the current endpoints as the 3ed and 4th numbers
                    num_3 = nums[j]
                    num_4 = nums[k]    
                    # if the current numbers sum to target                         
                    if num_1 + num_2 + num_3 + num_4 == target:  
                        # add the current combination to the answer set
                        ans.append([num_1,num_2,num_3,num_4])  
                        # to avoid duplicates
                        # if remaining search range is not empty and
                        # the end point at front equal to previous num_3
                        # or the end point at tail equal to previous num_4
                        # update endpoints and shrink search range
                        while (j < k) and (nums[j] == num_3):
                            j = j + 1 
                        while (j < k) and (nums[k] == num_4):
                            k = k - 1
                    # if the current numbers do not sum to target   
                    # adjust endpoints accordingly
                    else:
                        # if the current sum is larger than target 
                        if num_1 + num_2 + num_3 + num_4 > target:
                            # the 4th number is too large
                            # try the smaller one before the current one
                            k = k - 1
                        # if the current sum is smaller than target 
                        else:
                            # the 3rd number is too small
                            # try the larger one after the current one
                            j = j + 1
                            
        return ans
    
nums = [1, 0, -1, 0, -2, 2]
target = 0
test = Solution()
print(test.fourSum(nums,target))   