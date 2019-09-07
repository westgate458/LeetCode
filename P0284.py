# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:08:10 2019

@author: Tianqi Guo
"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        if self.iterator.hasNext():
            self.cache_next = self.iterator.next()
        else:
            self.cache_next = None          
            
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """ 
        return self.cache_next
    

    def next(self):
        """
        :rtype: int
        """       
        temp = self.cache_next            
        if self.iterator.hasNext():
            self.cache_next = self.iterator.next()
        else:
            self.cache_next = None  
        return temp
        

    def hasNext(self):
        """
        :rtype: bool
        """        
        return self.cache_next != None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].