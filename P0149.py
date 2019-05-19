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
        # deal with trivial case
        if not points:
            return 0 
        # convert list to tuples for hash table
        points = [(point[0],point[1]) for point in points]
        # hash table for number of occurances of each point
        points_dict = defaultdict(int)
        # count occurances
        for point in points:
            points_dict[point] += 1
        # only retain unique points
        points = list(set(points))   
        # number of unique points                
        Np = len(points)
        # deal with another trivial case
        if Np == 1:
            return points_dict.values()[0]      
        # max number of points
        ans = 0
        # try each combination of two unique points
        for i in xrange(Np-1):
            # slopes from first point
            # first point + slope -> one unique line
            ks = defaultdict(int)
            # all possible second points
            for j in xrange(i+1,Np):
                # the differences in (x, y) coordinates
                dx, dy = points[i][0] - points[j][0], points[i][1] - points[j][1]              
                # special case of vertical line
                if dx == 0:
                    # denote slope by None
                    k = None 
                # slopes of other regular lines
                else:
                    # convert to float for precision
                    k = float(dy)/dx                
                # update number of points on this unique line
                # addition is the number of occurances of the second point
                ks[k] += points_dict[points[j]]                         
            # after all second points are examined
            # update the max number of points on any line
            ans = max(ans, points_dict[points[i]] + max(ks.values()))       
        # return the max number of points on any line
        return ans
        
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]  
#
#points = [[0,0],[1,1],[0,0]]      

#points = [[0,0],[1,1],[1,-1]]
        
#points = [[0,0],[94911151,94911150],[94911152,94911151]]

test = Solution()
print test.maxPoints(points)                    