# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:28:51 2019

@author: Tianqi Guo
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
        # Solution 1: max-min beats 96.12%
        l1 = max(0, min(D, H) - max(B, F))
        l2 = max(0, min(C, G) - max(A, E))               
        return (C-A)*(D-B) + (G-E)*(H-F) - l1 * l2
        
        # Solution 2: if-else beats 59.79%
        def computeLength(x11, x12, x21, x22):
            if x12 <= x21 or x11 >= x22:
                return 0            
            if x11 <= x21:
                if x12 <= x22:
                    return x12 - x21
                else:
                    return x22 - x21
            else:
                if x12 <= x22:
                    return x12 - x11
                else:
                    return x22 - x11         
        return (C-A)*(D-B) + (G-E)*(H-F) - computeLength(A, C, E, G) * computeLength(B, D, F, H)

A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 2    
test = Solution()
print(test.computeArea(A, B, C, D, E, F, G, H))
            