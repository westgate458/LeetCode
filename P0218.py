# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:20:39 2019

@author: Tianqi Guo
"""

class Solution(object):
    
    # sub function for divide-and-conquer merging
    def merge(self, Skylines):
            
        # number of buildings in the Skyline list
        l = len(Skylines)            
        
        # if there is only one
        if l == 1:
            # no need to merge
            return Skylines[0]
        # if there is more than one
        else:                
            # merge the first and second halves separately
            Skyline1 = self.merge(Skylines[:l/2])
            Skyline2 = self.merge(Skylines[l/2:])    
        
        # pointers for buildings in two skylines
        i = j = 0 
        # current heights for two skylines
        h1 = h2 = 0    
        # result for the merged skyline        
        result = [(0,0)]    
        # length of two skylines
        l1, l2 = len(Skyline1), len(Skyline2)
        
        # continue scanning from left to right
        # until one of the skyline has been fully merged into result
        while i < l1  and j < l2:          
                
            # check for next elements in two skylines
            # which one comes first
            # if building in first skyline comes first
            if Skyline1[i][0] < Skyline2[j][0]:                
                # next building in the result is from 1st skyline
                x = Skyline1[i][0]
                # update current height of skyline 1
                h1 = Skyline1[i][1]  
                # move on to next building
                i += 1
            
            # similar operations for 2nd skyline
            elif Skyline1[i][0] > Skyline2[j][0]:                
                x = Skyline2[j][0]
                h2 = Skyline2[j][1]                         
                j += 1
            
            # if next buildings from two skylines start at the same position
            else:                                
                x = Skyline1[i][0]
                # update both heights    
                h1 = Skyline1[i][1]  
                h2 = Skyline2[j][1]          
                # both move on
                i += 1
                j += 1
            
            # the height in the merged result
            # is the higher one between the two current heights
            h_now = max(h1, h2)  
            # to avoid no consecutive horizontal lines of equal height
            # only add new lines to merged result when current height is different from previous one
            if h_now != result[-1][1]:
                # add new line to merged result
                result.append((x, h_now))                     
        
        # if either skyline has buildings that are not merged into results yet
        # directly copy them into the results
        if i < l1:
            result = result + Skyline1[i:] 
        elif j < l2:
            result = result + Skyline2[j:] 
        
        # return the merged results
        return result[1:]    
        
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """    
        # deal with trivial case
        if not buildings:
            return []
        # convert input to output format, each building is now a horizontal line    
        Skylines = [[(building[0], building[2]), (building[1], 0)] for building in buildings]       
        # start merging from the entire building set
        return self.merge(Skylines)
            
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]       
buildings = [[1,2,1],[1,2,2],[1,2,3]] 
test = Solution()
print test.getSkyline(buildings)