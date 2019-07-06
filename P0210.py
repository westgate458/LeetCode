# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:06:33 2019

@author: Tianqi Guo
"""
from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        courses = defaultdict(list)       
        inDegree = [0] * numCourses
        
        for crs, pre in prerequisites:       
            courses[pre] += [crs]
            inDegree[crs] += 1        
        
        q = [idx for idx, iD in enumerate(inDegree) if iD == 0]        
        for node in q: 
            for next_node in courses[node]: 
                inDegree[next_node] -= 1
                if inDegree[next_node] == 0:
                    q.append(next_node)                   
        return q if len(q) == numCourses else []
