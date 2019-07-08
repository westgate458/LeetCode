# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:02:29 2019

@author: Tianqi Guo
"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
                   
        # Solution 1: beats 67.63%
        # number of bits from the right that the two numbers differ
        i = 0        
        # continue loop until two numbers are equal
        while m != n:            
            # shifting bits of both numbers right
            # i.e. remove the different bits
            m >>= 1
            n >>= 1
            # counting number of different bits
            i += 1                
        # the 'bitwise and' should just be the bits where two numbers are identical
        # bitwise left-shift number back to obtain the result
        return n << i
        
    
        # Solution 2: beats 99.59%
        s1, s2 = bin(m), bin(n)    
        l1, l2 = len(s1), len(s2)        
        if l2 > l1:
            return 0        
        ans = 0
        for i in xrange(l2):
            if s1[i] != s2[i]:
                break
            elif s1[i] == '1':
                ans += 2**(l2-1-i)                
        return ans


m = 4
n = 14        
test = Solution()
print test.rangeBitwiseAnd(m,n)