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
        
        # Solution 1: quick select beats 67.65%
        # subfunction does quick selection of the k-th largest element in the range (left, right)
        def quickSelect(nums, left, right, k):
            # if current invertal only has one element            
            if left == right:
                # select this element
                return nums[left]
            # choose the middle point as the pivot for partition
            pivotIdx = (left + right)//2        
            # value of the pivot point
            pivotVal = nums[pivotIdx] 
            # place pivot point at the end for now
            nums[pivotIdx], nums[right] = nums[right], nums[pivotIdx]            
            # index of the already sorted sub-array (from left to storeIdx)
            # all element larger than the pivot value will be placed before this pointer
            storeIdx = left   
            # for each element in current interval
            for i in range(left,right):
                # if current value is larger than the pivot value
                if nums[i] > pivotVal:
                    # swap it with the next element at the front
                    nums[storeIdx], nums[i] = nums[i], nums[storeIdx]
                    # and move storeIdx towards right
                    storeIdx += 1
            # swap the pivot element back
            # so (left, storeIdx) has all elements no less than pivot value
            nums[storeIdx], nums[right] = nums[right], nums[storeIdx]   
            # if we are selecting this k-th (storeIdx-th) largest value
            if k == storeIdx:
                # return its value
                return nums[k]
            # if what we are selecting is smaller than current storeIdx
            elif k < storeIdx:
                # search the first half
                return quickSelect(nums, left, storeIdx-1, k)
            # if what we are selecting is larger than current storeIdx
            else:
                # search the second half
                return quickSelect(nums, storeIdx+1, right, k)
        
        # start quick select in the whole range
        return quickSelect(nums, 0, len(nums)-1, k-1)
        
        # Solution 2: cheat by sorting beats 92.07%
        return sorted(nums)[-k]
    
nums = [3,2,1,5,6,4] 
k = 2    
test = Solution()
print(test.findKthLargest(nums, k))