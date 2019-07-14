# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:05:34 2019

@author: Tianqi Guo
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Solution 1
        def quickSelect(nums, left, right, k):            
            if left == right:
                return nums[left]
            pivotIdx = (left + right)//2            
            pivotVal = nums[pivotIdx]            
            nums[pivotIdx], nums[right] = nums[right], nums[pivotIdx]            
            storeIdx = left            
            for i in range(left,right):
                if nums[i] > pivotVal:
                    nums[storeIdx], nums[i] = nums[i], nums[storeIdx]
                    storeIdx += 1
            nums[storeIdx], nums[right] = nums[right], nums[storeIdx]         
            if k == storeIdx:
                return nums[k]
            elif k < storeIdx:
                return quickSelect(nums, left, storeIdx-1, k)
            else:
                return quickSelect(nums, storeIdx+1, right, k)
        return quickSelect(nums, 0, len(nums)-1, k-1)
        
        # Solution 2
        return sorted(nums)[-k]
nums = [3,2,1,5,6,4] 
k = 2    
test = Solution()
print(test.findKthLargest(nums, k))