# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
		# level order traversal
        s = [root]        
        while s:
            ans = s[0].val            
            s = [nn for n in s for nn in (n.left, n.right) if nn]            
        return ans
            