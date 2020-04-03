# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:48:02 2020

@author: Tianqi Guo
"""

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # deal with trivial case where the algorithm fails
        if n == 1: return 9
        # palindrome = n1 * n2 = (10**n-a)*(10**n-b) -> minimize a and b
        # palindrome = 10**n * 10**n - (a+b)* 10**n + ab
        # palindrome = (10**n - (a+b)) * 10**n + ab = L * 10**n + R
        # left bits L = 10**n - s -> s = a+b
        # rightbits R = ab = reverse(L)
        # try all possible s, starting from smallest possible s = 1 + 1 = 2
        # stop when integer a and b are found -> palindrome = L + R
        s = 2
        while True:     
            # calculate R from s
            R = int(str(10**n-s)[::-1])
            # determinant for real roots to exist
            # equation: a + b = s, ab = R ->  x^2 - sx + R = 0
            if s**2-4*R >= 0:
                # the positive root
                x = (s + (s**2-4*R)**0.5)/2
                # if x is integer, we have found n1 and n2
                # return the mod of the palindrome
                if x.is_integer(): return (10**(2*n) - s*10**n + R)%1337
            # if n1 and n2 not found, try next s
            s += 1
        