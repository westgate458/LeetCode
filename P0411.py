# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:30:19 2020

@author: Tianqi Guo
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for num in xrange(1,n+1):   
            s = str(num)
            if num%3==0:
                s = 'Fizz'  
            if num%5==0:
                s = 'Buzz'
            if num%15==0:
                s = 'FizzBuzz'
            res.append(s)                
        return res