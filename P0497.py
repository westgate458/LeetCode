# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 01:22:26 2020

@author: Tianqi Guo
"""

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        area = 0
        self.areas = [0]
        self.rects = [[]]       
        for x1, y1, x2, y2 in rects:
            xx, yy = x2-x1+1, y2-y1+1
            area += xx*yy
            self.areas.append(area)   
            self.rects.append((xx,x1,y1))        

    def pick(self):
        """
        :rtype: List[int]
        """        
        target = random.randrange(self.areas[-1])        
        i = bisect.bisect_right(self.areas, target)  
        y, x = divmod(target-self.areas[i-1],self.rects[i][0])        
        return x+self.rects[i][1],y+self.rects[i][2]     

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()