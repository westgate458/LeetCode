# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:44:23 2020

@author: Tianqi Guo
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """        
        # the stack for remaining digits
        picked = [] 
        # check each digit
        # we add an extra '0' to remove large digits at the end
        for n in num+'0':
            # greedy rule:
            # if previous digit in the stack is larger than current one
            # and we have not removed k digits yet
            # then we remove previous digit            
            while picked and n < picked[-1] and k:
                picked.pop()
                k -= 1
            # we put current digit in the place, resulting number is smaller
            picked.append(n)        
        # remove the additional '0' at the end
        picked.pop()            
        # remove leading 0's
        while picked and picked[0] == '0':
            del picked[0]
        # the smallest numebr after removing digits
        return ''.join(picked) if picked else '0'   