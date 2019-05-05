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
        # hash table dictionary[original node]: cloned node
        self.visited = {}     
        
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        # if trivial case or reached end
        if not node:
            return None                
        
        # create a new node
        new_node = Node(node.val, [])    
        # record original node and cloned node in the hash table
        self.visited[node] = new_node                       
        
        # check each neighbor for the original node
        for neighbor in node.neighbors:    
            # if neighbor has already been cloned: retrieve the cloned neighbor 
            # if has not been cloned: clone neighbor recursively
            new_neighbor = self.visited[neighbor] if neighbor in self.visited else self.cloneGraph(neighbor)
            # link cloned neighbor to current node
            new_node.neighbors.append(new_neighbor)
        
        # return the cloned current node
        return new_node
        
        
            