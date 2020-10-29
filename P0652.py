# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
		# serialization of subtrees and store in hashmap
        self.d = defaultdict(int)
        self.res = []
        def serialization(node):
            if not node: return ''
            S = str(node.val) + '(' + serialization(node.left) + ')' + '(' + serialization(node.right) + ')'
            if self.d[S] == 1: self.res += [node]
            self.d[S] += 1                
            return S        
        serialization(root)
        return self.res
        