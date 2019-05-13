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
      
        self.opCount = collections.defaultdict(int)
        self.capacity = capacity
        self.queue = collections.deque()
        self.values = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """       
        
        if key in self.values:
            
            self.queue.append(key)
            self.opCount[key] += 1
            return self.values[key]
        
        else:
            return -1   

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """  
        
        self.queue.append(key)
        self.opCount[key] += 1
        self.values[key] = value
        
        while len(self.values) > self.capacity:
            
            k = self.queue.popleft()
            self.opCount[k] -= 1
            if self.opCount[k] == 0:
                del self.opCount[k]
                del self.values[k]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
            