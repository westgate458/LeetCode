import abc 
from abc import ABCMeta, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node:
    __metaclass__ = ABCMeta
    # define your fields here
    #@abstractmethod
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def evaluate(self):
        if self.val not in '+-*/':
            return int(self.val)
        else:
            l = self.left.evaluate()
            r = self.right.evaluate()
            if self.val == '+':
                return l+r
            elif self.val == '-':
                return l-r
            elif self.val == '*':
                return l*r
            elif self.val == '/':
                return l/r


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix):
        """
        :type s: List[str]
        :rtype: int
        """
        s = []
        for c in postfix:
            if c in '+-*/':
                node = Node(c)
                node.right = s.pop()
                node.left = s.pop()
                s.append(node)
            else:
                s.append(Node(c))
        
        return s[-1]
        

"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        