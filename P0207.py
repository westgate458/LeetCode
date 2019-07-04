# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:23:14 2019

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
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
        return len(q) == numCourses

numCourses, prerequisites = 2, [[1,0]] 
numCourses, prerequisites = 2, [[1,0],[0,1]]
numCourses, prerequisites = 3, [[0,1],[0,2],[1,2]]
numCourses, prerequisites = 3, [[1,0],[0,2],[2,1]]

test = Solution()
print test.canFinish(numCourses, prerequisites)
    
        
        