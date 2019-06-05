# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:40:45 2019

@author: Tianqi Guo
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """        
        chars, ans = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ', ''        
        while n:            
            digit = n%26
            if digit == 0:
                digit = 26                  
            n = (n - digit)//26
            ans = chars[digit] + ans
        return ans  
            
test = Solution()
print test.convertToTitle(703)