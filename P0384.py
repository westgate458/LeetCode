# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:56:48 2019

@author: Tianqi Guo
"""

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.l = len(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ans = self.nums[:]
        for ll in xrange(self.l):
            ind = random.randint(0,self.l-1)
            ans[ll], ans[ind] = ans[ind], ans[ll]
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()