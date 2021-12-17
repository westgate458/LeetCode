# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete = set(to_delete)    
        res = [] if root.val in to_delete else [root]            
        q = [root]        
        for node in q:            
            if node.left:
                q.append(node.left)
                if node.left.val in to_delete:
                    node.left = None
                elif node.val in to_delete:                
                    res.append(node.left)
            if node.right:
                q.append(node.right)
                if node.right.val in to_delete:
                    node.right = None  
                elif node.val in to_delete: 
                    res.append(node.right) 
        return res
                