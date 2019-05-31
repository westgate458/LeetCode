# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:48:37 2019

@author: Tianqi Guo
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        # head and tail pointers for binary search
        h, t = 0, len(nums) - 1
        # continue searching until two pointers meet
        while h < t:
            # take the midpoint
            m = (h + t)//2 
            # if tail larger than mid
            if nums[t] > nums[m]:
                # 2nd half is sorted, search the 1st half
                t = m
            # if tail smaller than mid
            elif nums[t] < nums[m]:  
                # 1st half is sorted, search the 2nd half
                h = m + 1
            # if tail equal to mid
            else:
                # duplicates found, shrink searching region by 1
                t -= 1
        # head is the smallest number
        return nums[h] 

        
                
nums = [3,4,5,1,2]  
nums = [4,5,6,7,0,1,2]       
nums = [2, 1]
nums = [3, 1, 2]
nums = [2,2,2,0,1]
nums = [3,1,3]
nums = [1,2,3]


nums = [2,2,2,0,1]
nums = [1,1,3,1]
nums = [1]

test = Solution()
print test.findMin(nums)