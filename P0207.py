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
        
        # each entry of dictionary is 
        # key: prerequisite
        # values: list of courses you can take after the key
        courses = defaultdict(list)       
        # number of prerequisites for each course
        inDegree = [0] * numCourses
        
        # for each edge, construct the graph
        for crs, pre in prerequisites:      
            # update list of courses you can take after this prerequisite
            courses[pre] += [crs]
            # update the number of prerequisites for this course
            inDegree[crs] += 1        
        
        # perform BFS using a queue, start from couses without any prerequisites     
        q = [idx for idx, iD in enumerate(inDegree) if iD == 0]
        # continue BFS until no new node is placed at the tail
        for node in q:       
            # for each next course you can take after current course            
            for next_node in courses[node]: 
                # if current course is completed
                # the next course then required one fewer course as its prerequisites 
                inDegree[next_node] -= 1
                # if all the prerequisites have been taken for the next course
                if inDegree[next_node] == 0:
                    # now we can take this next course and place it in the queue
                    q.append(next_node)                   
        # if total number of courses we have taken in the queue
        # is equal to the total number of courses
        # then it is possible to finish all courses
        return len(q) == numCourses

numCourses, prerequisites = 2, [[1,0]] 
numCourses, prerequisites = 2, [[1,0],[0,1]]
numCourses, prerequisites = 3, [[0,1],[0,2],[1,2]]
numCourses, prerequisites = 3, [[1,0],[0,2],[2,1]]

test = Solution()
print test.canFinish(numCourses, prerequisites)
    
        
        