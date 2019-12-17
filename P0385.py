#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:25:06 2019

@author: Tianqi Guo
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

# Solution 1 beats 81.53%: isinstance and eval
class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        # subfunction to parse each nested list
        def parser(l):
            # if current list is just one number
            if isinstance(l,int):
                # place it in a nested list container and return it
                return NestedInteger(l)
            # now it should be a list
            # initialize an empty container
            nl = NestedInteger()
            # deal with each element in this list
            for elem in l:
                # add the converted lists or numbers to the container
                nl.add(parser(elem))
            # return the converted lists at this level
            return nl
        # first eval all strings to convert them to numbers
        # but preserving the nest hierarchies
        return parser(eval(s))
                    
# Solution 2 beats 91.08%: all manual             
    class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        s = s+']'
        def DFS(i):
            num = ''
            l = NestedInteger()
            while True:
                if s[i] in '-0123456789':
                    num += s[i]
                elif s[i] == '[':
                    ll,i = DFS(i+1)
                    l.add(ll)
                else:
                    if num:
                        l.add(NestedInteger(int(num)))
                    if s[i] == ']':
                        return l, i
                    num = ''
                i += 1
        ans, _ = DFS(0)
        return ans.getList()[0]    
        
        
        
        