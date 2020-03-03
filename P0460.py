# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:28:30 2020

@author: Tianqi Guo
"""

# Solution 1 beats 100%: use heap for least used elements
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.values = {}
        self.freq_time = {}
        self.least_used = []
        self.update = set()
        self.time = 0
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """       
        self.time += 1
        if key in self.values:   
            self.update.add(key)
            self.freq_time[key] = (self.freq_time[key][0]+1, self.time)            
            return self.values[key]   
        return -1        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity <= 0: return
        self.time += 1        
        if key not in self.values:            
            if len(self.values) >= self.capacity:  
                while self.least_used and (self.least_used[0][2] in self.update):
                    _, _, k = heapq.heappop(self.least_used)
                    heapq.heappush(self.least_used, (self.freq_time[k][0], self.freq_time[k][1], k))
                    self.update.remove(k)                
                _, _, k = heapq.heappop(self.least_used)
                self.values.pop(k)
                self.freq_time.pop(k)
            self.values[key], self.freq_time[key] = value, (1, self.time)                              
            heapq.heappush(self.least_used, (1, self.time, key))
        else:            
            self.update.add(key)
            self.values[key], self.freq_time[key] = value, (self.freq_time[key][0]+1, self.time)                

# Solution 2 beats 5.05%: look for the least-used element everytime
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = {}
        self.op = 0 

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #print(self.d)
        self.op += 1
        if key not in self.d:
            return -1
        else:
            self.d[key] = [self.d[key][0], self.d[key][1]+1, self.op]
            return self.d[key][0]        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.op += 1
        if key not in self.d:
            if self.capacity > 0:
                if len(self.d) >= self.capacity:                
                    keys = self.d.keys()
                    freq = [self.d[k][1] for k in keys]
                    oprs = [self.d[k][2] for k in keys]
                    keys = sorted(zip(keys, freq, oprs),key=lambda x:(x[1],x[2]))
                    del self.d[keys[0][0]]
                self.d[key] = [value, 1, self.op]
        else:
            self.d[key] = [value, self.d[key][1]+1, self.op]



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)