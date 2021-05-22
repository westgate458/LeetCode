"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        if not root: return None        
        head = pre = Node(0)                
        s = []      
        while s or root:                       
            while root:
                s.append(root)                    
                root = root.left                    
            root = s.pop()           
            
            pre.right, root.left = root, pre             
            pre, root = root, root.right            
         
        pre.right, head.right.left = head.right, pre        
        
        return(head.right)