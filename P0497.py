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
        # accumulative area
        area = 0
        # record accumulative area for each rectangle
        self.areas = [0]
        # also record the side length, and coordinates of bot-left point
        self.rects = [[]]       
        # deal with each rectangle
        for x1, y1, x2, y2 in rects:
            # side lengths
            xx, yy = x2-x1+1, y2-y1+1
            # update accumulative area
            area += xx*yy
            # record accumulative area
            self.areas.append(area)   
            # record current rectangle
            self.rects.append((xx,x1,y1))        

    def pick(self):
        """
        :rtype: List[int]
        """        
        # generate the random number
        # each point in all the rectangles is now represented by one number in the range [0, total_area)
        target = random.randrange(self.areas[-1])   
        # find which rectangle this point belongs to
        i = bisect.bisect_right(self.areas, target) 
        # with the rectangle determined, recover the coordinates of the random point within this rectangle
        y, x = divmod(target-self.areas[i-1],self.rects[i][0])        
        # the absolute coodinates
        return x+self.rects[i][1],y+self.rects[i][2]     

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()