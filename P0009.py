# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:24:13 2018

@author: Tianqi Guo
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # negative numbers are not palindrome by def.
        if x < 0:
            return False
        # convert number to string
        s = str(x)
        l = len(s)
        # for each digit check if equal to its mirror digit
        for i in range(int(l/2)):
            # if not equal then x is not palindrome
            if s[i] != s[-i-1]:
                return False
            
        # x is palindrome after all digits checked
        return True

x = -121
test = Solution()
print(test.isPalindrome(x))