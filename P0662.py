# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
		# level order traversal, child = parent*2+(0,1)
        l, res = [(root,1)], 0        
        while l:
            res, ll = max(res, l[-1][1]-l[0][1]+1), []            
            for node, id in l:
                if node.left: ll += [(node.left, id*2)]
                if node.right: ll += [(node.right, id*2+1)]
            l = ll
        return res