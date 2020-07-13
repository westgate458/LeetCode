# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
		# level order traversal
        if not root: return []
        res, s = [], [root]             
        while s:
            res.append(max([n.val for n in s]))           
            s = [nn for n in s for nn in (n.left, n.right) if nn]            
        return res