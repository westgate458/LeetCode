# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:32:51 2019

@author: Tianqi Guo
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """     
        
        # head pointer: before which lies all found 0's
        h = 0
        # tail pointer: after which lies all found 2's
        t = len(nums)-1
        # tranverse pointer
        p = 0
        
        # continue tranverse until pointer meets tail
        while p <= t:       
            
            # if current number is 2
            if nums[p] == 2:
                # switch with tail
                nums[p], nums[t] = nums[t], nums[p]    
                # update tail
                t = t - 1
                # the pointer is not updated here
                # since the tail switched here need to be checked if it is 0
                
            # if current number is 0
            elif nums[p] == 0:
                # switch with head
                nums[p], nums[h] = nums[h], nums[p]  
                # update head
                h = h + 1
                # move on to next element
                # the head switched to current position is guaranteed not 2
                # since all proceeding 2 have already been switched to tail
                # before tranverse pointer gets to current position
                p = p + 1
            
            # if current number is 1
            else:
                # no need to switch, move on to next element
                p = p + 1
        
        # return the sorted list
        return
    
nums = [2,0,2,1,1,0]
test = Solution()
test.sortColors(nums)  
print nums
    
