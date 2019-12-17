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
        # record the original numbers and the length of the list
        self.nums = nums
        self.l = len(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        # resetting is just taking the original numbers
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # make a copy of the original numbers
        ans = self.nums[:]
        # for each sublist in the list
        for ll in xrange(self.l):
            # randomly choose one number in the sublist
            ind = random.randint(0,self.l-1)
            # and swap it with the last number in the sublist
            ans[ll], ans[ind] = ans[ind], ans[ll]
        # a randomly shuffled list is formed, somehow
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()