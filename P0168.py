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
        # all characters and the empty answer string
        chars, ans = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ', ''        
        # continue until remaining number is 0
        while n:            
            # calculate current digit
            digit = n%26
            # if current digit is 0            
            if digit == 0:
                # since there is no 0 in Excel column titles
                # it is instead labeled by Z
                digit = 26                  
            # update remaining number after current digit
            n = (n - digit)//26
            # update column title string with current digit
            ans = chars[digit] + ans
        # return the final column title
        return ans  
            
test = Solution()
print test.convertToTitle(703)