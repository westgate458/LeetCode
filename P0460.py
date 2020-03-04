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
        # save capacity
        self.capacity = capacity
        # map from key to value
        self.values = {}
        # map from key to its frequency and most recent get\put time
        self.freq_time = {}
        # heap for least used element in the form (frequence, time, key) 
        self.least_used = []
        # all elements that got updated since last time a new key was inserted
        self.update = set()
        # timer to keep track of relative operation timing
        self.time = 0
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """       
        # update timer
        self.time += 1
        # if current key exists
        if key in self.values:   
            # we record it as updated since both frequency and time will be changed
            self.update.add(key)
            # update frequency and time
            self.freq_time[key] = (self.freq_time[key][0]+1, self.time)            
            # return key value
            return self.values[key]   
        # default value if key doesn't exist
        return -1        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # deal with trivial case
        if self.capacity <= 0: return
        # update timer
        self.time += 1
        # if current key is new        
        if key not in self.values:            
            # if we have reach the capacity, we need to get rid of one least-used key
            if len(self.values) >= self.capacity:  
                # from the heap, we check the top element (previously least used)
                # see if it got updated since last new key was inserted
                while self.least_used and (self.least_used[0][2] in self.update):
                    # first identify which key is at top
                    _, _, k = heapq.heappop(self.least_used)
                    # then we retrieve its updated frequency and time from the dictionary 
                    # and push it back into the heap
                    heapq.heappush(self.least_used, (self.freq_time[k][0], self.freq_time[k][1], k))
                    # already updated, remove it from the list
                    self.update.remove(k)                
                # now the top element in the heap was not updated since last time a new key was inserted
                # so it is the current least used element, we remove it from heap and keep its key
                _, _, k = heapq.heappop(self.least_used)
                # we discard it from the value and frequent-time dictionaries
                self.values.pop(k)
                self.freq_time.pop(k)
            # we insert the new key into both dictionaries, with frequency 1 and current operation time
            self.values[key], self.freq_time[key] = value, (1, self.time)                              
            # push this key into the heap as well
            heapq.heappush(self.least_used, (1, self.time, key))
        # if current key was an old one
        else:            
            # we add it to the updated list
            self.update.add(key)
            # also udpate its value and frequency-time accordingly
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