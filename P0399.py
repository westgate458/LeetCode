# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 20:59:04 2019

@author: Tianqi Guo
"""

from collections import defaultdict, deque
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """        
        # construct the map
        d = defaultdict(dict)
        # two way graph with nodes as equations and values as edges
        for i in xrange(len(equations)):
            d[equations[i][0]][equations[i][1]]  = values[i]
            d[equations[i][1]][equations[i][0]]  = 1./values[i]    
        # BFS function for each ratio query
        def search(query):
            # the two ends of the path in query
            m, n = query
            # if two equations exist as nodes in the graph
            if m in d and n in d:                
                # initialize the BFS queue
                # routes: paths already seen so far
                # ratios: the ratio along each path
                routes = deque([[m]])
                ratios = deque([1])                
                # continue while the end has not been visited
                while routes:
                    # check next route in queue
                    route = routes.popleft()
                    ratio = ratios.popleft()
                    # if target is the end of current route
                    if route[-1] == n:
                        # return the ratio
                        return(ratio)
                    # if the target has not been visited
                    # check all nodes connected to current node
                    for y in d[route[-1]]:
                        # if it has not been visited on current route
                        if y not in route:
                            # update route and ratio and push them into the BFS queue
                            routes.append(route+[y])
                            ratios.append(ratio*d[route[-1]][y])
            # if no viable path is found, return -1
            return(-1)                    
        # for each query, call the function to solve for the ratio
        return([search(query) for query in queries])
        