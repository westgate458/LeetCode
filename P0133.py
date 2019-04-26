# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:40:56 2019

@author: Tianqi Guo
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    
    def __init__(self):
        self.visited = {}     
        
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None                
            
        new_node = Node(node.val, [])    
        self.visited[node] = new_node                       
            
        for neighbor in node.neighbors:    
            new_neighbor = self.visited[neighbor] if neighbor in self.visited else self.cloneGraph(neighbor)
            new_node.neighbors.append(new_neighbor)
            
        return new_node
        
        
            