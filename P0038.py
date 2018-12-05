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
      
        ans = '1'
        for _ in range(n-1):
            temp = ''
            for digit, group in itertools.groupby(ans):
                temp = temp + str(len(list(group))) + digit
            ans = temp
            
        return(ans)
        
test = Solution()
n = 5
print(test.countAndSay(n))                 
                  
                