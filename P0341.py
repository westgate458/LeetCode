# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:35:13 2019

@author: Tianqi Guo
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# Solution 1 beats 50.43%: generator-yield-next
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """   
        # cache for next value
        self.value = None
        # DFS function to flatten each nested list
        def gen(nl):
            # check each element in current nested list
            for x in nl:
                # if this element is an integer
                if x.isInteger():
                    # pause DFS and return this value
                    yield x.getInteger()
                # if this element is another nested list
                else:
                    # continue DFS
                    for y in gen(x.getList()):
                        # pause DFS when a new value is returned
                        yield y
        # the generator
        self.gen = gen(nestedList)

    def next(self):
        """
        :rtype: int
        """
        # if we have not cached next value
        if self.value == None:
            # use next to continue DFS in the generator function
            self.value = next(self.gen)
        # return the cached value
        return self.value         

    def hasNext(self):
        """
        :rtype: bool
        """
        # try to cache next value in the generator
        try:
            # cache next value
            self.value = next(self.gen)
            # return there is a next value
            return True
        # if error occurs
        except:
            # there is no next value
            return False


## Solution 2 beats 50.43%: naive DFS stack
#class NestedIterator(object):
#
#    def __init__(self, nestedList):
#        """
#        Initialize your data structure here.
#        :type nestedList: List[NestedInteger]
#        """             
#        if not nestedList:
#            self.s = []
#        else:
#            self.s = [nestedList]
#            self.p = [0]  
#            while self.s and not self.s[-1][self.p[-1]].isInteger():
#                next_list = self.s[-1][self.p[-1]].getList()
#                self.p[-1] += 1                
#                self.s.append(next_list)                    
#                self.p.append(0)  
#                while self.s and (self.p[-1] == len(self.s[-1])):
#                    self.s.pop()
#                    self.p.pop()    
#    def next(self):
#        """
#        :rtype: int
#        """        
#        current_obj = self.s[-1][self.p[-1]]
#        value = current_obj.getInteger()        
#        self.p[-1] += 1        
#        while self.s and (self.p[-1] == len(self.s[-1])):
#            self.s.pop()
#            self.p.pop()          
#        while self.s and not self.s[-1][self.p[-1]].isInteger():
#            next_list = self.s[-1][self.p[-1]].getList()
#            self.p[-1] += 1                
#            self.s.append(next_list)                    
#            self.p.append(0)  
#            while self.s and (self.p[-1] == len(self.s[-1])):
#                self.s.pop()
#                self.p.pop()             
#        return value
#    def hasNext(self):
#        """
#        :rtype: bool
#        """
#        return self.s != []

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())