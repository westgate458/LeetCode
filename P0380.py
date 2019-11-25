# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:12:35 2019

@author: Tianqi Guo
"""

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # list for all numbers
        self.nums = []
        # the index for each number in the list
        self.inds = {}
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # if it already exists return error
        if val in self.inds:
            return False
        # record the index and save the number
        self.inds[val] = len(self.nums)
        self.nums.append(val)            
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # if it doesn't exist return error        
        if val not in self.inds:
            return False
        # find the index for the val in list, and take the last element
        ind, temp = self.inds[val], self.nums.pop()           
        # if the one to delete is not the last number    
        if ind < len(self.nums):
            # place the last element at where the val was
            # and update the index for the last element
            self.nums[ind], self.inds[temp] = temp, ind
        # delete the index for val
        del self.inds[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # pick a random number from the list
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()