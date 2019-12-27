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
        d = defaultdict(dict)
        for i in xrange(len(equations)):
            d[equations[i][0]][equations[i][1]]  = values[i]
            d[equations[i][1]][equations[i][0]]  = 1./values[i]     
        def search(query):
            m, n = query
            if m in d and n in d:                
                routes = deque([[m]])
                ratios = deque([1])                
                while routes:
                    route = routes.popleft()
                    ratio = ratios.popleft()
                    if route[-1] == n:
                        return(ratio)
                    for y in d[route[-1]]:
                        if y not in route:
                            routes.append(route+[y])
                            ratios.append(ratio*d[route[-1]][y])
            return(-1)                    
        return([search(query) for query in queries])
        