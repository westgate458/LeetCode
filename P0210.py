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
        # for detailed comments see P207
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
      
        # the timing to take each course when all its prerequisites have been taken
        # i.e. when its inDegree is zero
        # so the order of appearance of each course in q
        # is the order of courses one should take to finish all courses
        return q if len(q) == numCourses else []
