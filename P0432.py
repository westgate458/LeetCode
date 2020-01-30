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
        self.d = {}

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
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
        if key in self.d:
            self.d[key] -= 1
            if self.d[key] == 0:
                del self.d[key]
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        res, max_v = '', 0
        for key in self.d:
            if self.d[key] > max_v:
                max_v, res = self.d[key], key
        return res

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        res, min_v = '', float('inf')
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