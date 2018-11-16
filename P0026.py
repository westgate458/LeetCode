# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:01:45 2018

@author: Tianqi Guo
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # pointer to traverse the list
        p = 1
        
        # compare each element with its previous one
        while p < len(nums):
            # if current element different from previous one
            if nums[p] != nums[p-1]:                
                # continue searching
                p = p + 1               
            else:
                # remove if duplicates found
                nums.pop(p)
        
        # return list after duplicates removed
        return len(nums)
        
        
nums = [1,1]
test = Solution()
p = test.removeDuplicates(nums)
print(p)