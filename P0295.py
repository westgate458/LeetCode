# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:43:36 2019

@author: Tianqi Guo
"""
import heapq 
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """        
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """            
        if not self.small or num <= -self.small[0]:            
            heapq.heappush(self.small, -num)      
        else:
            heapq.heappush(self.large, num)     
        
        if len(self.large) > len(self.small):           
            heapq.heappush(self.small, -heapq.heappop(self.large))  
        elif len(self.large) < len(self.small) - 1:      
             heapq.heappush(self.large, -heapq.heappop(self.small))  
        
    def findMedian(self):
        """
        :rtype: float
        """        
        if len(self.large) == len(self.small):            
            return float((-self.small[0] + self.large[0]))/2
        else:
            return -self.small[0]    


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()