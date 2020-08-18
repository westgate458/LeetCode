"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """       
        # simple recursion
        if quadTree1.isLeaf == 1:
            if quadTree1.val == 1: return quadTree1
            else: return quadTree2
        elif quadTree2.isLeaf == 1:
            if quadTree2.val == 1: return quadTree2
            else: return quadTree1        

        TL, TR, BL, BR = self.intersect(quadTree1.topLeft, quadTree2.topLeft), \
                         self.intersect(quadTree1.topRight, quadTree2.topRight), \
                         self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft), \
                         self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)                    
                
        if TL.isLeaf == 1 and TR.isLeaf == 1 and BL.isLeaf == 1 and BR.isLeaf == 1 and (TL.val == TR.val == BL.val == BR.val):
            return Node(TL.val, 1, None, None, None, None)            
        else:
            return Node(0, 0, TL, TR, BL, BR)   
