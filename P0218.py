# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:20:39 2019

@author: Tianqi Guo
"""

class Solution(object):
    
    def merge(self, Skylines):
            
        l = len(Skylines)            
        
        if l == 1:
            return Skylines[0]
        else:                
            Skyline1 = self.merge(Skylines[:l/2])
            Skyline2 = self.merge(Skylines[l/2:])    
            
        i = j = 0 
        h1 = h2 = 0            
        result = [(0,0)]    
        l1, l2 = len(Skyline1), len(Skyline2)
            
        while i < l1  and j < l2:          
                
            if Skyline1[i][0] < Skyline2[j][0]:                
                x = Skyline1[i][0]
                h1 = Skyline1[i][1]  
                i += 1
               
            elif Skyline1[i][0] > Skyline2[j][0]:                
                x = Skyline2[j][0]
                h2 = Skyline2[j][1]                         
                j += 1
                    
            else:                
                x = Skyline1[i][0]    
                h1 = Skyline1[i][1]  
                h2 = Skyline2[j][1]          
                i += 1
                j += 1
            
            h_now = max(h1, h2)  
            if h_now != result[-1][1]:
                result.append((x, h_now))                     
                        
        if i < l1:
            result = result + Skyline1[i:] 
        elif j < l2:
            result = result + Skyline2[j:] 
                
        return result[1:]    
        
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """    
        
        if not buildings:
            return []
            
        Skylines = [[(building[0], building[2]), (building[1], 0)] for building in buildings]       
        
        return self.merge(Skylines)
            
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]       
buildings = [[1,2,1],[1,2,2],[1,2,3]] 
test = Solution()
print test.getSkyline(buildings)