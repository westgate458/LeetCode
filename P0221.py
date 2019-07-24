# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:14:11 2019

@author: Tianqi Guo
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
              
        n = len(matrix[0])        
        
        areas = [0]* (n+1)
        l_max = 0

        for row in matrix:
            areas = [areas[i] + 1 if row[i] == '1' else 0 for i in range(n)] + [0]             
            ps = [-1]            
            for p in range(n+1):                
                while areas[p] < areas[ps[-1]]:
                    pp = ps.pop()    
                    l_max = max(l_max, min(p - ps[-1] - 1, areas[pp]))            
                ps.append(p)
       
        return l_max * l_max