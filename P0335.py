# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:45:28 2019

@author: Tianqi Guo
"""

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) < 4:
            return False        
        l1, l2, l3, l4 = 0, x[0], x[1], x[2] 
        increasing = x[2] > x[0]       
        for i in x[3:]:         
            if increasing:
                if i > l2:
                    l1, l2, l3, l4 = l2, l3, l4, i
                else:
                    increasing = False
                    if i + l1 < l3:
                        l1, l2, l3, l4 = l2, l3, l4, i
                    else:
                        l1, l2, l3, l4 = l2, l4-l2, l4, i
            else:
                if i >= l2:
                    return True
                else:
                    l1, l2, l3, l4 = l2, l3, l4, i
        return False
            