# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        s, res = [root], []        
        while s:           
            res.append([n.val for n in s])
            s = [c for n in s for c in [n.left, n.right] if c]
        return(res)
            
        