# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 19:57:42 2019

@author: Tianqi Guo
"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # use list to represent the queue
        self.q = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # place at the end of list
        self.q.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # pop the earliest number
        return self.q.pop(0)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # check the value of the earliest number
        return self.q[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # check if queue is empty
        return self.q == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()