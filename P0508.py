# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
		# calculate tree sum at all nodes and update hash table
        self.d = defaultdict(int)
        def helper(node):        
            if not node: return 0
            s = helper(node.left) + helper(node.right) + node.val
            self.d[s] += 1
            return s
        helper(root)
        max_f = 0
        res = []
        for key in self.d:
            if self.d[key] == max_f:
                res += [key]
            elif self.d[key] > max_f:
                max_f = self.d[key]
                res = [key]
        return res