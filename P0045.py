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
        l = len(nums)
        
        if l == 1:
            return 0

        steps = nums[0]
        jumps = 1

        max_reach = steps

        for i in range(1,l-1):
            steps = steps - 1
            max_reach = max(max_reach,i+nums[i])
            if steps == 0:
                jumps = jumps + 1
                steps = max_reach - i
                
        return jumps
    
nums = [2,3,1,1,4]
test = Solution()
print(test.jump(nums))