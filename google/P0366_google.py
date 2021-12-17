# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.d = defaultdict(list)
        def DFS(node):
            if not node: return 0      
            t = max(DFS(node.left),DFS(node.right))+1
            self.d[t].append(node.val)
            return t        
        _ = DFS(root)
        return self.d.values()
            