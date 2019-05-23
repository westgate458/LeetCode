# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:18:31 2019

@author: Tianqi Guo
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.minNum = 9999999999 

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        self.s.append((x, self.minNum))
        if x < self.minNum:
            self.minNum = x
        

    def pop(self):
        """
        :rtype: None
        """
        
        self.minNum = self.s[-1][1]
        self.s.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minNum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()