# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:26:34 2019

@author: Tianqi Guo
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # pointers of the head and tail for the seaching segment
        h = 0
        t = len(nums) - 1
        
        # continue searching while the head and tail have not met
        while h <= t:
            
            # the midpoint of the segment
            m = (h + t)/2
            
            # if the target has been found
            if nums[m] == target:
                # return it exists
                return True
            
            # deal with duplicates
            # move head\tail closer to the midpoint
            # while it equals the midpoint value
            while (h < m) and (nums[h] == nums[m]):
                h = h + 1
            while (m < t) and (nums[t] == nums[m]):
                t = t - 1
            
            # if the head smaller than midpoint
            # it means the first half is in sorted order
            if nums[h] <= nums[m]:
                # if the target is within the first half
                if nums[h] <= target < nums[m]:
                    # make the first half as the new searching segment
                    t = m - 1                
                else:
                    # make the second half as the new searching segment
                    h = m + 1
            # if the second half is in sorted order
            else:
                # if the target is within the second half
                if nums[m] < target <= nums[t]:
                    # make the second half as the new searching segment
                    h = m + 1                
                else:
                    # make the first half as the new searching segment
                    t = m - 1
        
        # if the target has not been found
        return False                        
        
nums = [1,1,2,1]
target = 2

test = Solution()
print(test.search(nums,target))