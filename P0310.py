# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:17:12 2019

@author: Tianqi Guo
"""

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        # Solution 1 beats 96.38%: optimized
        if n == 1:
            return [0]        
        neighbors = [set() for _ in xrange(n)]          
        for n1, n2 in edges:       
            neighbors[n1].add(n2)
            neighbors[n2].add(n1)
        q = [idx for idx, neighbor in enumerate(neighbors) if len(neighbor) == 1]        
        while n > 2:
            n -= len(q)
            new_q = []
            for node in q:
                for next_node in neighbors[node]: 
                    neighbors[next_node].remove(node)
                    if len(neighbors[next_node]) == 1:
                        new_q.append(next_node)                             
            q = new_q        
        return q
        
        # Solution 2 beats 5.12%: adapted from P207
        from collections import defaultdict
        neighbors = defaultdict(list)       
        inDegree = [0] * n
        depths = [0] * n        
        for n1, n2 in edges:       
            neighbors[n1] += [n2]
            neighbors[n2] += [n1]
            inDegree[n1] += 1        
            inDegree[n2] += 1 
        q = [idx for idx, iD in enumerate(inDegree) if iD == 1]        
        for node in q:            
            for next_node in neighbors[node]: 
                inDegree[next_node] -= 1
                if inDegree[next_node] == 1:
                    q.append(next_node)     
                    depths[next_node] = depths[node] + 1 
        return [idx for idx, depth in enumerate(depths) if depth == max(depths)]
    
n = 4
edges = [[1, 0], [1, 2], [1, 3]]


n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

    
test = Solution()
print(test.findMinHeightTrees(n, edges))

