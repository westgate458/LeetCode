# -*- coding: utf-8 -*-
"""
Created on Sun May 12 22:31:08 2019

@author: Tianqi Guo
"""
import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """                
        # number of operations for each key
        self.opCount = collections.defaultdict(int)
        # capacity of the cache
        self.capacity = capacity
        # operation sequence already seen
        self.queue = collections.deque()
        # value for each key
        self.values = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """              
        # if key exists
        if key in self.values:
            # keep record of the operation in order
            self.queue.append(key)
            # update number of operations for current key
            self.opCount[key] += 1
            # return key value
            return self.values[key]
        # if key doesn't exist
        else:
            # return not found
            return -1   

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """  
        # keep record of the operation in order
        self.queue.append(key)
        # update number of operations for current key
        self.opCount[key] += 1
        # record value for current key
        self.values[key] = value        
        # remove least recently used key from cache
        while len(self.values) > self.capacity:
            # retrieve earliest key currently in the operation sequence
            k = self.queue.popleft()
            # reduce its operation counts by 1
            self.opCount[k] -= 1
            # if remaining operation counts is zero
            # i.e. this key has not beed accessed thereafter
            if self.opCount[k] == 0:
                # this key is the least recently used key currently in cache
                # remove it from cache (both its operation counts and its value)
                del self.opCount[k]
                del self.values[k]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
            