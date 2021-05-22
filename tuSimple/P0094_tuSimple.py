# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:                
        s, res = [], []
        while s or root:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            res.append(root.val)
            root = root.right        
        return(res)