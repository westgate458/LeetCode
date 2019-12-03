#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:20:12 2019

@author: Tianqi Guo
"""

from random import choice
from collections import defaultdict
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # list for all numbers
        self.nums = []
        # the index for each number in the list
        self.inds = defaultdict(set)
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # record the index and save the number
        self.inds[val].add(len(self.nums))
        self.nums.append(val)            
        return len(self.inds[val]) == 1
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # if it doesn't exist return error        
        if not self.inds[val]:
            return False

        ind, temp = self.inds[val].pop(), self.nums[-1]
        self.inds[temp].add(ind)
        self.inds[temp].discard(len(self.nums)-1)
        self.nums[ind] = temp
        self.nums.pop()
      
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # pick a random number from the list
        return choice(self.nums)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()