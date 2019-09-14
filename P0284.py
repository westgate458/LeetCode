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
        # pointer to the iterator
        self.iterator = iterator
        # if iterator is not empty
        if self.iterator.hasNext():
            # cache the next number
            self.cache_next = self.iterator.next()
        # if we got an empty iterator
        else:
            # cache None to indicate tail
            self.cache_next = None          
            
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """ 
        # peek is now looking at the cached value
        return self.cache_next
    

    def next(self):
        """
        :rtype: int
        """       
        # record current cached value
        temp = self.cache_next       
        # advance iterator and cache next value
        if self.iterator.hasNext():
            self.cache_next = self.iterator.next()
        else:
            self.cache_next = None  
        # return previously cached value, which is the 'next'
        return temp
        

    def hasNext(self):
        """
        :rtype: bool
        """        
        # iterator has next if cached value is not none
        return self.cache_next != None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].