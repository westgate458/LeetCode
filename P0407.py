# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:39:20 2020

@author: Tianqi Guo
"""

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        m, n = len(heightMap), len(heightMap[0])     
        visited = [[False] * n for _ in xrange(m)]
        h = []
        for x in xrange(m):           
            heapq.heappush(h, (heightMap[x][0],x, 0))
            heapq.heappush(h, (heightMap[x][n-1],x, n-1))            
        for y in xrange(n):            
            heapq.heappush(h, (heightMap[0][y], 0, y))
            heapq.heappush(h, (heightMap[m-1][y], m-1, y))
        
        res = 0        
        while h:            
            level, x, y = heapq.heappop(h)
            for xx, yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:      
                if 0<xx<m-1 and 0<yy<n-1 and not visited[xx][yy]:
                    visited[xx][yy] = True                                             
                    if heightMap[xx][yy] < level:
                        res += level - heightMap[xx][yy]                        
                        heapq.heappush(h, (level,xx, yy))   
                    else:
                        heapq.heappush(h, (heightMap[xx][yy],xx, yy))           
        return(res)