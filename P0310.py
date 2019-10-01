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
        # deal with trivial case
        if n == 1:
            return [0]        
        # record all nodes that each node is connected to
        neighbors = [set() for _ in xrange(n)]          
        # for each edge, add each node to the other node's neighbors
        for n1, n2 in edges:       
            neighbors[n1].add(n2)
            neighbors[n2].add(n1)
        # deleting nodes, start from the ones that only connected to one
        q = [idx for idx, neighbor in enumerate(neighbors) if len(neighbor) == 1]        
        # continue deleting, until only one or two nodes are left
        while n > 2:
            # update number of remaining after this round
            n -= len(q)
            # next layer to be deleted
            new_q = []
            # check each node to be deleted
            for node in q:
                # update all of its neighbor
                for next_node in neighbors[node]: 
                    # remove current node from their neighbors
                    neighbors[next_node].remove(node)
                    # if the neighbor now only has one node connected to it
                    if len(neighbors[next_node]) == 1:
                        # it belongs to the next layer to be removed
                        new_q.append(next_node)                             
            # after all current layer has been removed, move on to next layer
            q = new_q        
        # the last layer contains the last one or two nodes 
        # that have the same distances from both ends (leaves)
        # which leads to the MHT
        return q
        
#        # Solution 2 beats 5.12%: adapted from P207
#        from collections import defaultdict
#        neighbors = defaultdict(list)       
#        inDegree = [0] * n
#        depths = [0] * n        
#        for n1, n2 in edges:       
#            neighbors[n1] += [n2]
#            neighbors[n2] += [n1]
#            inDegree[n1] += 1        
#            inDegree[n2] += 1 
#        q = [idx for idx, iD in enumerate(inDegree) if iD == 1]        
#        for node in q:            
#            for next_node in neighbors[node]: 
#                inDegree[next_node] -= 1
#                if inDegree[next_node] == 1:
#                    q.append(next_node)     
#                    depths[next_node] = depths[node] + 1 
#        return [idx for idx, depth in enumerate(depths) if depth == max(depths)]
    
n = 4
edges = [[1, 0], [1, 2], [1, 3]]


n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

    
test = Solution()
print(test.findMinHeightTrees(n, edges))

