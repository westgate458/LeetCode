# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:25:14 2019

@author: Tianqi Guo
"""
from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0 
        
        points = [(point[0],point[1]) for point in points]
        points_dict = defaultdict(int)
        for point in points:
            points_dict[point] += 1
        
        points = list(set(points))   
                
        Np = len(points)
        if Np == 1:
            return points_dict.values()[0]
        
        Np = len(points)       
        
        ans = 0
        for i in xrange(Np-1):
            ks = defaultdict(int)
            for j in xrange(i+1,Np):
                dx, dy = points[i][0] - points[j][0], points[i][1] - points[j][1]              
                if dx == 0:
                    k = None
                elif dy == 0:
                    k = 0
                else:
                    k = float(dy)/dx                
                ks[k] += points_dict[points[j]]                         
            ans = max(ans, points_dict[points[i]] + max(ks.values()))       
        
        return ans
        
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]  
#
#points = [[0,0],[1,1],[0,0]]      

#points = [[0,0],[1,1],[1,-1]]
        
#points = [[0,0],[94911151,94911150],[94911152,94911151]]

test = Solution()
print test.maxPoints(points)                    