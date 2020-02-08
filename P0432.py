# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:38:16 2020

@author: Tianqi Guo
"""

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # dictionary for all keys and counts
        self.d = {}

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        # insert key or update its count
        if key in self.d:
            self.d[key] += 1
        else:
            self.d[key] = 1
            

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        # reduce the count of the key if it exists
        if key in self.d:
            self.d[key] -= 1
            # remove the key if count drops to 0
            if self.d[key] == 0:
                del self.d[key]
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        # res: the key with the max count
        # max_v: the maximum count
        res, max_v = '', 0
        # get the max key with O(n) time
        for key in self.d:
            if self.d[key] > max_v:
                max_v, res = self.d[key], key
        return res

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        # res: the key with the min count
        # max_v: the minimum count
        res, min_v = '', float('inf')
        # get the min key with O(n) time
        for key in self.d:
            if self.d[key] < min_v:
                min_v, res = self.d[key], key
        return res


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()