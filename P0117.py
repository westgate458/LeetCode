# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:10:10 2019

@author: Tianqi Guo
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """     
        
        
        # Solution 1: level order traversal (cheat, not constant extra space)        
        # deal with trivial case
        if not root:            
            return 
        # stack storing nodes at each level
        s = [root]  
        # continue traversing while still nodes left
        while s: 
            # stack stores nodes on next level
            new_s = []            
            # check each node on current level
            for n in s:
                # place child nodes into new stack if they exist
                if n.left:
                    new_s.append(n.left)
                if n.right:
                    new_s.append(n.right)      
                    
            # connect child nodes on next level
            for i in range(len(new_s)-1):
                new_s[i].next  = new_s[i+1]            
            # update the stack for traversal
            s = new_s 
        # return the connected tree
        return root
    
        # Solution 2: modification from P0116, constant extra space
#        # deal with trivial case
#        if not root:            
#            return         
#        current_level = root
#        if root.left:
#            next_level = root.left
#        elif root.right:
#            next_level = root.right    
#        else:
#            next_level = None 
#        while current_level.left or current_level.right or current_level.next or next_level:
#            current_level_next = current_level.next            
#            if current_level_next:                
#                while (not (current_level_next.left or current_level_next.right)) and current_level_next.next:
#                    current_level_next = current_level_next.next             
#            if current_level.left:               
#                if not next_level:
#                    next_level = current_level.left
#                if current_level.right:
#                    current_level.left.next = current_level.right                    
#                elif current_level_next:
#                    if current_level_next.left:
#                        current_level.left.next = current_level_next.left
#                    elif current_level_next.right:
#                        current_level.left.next = current_level_next.right
#            if current_level.right:                
#                if not next_level:
#                    next_level = current_level.right
#                if current_level_next:                 
#                    if current_level_next.left:
#                        current_level.right.next = current_level_next.left
#                    elif current_level_next.right:
#                        current_level.right.next = current_level_next.right
#            if current_level_next:                
#                current_level = current_level.next
#            else:                
#                current_level = next_level
#                next_level = None
#        return root  