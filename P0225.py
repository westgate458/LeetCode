# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 17:32:03 2019

@author: Tianqi Guo
"""

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # use list for the stack
        self.s = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # place element at the end of the list, i.e. the top of the stack
        self.s.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # remove and return the last element of the list, i.e. from the top of the stack
        return self.s.pop(-1)
        
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        # return the last element of the list, i.e. from the top of the stack
        return self.s[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        # check if the list is empty
        return not self.s


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()