# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:01:35 2018

@author: Tianqi Guo
"""
import itertools

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        # first element
        ans = '1'
        # count and say one by one
        for _ in range(n-1):
            # temperary answer string for current n
            temp = ''
            # itertools.groupby(s) returns the characters and its repetition in string s
            for digit, group in itertools.groupby(ans):
                # construct answer string by adding repetition and the corresponding digit
                # len(list(group)) gives the repetition
                temp = temp + str(len(list(group))) + digit
            # update the answer string
            ans = temp
        # return the count and say for current n
        return(ans)
        
test = Solution()
n = 5
print(test.countAndSay(n))                 
                  
                