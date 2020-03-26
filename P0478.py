# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:45:22 2020

@author: Tianqi Guo
"""

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        # Solution 1 beats 82.81%: generate any distrubution from uniform distribution
        r = self.r * random.random()**0.5        
        a = random.random() * 360.0     
        return([self.x+r*math.cos(a),self.y+r*math.sin(a)])
        
        # Solution 2 beats 70.31%: reject sampling
        r = float('inf')
        while r > self.r:
            dx = (random.random()*2-1)*self.r
            dy = (random.random()*2-1)*self.r
            r = (dx**2 + dy**2)**0.5
        return([self.x+dx,self.y+dy])

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()