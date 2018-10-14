# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:24:13 2018

@author: Tianqi Guo
"""
def isPalindrome(x):
    
    if x < 0:
        return False
    
    s = str(x)
    l = len(s)
    
    for i in range(int(l/2)):
        if s[i] != s[-i-1]:
            return False
    
    return True

x = -121
print(isPalindrome(x))