# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
		# right-root-left traversal
        s, n, v = [], root, 0
        while s or n:
            while n:
                s.append(n)
                n = n.right
            n = s.pop()
            v += n.val
            n.val, n = v, n.left            
        return root
            
            