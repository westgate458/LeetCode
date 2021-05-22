# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """        
        s, pre = [root], TreeNode()               
        while s:            
            n = s.pop()
            if n:                
                s += [n.right, n.left]
                pre.right, n.left, pre = n, None, n