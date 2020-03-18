# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:11:38 2020

@author: Tianqi Guo
"""

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """       
        # Solution 1 beats 90.65%: form a 7x7 array and map back to 1-10
        n = 40
        # continue construct the number until it can be mapped to 1-10
        # number = row*7 + column
        while n >= 40: n = (rand7()-1)*7+rand7()-1
        # when it is in the range of [0,39], each number has equal probability
        # map it to [1, 10], and each number has equal probability still
        return n//4+1
    
        # Solution 2 beats 22.90%: generate two numbers, one is 1 out of 5, the other 1 out of 2
        a, b = rand7(), rand7()
        if a <= 5:
            while b > 2: b = rand7()                    
            if b == 1: return a
            else: return a+5
        else:
            while b > 5: b = rand7()                    
            if a == 6: return b
            else: return b+5      