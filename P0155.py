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
        # s stores (current number, current min)
        self.s = [(None, 9999999999)]        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # push (new number, new min) into stack
        self.s.append((x, min(x,self.s[-1][1])))

    def pop(self):
        """
        :rtype: None
        """        
        # remove most recent (number, min)
        self.s.pop()
        

    def top(self):
        """
        :rtype: int
        """
        # current number from top of the stack
        return self.s[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        # current min from top of the stack
        return self.s[-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()