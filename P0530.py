# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
		# for BST, in-order traversal gives the sorted list of all nodes
        n, v, res, s = root, float('-inf'), float('inf'), []        
        while n or s:
            while n:
                s.append(n)
                n = n.left            
            n = s.pop()
            res, v, n = min(res, n.val-v), n.val, n.right                
        return(res)