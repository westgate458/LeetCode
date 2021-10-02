# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = [(0,root)]
        res = defaultdict(list)
        
        for col, node in levels:
            if node:                
                res[col].append(node.val)
                levels.append((col-1,node.left))
                levels.append((col+1,node.right))
        
        return [res[k] for k in sorted(res.keys())]