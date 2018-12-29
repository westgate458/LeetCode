# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 18:19:27 2018

@author: Tianqi Guo
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # length of the list
        l = len(nums)
        
        # trivial case
        if l == 1:
            return 0
        
        # steps: steps can take before making a jump
        steps = nums[0]
        # number of jumps already taken
        jumps = 1
        
        # maximum position can reach before jump
        max_reach = steps
        
        # walk through the list from beginning
        for i in range(1,l-1):
            # reduce the remaining steps by one
            steps = steps - 1
            # the maximum reachable position is now updated from the current position
            # i.e. instead of jumping to previous max_reach directly
            # we jump from previous position to current position
            # then with the same numbers of jump we can go further
            max_reach = max(max_reach,i+nums[i])
            # if the remaining steps are zero
            if steps == 0:
                # then we must jump one more time
                jumps = jumps + 1
                # and the remaining steps we can take before next jump
                # is from the current position to the maximum reachable position
                steps = max_reach - i
        
        # return how many jumps are needed
        return jumps
    
nums = [2,3,1,1,4]
test = Solution()
print(test.jump(nums))