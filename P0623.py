# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
		# simple recursion
        if root:
            if d == 1:
                return TreeNode(v, root, None)
            elif d == 2:
                root.left, root.right = TreeNode(v, root.left, None), TreeNode(v, None, root.right)                 
            else:
                self.addOneRow(root.left, v, d-1)
                self.addOneRow(root.right, v, d-1)
        return root
            