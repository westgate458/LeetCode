# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:14:37 2018

@author: Tianqi Guo
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # length of list        
        l = len(nums)
        # deal with trivial cases
        if l == 0:
            return -1
        else:
            if l == 1:
                if nums[0] == target:
                    return 0
                else:
                    return -1
        
        # find the number where the list is rotated
        # start binary searching from both ends
        h = 0
        t = l - 1        
        # continue searching until endpoints meet
        while h < t:
            # take the median
            m = (h + t)/2        
            # if median larger than its right neighbor
            # median is the rotation point
            if nums[m] > nums[m+1]:
                break    
            # if median larger than tail
            # rotation point is after median
            if nums[m] > nums[t]:
                h = m
                continue
            # if median smaller than head
            # rotation point is before median
            if nums[m] < nums[h]:
                t = m
                continue
            
            # if head < median < tail
            # the original list is already sorted in ascending order            
            # mark rotation point as -1 so no rotation will be done
            m = - 1
            break
        
        # rotate the list so it is in ascending order        
        nums = list(nums[m+1:]+nums[:m+1])
        # keep track of the original position of each number as well
        inds = range(l)        
        inds = list(inds[m+1:]+inds[:m+1])
        
        # second binary search to locate target
        # start searching from both ends
        h = 0
        t = l - 1 
        # continue searching until endpoints meet
        while h <= t:
            # take the median
            m = (h + t)/2        
            # if median is the target
            if nums[m] == target:
                # return its original position in the rotated list
                return inds[m]
                break    
            # if median is larger than target
            if nums[m] > target:
                # target is in the 1st half
                # update tail
                t = m - 1                
                continue
            # if median is smaller than target
            if nums[m] < target:
                # target is in the 2nd half
                # update head                
                h = m + 1
                continue
        
        # if target not found, return -1
        return -1
        
#        h = 0
#        t = len(nums) - 1        
#        while h <= t:            
#            m = (h + t)/2            
#            if nums[m] == target:
#                return m 
#            if nums[h] <= nums[m]:
#                if nums[h] <= target < nums[m]:
#                    t = m - 1
#                else:
#                    h = m + 1
#            else:
#                if nums[m] < target <= nums[t]:
#                    h = m + 1
#                else:
#                    t = m - 1        
#        return -1
        
nums = [1,3,5]
target = 5

test = Solution()
print(test.search(nums,target))

  