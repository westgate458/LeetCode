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
        # deal with trivial case
        if not heightMap:
            return 0
        # size of the map
        m, n = len(heightMap), len(heightMap[0])     
        # record if each tile has been visited yet
        visited = [[False] * n for _ in xrange(m)]
        # heap for BFS
        h = []
        # push all border tiles into the heap
        for x in xrange(m):           
            heapq.heappush(h, (heightMap[x][0],x, 0))
            heapq.heappush(h, (heightMap[x][n-1],x, n-1))            
        for y in xrange(n):            
            heapq.heappush(h, (heightMap[0][y], 0, y))
            heapq.heappush(h, (heightMap[m-1][y], m-1, y))
        # res is the total amount of water trapped
        res = 0        
        # continue BFS until all tiles have been considered
        while h:            
            # level of previous tile, and its position
            level, x, y = heapq.heappop(h)
            # check its four neighbors
            for xx, yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:      
                # if neighbor tile is within the board
                # and we have not visited it yet
                if 0<xx<m-1 and 0<yy<n-1 and not visited[xx][yy]:
                    # mark it visited
                    visited[xx][yy] = True                                             
                    # if neighbor tile is lower in height                    
                    if heightMap[xx][yy] < level:
                        # then the highest water level it could hold is the current level
                        # update trapped water volume
                        res += level - heightMap[xx][yy]                        
                        # push this tile into the heap
                        # and since this tile can only hold current water level
                        # then its neighbors won't hold water of higher level as well
                        heapq.heappush(h, (level,xx, yy))   
                    # if neighbor tile is higher
                    else:
                        # then it won't hold water now, push it into heap for later visit
                        heapq.heappush(h, (heightMap[xx][yy],xx, yy))           
        # all trapped water has been calculated
        return(res)