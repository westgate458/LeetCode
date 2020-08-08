# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
		# Compare within, return max out
        self.res = 0
        def helper(node):            
            if not node: return 0            
            l, r = helper(node.left), helper(node.right)                        
            self.res = max(self.res,l+r)
            return max(l,r)+1
        helper(root)
        return self.res
            