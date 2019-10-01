# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:04:53 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # sub function to check each digit
        def DFS(a, b, s):
            # a, b: revious two numbers
            # s: remaining digits
            
            # n: current number formed by remaining digits
            # l: number of remaining digits
            n, l = 0, len(s) - 1
            # check each remaining digit
            for i, c in enumerate(s):
                # add current digit to current number
                n = n * 10 + int(c) 
                # if current number is the first two numbers
                if a == None or b == None:
                    # if we have reached the end but only got two numbers
                    if i == l: 
                        # it is not a valid combination
                        return False
                    # if we have more digits to cover
                    # continue DFS and check if the remaining digits are valid
                    elif DFS(b, n, s[i+1:]):
                        # as long as one valid combo is found, return True
                        return True
                # if current number is at least the third one
                # and valid addition is found
                elif a + b == n:             
                    # if we have reached the end
                    if i == l: 
                        # then the entire string is valid addition
                        return True
                    # if we have more digits to cover
                    # continue DFS and check if the remaining digits are valid
                    elif DFS(b, n, s[i+1:]):
                        # as long as one valid combo is found, return True
                        return True
                
                # deal with the special case where leading zero is not valid
                if s[0] == '0':
                    # do not need to add next digit to current number, we terminate loop
                    break
        # start DFS from the first digit with no previous numbers
        return DFS(None, None, num)