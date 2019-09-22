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
        # two heaps that store the smaller half and larger half
        # to make the root element the largest in the smaller heap
        # it will store the negative of actual numbers
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """            
        # if current number smaller than the root element in smaller heap
        if not self.small or num <= -self.small[0]:            
            # place the negative of its value to the smaller heap
            heapq.heappush(self.small, -num)      
        # if current number larger than the root element in smaller heap
        else:
            # place this number to the larger heap
            heapq.heappush(self.large, num)     
        
        # make sure the smaller heap has 
        # one more than or equal elements as
        # the larger heap        
        if len(self.large) > len(self.small):           
            heapq.heappush(self.small, -heapq.heappop(self.large))  
        elif len(self.large) < len(self.small) - 1:      
            heapq.heappush(self.large, -heapq.heappop(self.small))  
        
    def findMedian(self):
        """
        :rtype: float
        """        
        # if two halves have the same number of elements
        if len(self.large) == len(self.small):          
            # median is the mean of the two roots
            return float((-self.small[0] + self.large[0]))/2
        # if the smaller half has one more element than the larger heap
        else:
            # the root of the smaller heap is the median
            return -self.small[0]    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()